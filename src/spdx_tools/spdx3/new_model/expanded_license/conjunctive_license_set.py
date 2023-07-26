# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..core import CreationInfo, ExternalIdentifier, ExternalReference, IntegrityMethod
from ..licensing import AnyLicenseInfo
from beartype.typing import List, Optional
from dataclasses import field
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class ConjunctiveLicenseSet(AnyLicenseInfo):
    """
    A ConjunctiveLicenseSet indicates that _each_ of its subsidiary AnyLicenseInfos apply. In other words, a
    ConjunctiveLicenseSet of two or more licenses represents a licensing situation where _all_ of the specified licenses
    are to be complied with. It is represented in the SPDX License Expression Syntax by the `AND` operator.

    It is syntactically correct to specify a ConjunctiveLicenseSet where the subsidiary AnyLicenseInfos may be
    "incompatible" according to a particular interpretation of the corresponding Licenses. The SPDX License Expression
    Syntax does not take into account interpretation of license texts, which is left to the consumer of SPDX data to
    determine for themselves.
    """
    member: List[AnyLicenseInfo] = field(default_factory=list)
    """
    A member is a license expression participating in a conjuctive (of type ConjunctiveLicenseSet) or a disjunctive (of
    type DisjunctiveLicenseSet) license set.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        member: List[AnyLicenseInfo],
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
