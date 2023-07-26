# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..core import CreationInfo, Element, ExternalIdentifier, ExternalReference, IntegrityMethod, RelationshipCompleteness, RelationshipType
from beartype.typing import List, Optional
from dataclasses import field
from datetime import datetime
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class Relationship(Element):
    """
    A Relationship is a grouping of characteristics unique to an assertion that one Element is related to one or more
    other Elements in some way.
    """
    from_element: str
    """
    This field references the Element on the left-hand side of a relationship.
    """
    to: List[str] = field(default_factory=list)
    """
    This field references an Element on the right-hand side of a relationship.
    """
    relationship_type: RelationshipType
    """
    This field provides information about the relationship between two Elements. For example, you can represent a
    relationship between two different Files, between a Package and a File, between two Packages, or between one
    SPDXDocument and another SPDXDocument.
    """
    completeness: Optional[RelationshipCompleteness] = None
    """
    Completeness gives information about whether the provided relationships are complete, known to be incomplete or if
    no assertion is made either way.
    """
    start_time: Optional[datetime] = None
    """
    A startTime specifies the time from which element is applicable / valid.
    """
    end_time: Optional[datetime] = None
    """
    A endTime specifies the time from which element is no applicable / valid.
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
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        to = [] if to is None else to
        check_types_and_set_values(self, locals())
