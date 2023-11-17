# SPDX-License-Identifier: Apache-2.0
#
# This file was auto-generated by dev/gen_python_model_from_spec.py
# Do not manually edit!
# flake8: noqa

from enum import Enum, auto

from beartype.typing import Optional


class DatasetType(Enum):
    """
    Describes the different structures of data within a given dataset. A dataset can have multiple types of data, or
    even a single type of data but still match multiple types, for example sensor data could also be timeseries or
    labeled image data could also be considered categorical.
    """

    STRUCTURED = auto()
    """
    data is stored in tabular format or retrieved from a relational database.
    """
    NUMERIC = auto()
    """
    data consists only of numeric entries.
    """
    TEXT = auto()
    """
    data consists of unstructured text, such as a book, wikipedia article (without images), or transcript.
    """
    CATEGORICAL = auto()
    """
    data that is classified into a discrete number of categories, such as the eye color of a population of people.
    """
    GRAPH = auto()
    """
    data is in the form of a graph where entries are somehow related to each other through edges, such a social network
    of friends.
    """
    TIMESERIES = auto()
    """
    data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a
    day.
    """
    TIMESTAMP = auto()
    """
    data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as
    when a taxi ride starts and ends.
    """
    SENSOR = auto()
    """
    data is recorded from a physical sensor, such as a thermometer reading or biometric device.
    """
    IMAGE = auto()
    """
    data is a collection of images such as pictures of animals.
    """
    SYNTACTIC = auto()
    """
    data describes the syntax or semantics of a language or text, such as a parse tree used for natural language
    processing.
    """
    AUDIO = auto()
    """
    data is audio based, such as a collection of music from the 80s.
    """
    VIDEO = auto()
    """
    data is video based, such as a collection of movie clips featuring Tom Hanks.
    """
    OTHER = auto()
    """
    data is of a type not included in this list.
    """
    NO_ASSERTION = auto()
    """
    data type is not known.
    """

    def __str__(self) -> str:
        if self == DatasetType.STRUCTURED:
            return "structured"
        if self == DatasetType.NUMERIC:
            return "numeric"
        if self == DatasetType.TEXT:
            return "text"
        if self == DatasetType.CATEGORICAL:
            return "categorical"
        if self == DatasetType.GRAPH:
            return "graph"
        if self == DatasetType.TIMESERIES:
            return "timeseries"
        if self == DatasetType.TIMESTAMP:
            return "timestamp"
        if self == DatasetType.SENSOR:
            return "sensor"
        if self == DatasetType.IMAGE:
            return "image"
        if self == DatasetType.SYNTACTIC:
            return "syntactic"
        if self == DatasetType.AUDIO:
            return "audio"
        if self == DatasetType.VIDEO:
            return "video"
        if self == DatasetType.OTHER:
            return "other"
        if self == DatasetType.NO_ASSERTION:
            return "noAssertion"
        return "unknown"

    @staticmethod
    def from_str(value: str) -> Optional["DatasetType"]:
        if value == "structured":
            return DatasetType.STRUCTURED
        if value == "numeric":
            return DatasetType.NUMERIC
        if value == "text":
            return DatasetType.TEXT
        if value == "categorical":
            return DatasetType.CATEGORICAL
        if value == "graph":
            return DatasetType.GRAPH
        if value == "timeseries":
            return DatasetType.TIMESERIES
        if value == "timestamp":
            return DatasetType.TIMESTAMP
        if value == "sensor":
            return DatasetType.SENSOR
        if value == "image":
            return DatasetType.IMAGE
        if value == "syntactic":
            return DatasetType.SYNTACTIC
        if value == "audio":
            return DatasetType.AUDIO
        if value == "video":
            return DatasetType.VIDEO
        if value == "other":
            return DatasetType.OTHER
        if value == "noAssertion":
            return DatasetType.NO_ASSERTION
        return None