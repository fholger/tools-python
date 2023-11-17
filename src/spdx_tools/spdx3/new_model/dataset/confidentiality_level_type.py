# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from enum import Enum, auto

from beartype.typing import Optional


class ConfidentialityLevelType(Enum):
    """
    Describes the different confidentiality levels as given by the [Traffic Light
    Protocol](https://en.wikipedia.org/wiki/Traffic_Light_Protocol).
    """

    RED = auto()
    """
    Data points in the dataset are highly confidential and can only be shared with named recipients.
    """
    AMBER = auto()
    """
    Data points in the dataset can be shared only with specific organizations and their clients on a need to know
    basis.
    """
    GREEN = auto()
    """
    Dataset can be shared within a community of peers and partners.
    """
    CLEAR = auto()
    """
    Dataset may be distributed freely, without restriction.
    """

    def __str__(self) -> str:
        if self == ConfidentialityLevelType.RED:
            return "Red"
        if self == ConfidentialityLevelType.AMBER:
            return "Amber"
        if self == ConfidentialityLevelType.GREEN:
            return "Green"
        if self == ConfidentialityLevelType.CLEAR:
            return "Clear"
        return "unknown"

    @staticmethod
    def from_str(value: str) -> Optional["ConfidentialityLevelType"]:
        if value == "Red":
            return ConfidentialityLevelType.RED
        if value == "Amber":
            return ConfidentialityLevelType.AMBER
        if value == "Green":
            return ConfidentialityLevelType.GREEN
        if value == "Clear":
            return ConfidentialityLevelType.CLEAR
        return None