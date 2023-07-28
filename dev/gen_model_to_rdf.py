# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0

"""
Auto-generates the (majority of the) RDF writer code from the SPDX3 model.

Usage: fetch a fresh copy of the spdx-3-model and the spec-parser, then generate a json dump of the model with
the spec-parser:

    python main.py --json-dump ../spdx-3-model/model

Copy the generated `model_dump.json` in `md_generated` next to this file, then run it:

    python gen_model_to_rdf.py

Commit resulting changes.
"""

import json
import os.path
from pathlib import Path
from typing import IO

from spdx_tools.spdx.casing_tools import camel_case_to_snake_case

FILE_HEADER = """# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_model_to_rdf.py
# Do not manually edit!
# flake8: noqa
# isort:skip_file

# fmt: off

from rdflib import Graph, URIRef, RDF, Literal, BNode
from rdflib.term import Identifier
from spdx_tools.spdx.casing_tools import snake_case_to_camel_case
{namespace_imports}


"""

CLS_CONVERTER_FUNC_BODY = """def {type_name}_to_rdf(obj, graph: Graph) -> Identifier:
    if '_spdx_id' in obj.__dict__:
        element_node = URIRef(obj.spdx_id)
    else:
        element_node = BNode()
    type_node = URIRef("{type_id}")
    graph.add((element_node, RDF.type, type_node))
    {type_name}_properties_to_rdf(element_node, obj, graph)
    return element_node


"""

CLS_CONVERTER_PROPERTIES_FUNC_BODY = """def {type_name}_properties_to_rdf(node: Identifier, obj, graph: Graph):
    from .converter import model_to_rdf{properties}{parent_call}


"""

PROP_CONVERTER_BODY = """
    if obj.{prop_name} is not None:
        prop_node = URIRef("{prop_id}")
        value = obj.{prop_name}
        graph.add((node, prop_node, {prop_conversion_code}))"""

PROP_LIST_CONVERTER_BODY = """
    for value in obj.{prop_name}:
        prop_node = URIRef("{prop_id}")
        graph.add((node, prop_node, {prop_conversion_code}))"""

PROP_DICT_CONVERTER_BODY = """
    for key, value in obj.{prop_name}.items():
        dict_node = BNode()
        graph.add((dict_node, RDF.type, URIRef("https://spdx.org/rdf/v3/Core/DictionaryEntry")))
        key_node = URIRef("https://spdx.org/rdf/v3/Core/key")
        graph.add((dict_node, key_node, Literal(key, datatype="http://www.w3.org/2001/XMLSchema#string")))
        if value is not None:
            value_node = URIRef("https://spdx.org/rdf/v3/Core/value")
            graph.add((dict_node, value_node, Literal(value, datatype="http://www.w3.org/2001/XMLSchema#string")))
        prop_node = URIRef("{prop_id}")
        graph.add((node, prop_node, dict_node))"""

VOCAB_CONVERTER_FUNC_BODY = """def {type_name}_to_rdf(obj, graph: Graph) -> Identifier:
    from .converter import enum_value_to_str
    name = enum_value_to_str(obj)
    return URIRef("{vocab_id}/" + name)


"""

MAIN_FILE_HEADER = """# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_model_to_rdf.py
# Do not manually edit!
# flake8: noqa
# fmt: off
# isort:skip_file

from beartype.typing import List, Optional, Dict, Callable
from rdflib import Graph, Literal, URIRef
from rdflib.term import Identifier
from spdx_tools.spdx.casing_tools import snake_case_to_camel_case
from spdx_tools.spdx3.model import HashAlgorithm
{namespace_imports}

"""

MAIN_CONVERTER_MAP = """
_CONVERTER_FUNCTIONS: Dict[str, Callable[[any, Graph], Identifier]] = {{
{converters}
}}

"""

MAIN_MODULE_MAP = """
def module_to_namespace(module: str) -> Optional[str]:
    if not module.startswith("spdx_tools.spdx3.model"):
        return None
{module_tests}
    return "Core"

"""

MAIN_MODULE_TEST = """    if module.startswith("spdx_tools.spdx3.model.{snake_namespace_name}"):
        return "{namespace_name}\""""

