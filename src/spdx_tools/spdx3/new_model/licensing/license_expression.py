# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..core import CreationInfo, ExternalIdentifier, ExternalReference, IntegrityMethod
from ..licensing import AnyLicenseInfo
from beartype.typing import List, Optional
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class LicenseExpression(AnyLicenseInfo):
    """
    Often a single license can be used to represent the licensing terms of a source code or binary file, but there are
    situations where a single license identifier is not sufficient. A common example is when software is offered under a
    choice of one or more licenses (e.g., GPL-2.0-only OR BSD-3-Clause). Another example is when a set of licenses is
    needed to represent a binary program constructed by compiling and linking two (or more) different source files each
    governed by different licenses (e.g., LGPL-2.1-only AND BSD-3-Clause).

    SPDX License Expressions provide a way for one to construct expressions that more accurately represent the licensing
    terms typically found in open source software source code. A license expression could be a single license identifier
    found on the SPDX License List; a user defined license reference denoted by the LicenseRef-idString; a license
    identifier combined with an SPDX exception; or some combination of license identifiers, license references and
    exceptions constructed using a small set of defined operators (e.g., AND, OR, WITH and +). We provide the definition
    of what constitutes a valid an SPDX License Expression in this section.
    """
    license_expression: str
    """
    Often a single license can be used to represent the licensing terms of a source code or binary file, but there are
    situations where a single license identifier is not sufficient. A common example is when software is offered under a
    choice of one or more licenses (e.g., GPL-2.0-only OR BSD-3-Clause). Another example is when a set of licenses is
    needed to represent a binary program constructed by compiling and linking two (or more) different source files each
    governed by different licenses (e.g., LGPL-2.1-only AND BSD-3-Clause).

    SPDX License Expressions provide a way for one to construct expressions that more accurately represent the licensing
    terms typically found in open source software source code. A license expression could be a single license identifier
    found on the SPDX License List; a user defined license reference denoted by the LicenseRef-idString; a license
    identifier combined with an SPDX exception; or some combination of license identifiers, license references and
    exceptions constructed using a small set of defined operators (e.g., AND, OR, WITH and +). We provide the definition
    of what constitutes a valid an SPDX License Expression in this section.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        license_expression: str,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        check_types_and_set_values(self, locals())
