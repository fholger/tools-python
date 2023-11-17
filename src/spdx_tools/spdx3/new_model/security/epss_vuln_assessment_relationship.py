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
from ..core.relationship_completeness import RelationshipCompleteness
from ..core.relationship_type import RelationshipType
from ..security.vuln_assessment_relationship import VulnAssessmentRelationship


@dataclass_with_properties
class EpssVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    An EpssVulnAssessmentRelationship relationship describes the likelihood or probability that a vulnerability will be
    exploited in the wild using the Exploit Prediction Scoring System (EPSS) as defined on
    [https://www.first.org/epss/model](https://www.first.org/epss/model).

    **Constraints**

    - The relationship type must be set to hasAssessmentFor.

    **Syntax**

    ```json
    {
      "@type": "EpssVulnAssessmentRelationship",
      "@id": "urn:spdx.dev:epss-1",
      "relationshipType": "hasAssessmentFor",
      "probability": 80,
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": ["urn:product-acme-application-1.3"],
      "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
      "publishedTime": "2021-03-09T11:04:53Z"
    }
    ```
    """

    probability: int = None
    """
    The probability score between 0 and 1 (0 and 100%) estimating the likelihood that a vulnerability will be exploited
    in the next 12 months.
    """
    severity: Optional[str] = None
    """
    The severity field provides a human readable string, a label that can be used as an English adjective that
    qualifies its numerical score.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        from_element: str,
        to: List[str],
        relationship_type: RelationshipType,
        probability: int,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
        completeness: Optional[RelationshipCompleteness] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        assessed_element: Optional[str] = None,
        published_time: Optional[datetime] = None,
        supplied_by: Optional[str] = None,
        modified_time: Optional[datetime] = None,
        withdrawn_time: Optional[datetime] = None,
        severity: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        check_types_and_set_values(self, locals())