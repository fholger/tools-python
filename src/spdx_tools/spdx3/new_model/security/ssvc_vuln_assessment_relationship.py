# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..core import Agent, CreationInfo, Element, ExternalIdentifier, ExternalReference, IntegrityMethod, RelationshipCompleteness, RelationshipType
from ..security import SsvcDecisionType, VulnAssessmentRelationship
from beartype.typing import List, Optional
from datetime import datetime
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class SsvcVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    An SsvcVulnAssessmentRelationship describes the decision made using the Stakeholder-Specific Vulnerability
    Categorization (SSVC) decision tree as defined on
    [https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).
    It is intended to communicate the results of using the CISA SSVC Calculator.

    **Constraints**

    - The relationship type must be set to hasAssessmentFor.

    **Syntax**

    ```json
    {
      "@type": "SsvcVulnAssessmentRelationship",
      "@id": "urn:spdx.dev:ssvc-1",
      "relationshipType": "hasAssessmentFor",
      "decisionType": "act",
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": ["urn:product-acme-application-1.3"],
      "assessedElement": "urn:npm-elliptic-6.5.2",
      "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
      "publishedTime": "2021-03-09T11:04:53Z"
    }
    ```
    """
    decision_type: SsvcDecisionType
    """
    A decisionType is a mandatory value and must select one of the four entries in the `SsvcDecisionType.md` vocabulary.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        from_element: str,
        to: List[str],
        relationship_type: RelationshipType,
        decision_type: SsvcDecisionType,
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
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        check_types_and_set_values(self, locals())