MAIN_CONVERTER_FUNC = """
def literal_to_rdf(obj, _: Graph) -> Identifier:
    return Literal(obj)


def enum_value_to_str(obj) -> str:
    if obj == HashAlgorithm.BLAKE2B256:
        return "blake2b256"
    if obj == HashAlgorithm.BLAKE2B384:
        return "blake2b384"
    if obj == HashAlgorithm.BLAKE2B512:
        return "blake2b512"
    if obj == HashAlgorithm.SHA3_224:
        return "sha3_224"
    if obj == HashAlgorithm.SHA3_256:
        return "sha3_224"
    if obj == HashAlgorithm.SHA3_384:
        return "sha3_384"
    if obj == HashAlgorithm.SHA3_512:
        return "sha3_512"
    return snake_case_to_camel_case(obj.name.lower())


def model_to_rdf(obj, graph: Graph) -> Identifier:
    if isinstance(obj, str):
        return URIRef(obj)
    type_name = obj.__class__.__qualname__
    module_name = obj.__class__.__module__
    namespace = module_to_namespace(module_name)
    if namespace is None:
        return literal_to_rdf(obj, graph)

    lookup = f"{namespace}/{type_name}"
    converter = _CONVERTER_FUNCTIONS[lookup] if lookup in _CONVERTER_FUNCTIONS else literal_to_rdf
    return converter(obj, graph)
"""

FINAL_LINE = """# fmt: on
"""

output_dir = os.path.join(os.path.dirname(__file__), "../src/spdx_tools/spdx3/writer/rdf/converters")


def prop_name_to_python(prop_name: str):
    special_cases = {"from": "from_element", "homePage": "homepage"}
    if prop_name in special_cases:
        return special_cases[prop_name]
    return camel_case_to_snake_case(prop_name)


def namespace_name_to_python(namespace_name: str):
    special_cases = {"AI": "ai"}
    if namespace_name in special_cases:
        return special_cases[namespace_name]
    return camel_case_to_snake_case(namespace_name)


