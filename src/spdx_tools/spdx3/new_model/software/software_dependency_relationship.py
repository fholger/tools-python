# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from datetime import datetime

from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from ..core.creation_info import CreationInfo
from ..core.external_identifier import ExternalIdentifier
from ..core.external_reference import ExternalReference
from ..core.integrity_method import IntegrityMethod
from ..core.lifecycle_scope_type import LifecycleScopeType
from ..core.lifecycle_scoped_relationship import LifecycleScopedRelationship
from ..core.relationship_completeness import RelationshipCompleteness
from ..core.relationship_type import RelationshipType
from ..software.dependency_conditionality_type import DependencyConditionalityType
from ..software.software_dependency_link_type import SoftwareDependencyLinkType


@dataclass_with_properties
class SoftwareDependencyRelationship(LifecycleScopedRelationship):
    """
    TODO
    """

    software_linkage: Optional[SoftwareDependencyLinkType] = None
    """
    A softwareLinkage is TODO
    """
    conditionality: Optional[DependencyConditionalityType] = None
    """
    A conditionality is TODO
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        from_element: str,
        relationship_type: RelationshipType,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
        to: List[str] = None,
        completeness: Optional[RelationshipCompleteness] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        scope: Optional[LifecycleScopeType] = None,
        software_linkage: Optional[SoftwareDependencyLinkType] = None,
        conditionality: Optional[DependencyConditionalityType] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        to = [] if to is None else to
        check_types_and_set_values(self, locals())
