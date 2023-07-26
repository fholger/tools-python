# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from ..licensing import ExtendableLicense, License
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class OrLaterOperator(ExtendableLicense):
    """
    An OrLaterOperator indicates that this portion of the AnyLicenseInfo represents either (1) the specified version of
    the corresponding License, or (2) any later version of that License. It is represented in the SPDX License
    Expression Syntax by the `+` operator.

    It is context-dependent, and unspecified by SPDX, as to what constitutes a "later version" of any particular
    License. Some Licenses may not be versioned, or may not have clearly-defined ordering for versions. The consumer of
    SPDX data will need to determine for themselves what meaning to attribute to a "later version" operator for a
    particular License.
    """
    subject_license: License

    def __init__(
        self,
        subject_license: License,
    ):
        check_types_and_set_values(self, locals())