class GenModelToRdf:
    prop_name_to_id: dict[str, str]
    class_to_converter_func: dict[str, str]
    namespace_imports: str

    def __init__(self):
        self.prop_name_to_id = {}
        self.class_to_converter_func = {}
        self.namespace_imports = ""

    def create_namespace_import(self, model: dict):
        namespaces = [namespace_name_to_python(namespace["name"]) for namespace in model.values()]
        if namespaces:
            self.namespace_imports = "from . import " + ", ".join(namespaces)

    def map_prop_names_to_ids(self, model: dict):
        for namespace in model.values():
            namespace_name = namespace["name"]
            for prop_name, prop in namespace["properties"].items():
                full_prop_name = f"{namespace_name}/{prop_name}"
                prop_id = prop["metadata"]["id"]
                self.prop_name_to_id[full_prop_name] = prop_id

    def is_literal_type(self, typename: str, namespace_name: str, model: dict) -> bool:
        if typename.startswith('/'):
            typename = typename[1:]
        if typename.startswith("xsd:"):
            return True
        if '/' in typename:
            namespace_name, _, typename = typename.partition('/')

        namespace = model.get(namespace_name)
        clazz = None
        if namespace:
            if typename in namespace["vocabs"]:
                return False
            clazz = namespace["classes"].get(typename)

        if not clazz:
            return True
        parent_class = clazz["metadata"].get("SubclassOf") or "none"
        if parent_class == "none" or parent_class.startswith("xsd:"):
            return not clazz["properties"]
        return False

    def get_type_uri(self, typename: str, namespace_name: str) -> str:
        if typename.startswith('/'):
            typename = typename[1:]
        if typename.startswith("xsd:"):
            return typename.replace("xsd:", "http://www.w3.org/2001/XMLSchema#")
        if '/' in typename:
            namespace_name, _, typename = typename.partition('/')
        return f"https://spdx.org/rdf/v3/{namespace_name}/{typename}"

    def prop_conversion_code(self, typename: str, namespace_name: str, model: dict) -> str:
        if self.is_literal_type(typename, namespace_name, model):
            return f"Literal(value, datatype=\"{self.get_type_uri(typename, namespace_name)}\")"
        return "model_to_rdf(value, graph)"

    def handle_class(self, output_file: IO[str], clazz: dict, namespace_name: str, model: dict):
        parent_class = clazz["metadata"].get("SubclassOf")
        if parent_class == "none":
            parent_class = None
        if parent_class == "xsd:string":
            return

        type_name = camel_case_to_snake_case(clazz["metadata"]["name"])
        self.class_to_converter_func[
            f"{namespace_name}/{clazz['metadata']['name']}"
        ] = f"{namespace_name_to_python(namespace_name)}.{type_name}_to_rdf"
        output_file.write(CLS_CONVERTER_FUNC_BODY.format(type_name=type_name, type_id=clazz["metadata"]["id"]))

        prop_code = ""
        # ignore spdxId, as we'll use it implicitly for the RDF URI
        # ignore extension as it is currently not fully specified and can't be mapped in a sensible way
        ignored_props = ["spdxId", "extension"]
        for prop_name, prop in clazz["properties"].items():
            if prop_name in ignored_props:
                continue
            if prop_name.startswith('/'):
                prop_name = prop_name[1:]
            full_prop_name = f"{namespace_name}/{prop_name}" if "/" not in prop_name else prop_name
            _, _, prop_name = full_prop_name.partition("/")
            is_list = prop.get("maxCount") != "1"
            prop_conversion_code = self.prop_conversion_code(prop["type"], namespace_name, model)
            if "DictionaryEntry" in prop["type"]:
                prop_code += PROP_DICT_CONVERTER_BODY.format(
                    prop_name=prop_name_to_python(prop_name),
                    prop_id=self.prop_name_to_id[full_prop_name],
                )
            elif is_list:
                prop_code += PROP_LIST_CONVERTER_BODY.format(
                    prop_name=prop_name_to_python(prop_name),
                    prop_id=self.prop_name_to_id[full_prop_name],
                    prop_conversion_code=prop_conversion_code
                )
            else:
                prop_code += PROP_CONVERTER_BODY.format(
                    prop_name=prop_name_to_python(prop_name),
                    prop_id=self.prop_name_to_id[full_prop_name],
                    prop_conversion_code=prop_conversion_code
                )

        parent_call = ""
        if parent_class:
            if parent_class.startswith("/"):
                parent_class = parent_class[1:]
            if "/" in parent_class:
                parent_namespace, _, parent_class = parent_class.partition("/")
            else:
                parent_namespace = namespace_name
            parent_call = f"\n    {namespace_name_to_python(parent_namespace)}.{camel_case_to_snake_case(parent_class)}_properties_to_rdf(node, obj, graph)"

        output_file.write(
            CLS_CONVERTER_PROPERTIES_FUNC_BODY.format(
                type_name=type_name, properties=prop_code, parent_call=parent_call
            )
        )

    def handle_vocab(self, output_file: IO[str], vocab: dict, namespace_name: str):
        type_name = camel_case_to_snake_case(vocab["metadata"]["name"])
        self.class_to_converter_func[
            f"{namespace_name}/{vocab['metadata']['name']}"
        ] = f"{namespace_name_to_python(namespace_name)}.{type_name}_to_rdf"
        output_file.write(VOCAB_CONVERTER_FUNC_BODY.format(type_name=type_name, vocab_id=vocab["metadata"]["id"]))

    def handle_namespace(self, output_file: IO[str], namespace: dict, model: dict):
        namespace_name = namespace["name"]
        for clazz in namespace["classes"].values():
            self.handle_class(output_file, clazz, namespace_name, model)
        for vocab in namespace["vocabs"].values():
            self.handle_vocab(output_file, vocab, namespace_name)

    def create_main_converter(self, model: dict):
        with open(os.path.join(output_dir, "converter.py"), "w") as output_file:
            output_file.write(MAIN_FILE_HEADER.format(namespace_imports=self.namespace_imports))
            converters = ",\n".join(
                [
                    f'    "{class_name}": {converter_func}'
                    for class_name, converter_func in self.class_to_converter_func.items()
                ]
            )
            output_file.write(MAIN_CONVERTER_MAP.format(converters=converters))
            module_tests = "\n".join(
                [
                    MAIN_MODULE_TEST.format(
                        snake_namespace_name=namespace_name_to_python(namespace["name"]),
                        namespace_name=namespace["name"],
                    )
                    for namespace in model.values()
                ]
            )
            output_file.write(MAIN_MODULE_MAP.format(module_tests=module_tests))
            output_file.write(MAIN_CONVERTER_FUNC)
            output_file.write(FINAL_LINE)

    def run(self):
        os.makedirs(output_dir, exist_ok=True)
        Path(os.path.join(output_dir, "__init__.py")).touch()

        with open("model_dump.json") as model_file:
            model = json.load(model_file)

        self.create_namespace_import(model)
        self.map_prop_names_to_ids(model)

        for namespace in model.values():
            module_name = namespace_name_to_python(namespace["name"])
            with open(os.path.join(output_dir, f"{module_name}.py"), "w") as output_file:
                output_file.write(FILE_HEADER.format(namespace_imports=self.namespace_imports))
                self.handle_namespace(output_file, namespace, model)
                output_file.write(FINAL_LINE)

        self.create_main_converter(model)


if __name__ == "__main__":
    GenModelToRdf().run()
