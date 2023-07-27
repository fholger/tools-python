# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from ..core.creation_info import CreationInfo
from ..core.external_identifier import ExternalIdentifier
from ..core.external_reference import ExternalReference
from ..core.integrity_method import IntegrityMethod
from ..licensing.license import License


@dataclass_with_properties
class ListedLicense(License):
    """
    A ListedLicense represents a License that is listed on the SPDX License List at https://spdx.org/licenses.
    """

    list_version_added: Optional[str] = None
    """
    A listVersionAdded for a ListedLicense or ListedLicenseException on the SPDX License List specifies which version
    release of the License List was the first one in which it was included.
    """
    deprecated_version: Optional[str] = None
    """
    A deprecatedVersion for a ListedLicense or ListedLicenseException on the SPDX License List specifies which version
    release of the License List was the first one in which it was marked as deprecated.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        license_text: str,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
        is_osi_approved: Optional[bool] = None,
        is_fsf_libre: Optional[bool] = None,
        standard_license_header: Optional[str] = None,
        standard_license_template: Optional[str] = None,
        is_deprecated_license_id: Optional[bool] = None,
        obsoleted_by: Optional[str] = None,
        list_version_added: Optional[str] = None,
        deprecated_version: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        check_types_and_set_values(self, locals())
