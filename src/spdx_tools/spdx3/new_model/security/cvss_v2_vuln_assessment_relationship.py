# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..core import Agent, CreationInfo, Element, ExternalIdentifier, ExternalReference, IntegrityMethod, RelationshipCompleteness, RelationshipType
from ..security import VulnAssessmentRelationship
from beartype.typing import List, Optional
from datetime import datetime
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class CvssV2VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    A CvssV2VulnAssessmentRelationship relationship describes the determined score and vector of a vulnerability using
    version 2.0 of the Common Vulnerability Scoring System (CVSS) as defined on
    [https://www.first.org/cvss/v2/guide](https://www.first.org/cvss/v2/guide). It is intented to communicate the
    results of using a CVSS calculator.

    **Constraints**

    - The value of severity must be one of 'low', 'medium' or 'high'
    - The relationship type must be set to hasAssessmentFor.

    **Syntax**

    ```json
    {
      "@type": "CvssV2VulnAssessmentRelationship",
      "@id": "urn:spdx.dev:cvssv2-cve-2020-28498",
      "relationshipType": "hasAssessmentFor",
      "score": 4.3,
      "vector": "(AV:N/AC:M/Au:N/C:P/I:N/A:N)",
      "severity": "low",
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": ["urn:product-acme-application-1.3"],
      "assessedElement": "urn:npm-elliptic-6.5.2",
      "externalReferences": [
        {
          "@type": "ExternalReference",
          "externalReferenceType": "securityAdvisory",
          "locator": "https://nvd.nist.gov/vuln/detail/CVE-2020-28498"
        },
        {
          "@type": "ExternalReference",
          "externalReferenceType": "securityAdvisory",
          "locator": "https://snyk.io/vuln/SNYK-JS-ELLIPTIC-1064899"
        },
        {
          "@type": "ExternalReference",
          "externalReferenceType": "securityFix",
          "locator": "https://github.com/indutny/elliptic/commit/441b742"
        }
      ],
      "suppliedBy": ["urn:spdx.dev:agent-my-security-vendor"],
      "publishedTime": "2023-05-06T10:06:13Z"
    },
    {
      "@type": "Relationship",
      "@id": "urn:spdx.dev:vulnAgentRel-1",  
      "relationshipType": "publishedBy",  
      "from": "urn:spdx.dev:cvssv2-cve-2020-28498",
      "to": ["urn:spdx.dev:agent-snyk"],
      "startTime": "2021-03-08T16:06:50Z"
    }
    ```
    """
    score: float
    """
    The score provides information on the severity of a vulnerability per the Common Vulnerability Scoring System as
    defined on [https://www.first.org/cvss](https://www.first.org/cvss/).
    """
    severity: Optional[str] = None
    """
    The severity field provides a human readable string, a label that can be used as an English adjective that qualifies
    its numerical score.
    """
    vector: Optional[str] = None
    """
    Sepcifies the vector string of a vulnerability, a string combining metrics from an assessment of its severity.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        from_element: str,
        to: List[str],
        relationship_type: RelationshipType,
        score: float,
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
        vector: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        check_types_and_set_values(self, locals())
