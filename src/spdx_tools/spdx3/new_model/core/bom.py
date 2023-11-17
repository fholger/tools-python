# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from ..core.bundle import Bundle
from ..core.creation_info import CreationInfo
from ..core.external_identifier import ExternalIdentifier
from ..core.external_map import ExternalMap
from ..core.external_reference import ExternalReference
from ..core.integrity_method import IntegrityMethod


@dataclass_with_properties
class Bom(Bundle):
    """
    A Bill Of Materials (BOM) is a container for a grouping of SPDX-3.0 content characterizing details about a product.
    This could include details of the content and composition of the product, provenence details of the product and/or
    its composition, licensing information, known quality or security issues, etc.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        element: List[str],
        root_element: List[str],
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
        imports: List[ExternalMap] = None,
        context: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        imports = [] if imports is None else imports
        check_types_and_set_values(self, locals())