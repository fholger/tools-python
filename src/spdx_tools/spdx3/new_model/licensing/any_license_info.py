# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from abc import abstractmethod

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties

from ..core.element import Element


@dataclass_with_properties
class AnyLicenseInfo(Element):
    """
    An AnyLicenseInfo is used by licensing properties of software artifacts. It can be a NoneLicense, a
    NoAssertionLicense, single license (either on the SPDX License List or a custom-defined license); a single license
    with an "or later" operator applied; the foregoing with additional text applied; or a set of licenses combined by
    applying "AND" and "OR" operators recursively.
    """

    @abstractmethod
    def __init__(self):
        pass
