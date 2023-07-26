# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!

from abc import ABC
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties


@dataclass_with_properties
class PositiveIntegerRange(ABC):
    """
    PositiveIntegerRange is a tuple of two positive integers that define a range. "begin" must be less than or equal to
    "end".
    """
    begin: int
    """
    begin is a positive integer that defines the beginning of a range.
    """
    end: int
    """
    end is a positive integer that defines the end of a range.
    """

    def __init__(
        self,
        begin: int,
        end: int,
    ):
        check_types_and_set_values(self, locals())
