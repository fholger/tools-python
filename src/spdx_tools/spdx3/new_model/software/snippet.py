# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..core import Agent, CreationInfo, ExternalIdentifier, ExternalReference, IntegrityMethod, PositiveIntegerRange
from ..licensing import AnyLicenseInfo
from ..software import SoftwareArtifact, SoftwarePurpose
from beartype.typing import List, Optional
from datetime import datetime
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class Snippet(SoftwareArtifact):
    """
    A Snippet describes a certain part of a file and can be used when the file is known to have some content that has
    been included from another original source. Snippets are useful for denoting when part of a file may have been
    originally created under another license or copied from a place with a known vulnerability.
    """
    byte_range: Optional[PositiveIntegerRange] = None
    """
    This field defines the byte range in the original host file that the snippet information applies to. A range of
    bytes is independent of various formatting concerns, and the most accurate way of referring to the differences. The
    choice was made to start the numbering of the byte range at 1 to be consistent with the W3C pointer method
    vocabulary.
    """
    line_range: Optional[PositiveIntegerRange] = None
    """
    This field defines the line range in the original host file that the snippet information applies to. If there is a
    disagreement between the byte range and line range, the byte range values will take precedence. A range of lines is
    a convenient reference for those files where there is a known line delimiter. The choice was made to start the
    numbering of the lines at 1 to be consistent with the W3C pointer method vocabulary.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
        originated_by: List[str] = None,
        supplied_by: List[str] = None,
        built_time: Optional[datetime] = None,
        release_time: Optional[datetime] = None,
        valid_until_time: Optional[datetime] = None,
        standard: List[str] = None,
        content_identifier: Optional[str] = None,
        primary_purpose: Optional[SoftwarePurpose] = None,
        additional_purpose: List[SoftwarePurpose] = None,
        concluded_license: Optional[AnyLicenseInfo] = None,
        declared_license: Optional[AnyLicenseInfo] = None,
        copyright_text: Optional[str] = None,
        attribution_text: Optional[str] = None,
        byte_range: Optional[PositiveIntegerRange] = None,
        line_range: Optional[PositiveIntegerRange] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        originated_by = [] if originated_by is None else originated_by
        supplied_by = [] if supplied_by is None else supplied_by
        standard = [] if standard is None else standard
        additional_purpose = [] if additional_purpose is None else additional_purpose
        check_types_and_set_values(self, locals())
