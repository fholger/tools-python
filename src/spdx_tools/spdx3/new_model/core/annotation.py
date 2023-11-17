# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from dataclasses import field

from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from ..core.annotation_type import AnnotationType
from ..core.creation_info import CreationInfo
from ..core.element import Element
from ..core.external_identifier import ExternalIdentifier
from ..core.external_reference import ExternalReference
from ..core.integrity_method import IntegrityMethod


@dataclass_with_properties
class Annotation(Element):
    """
    An Annotation is an assertion made in relation to one or more elements.
    """

    annotation_type: AnnotationType = None
    """
    An annotationType describes the type of an annotation.
    """
    content_type: List[str] = field(default_factory=list)
    """
    ContentType specifies the media type of an Element.
    """
    statement: Optional[str] = None
    """
    A statement is a commentary on an assertion that an annotator has made.
    """
    subject: str = None
    """
    A subject is an Element an annotator has made an assertion about.
    """

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        annotation_type: AnnotationType,
        subject: str,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_reference: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: List[str] = None,
        content_type: List[str] = None,
        statement: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_reference = [] if external_reference is None else external_reference
        external_identifier = [] if external_identifier is None else external_identifier
        extension = [] if extension is None else extension
        content_type = [] if content_type is None else content_type
        check_types_and_set_values(self, locals())