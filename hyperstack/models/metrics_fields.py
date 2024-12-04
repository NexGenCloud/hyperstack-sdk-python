# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ..models.metric_item_fields import MetricItemFields
from typing import Optional, Set
from typing_extensions import Self

class MetricsFields(BaseModel):
    """
    MetricsFields
    """ # noqa: E501
    cpu: Optional[MetricItemFields] = None
    disk_read: Optional[MetricItemFields] = Field(default=None, alias="disk.read")
    disk_write: Optional[MetricItemFields] = Field(default=None, alias="disk.write")
    memory_usages: Optional[MetricItemFields] = Field(default=None, alias="memory.usages")
    network_in: Optional[MetricItemFields] = Field(default=None, alias="network.in")
    network_out: Optional[MetricItemFields] = Field(default=None, alias="network.out")
    __properties: ClassVar[List[str]] = ["cpu", "disk.read", "disk.write", "memory.usages", "network.in", "network.out"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MetricsFields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict['cpu'] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disk_read
        if self.disk_read:
            _dict['disk.read'] = self.disk_read.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disk_write
        if self.disk_write:
            _dict['disk.write'] = self.disk_write.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory_usages
        if self.memory_usages:
            _dict['memory.usages'] = self.memory_usages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_in
        if self.network_in:
            _dict['network.in'] = self.network_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_out
        if self.network_out:
            _dict['network.out'] = self.network_out.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetricsFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpu": MetricItemFields.from_dict(obj["cpu"]) if obj.get("cpu") is not None else None,
            "disk.read": MetricItemFields.from_dict(obj["disk.read"]) if obj.get("disk.read") is not None else None,
            "disk.write": MetricItemFields.from_dict(obj["disk.write"]) if obj.get("disk.write") is not None else None,
            "memory.usages": MetricItemFields.from_dict(obj["memory.usages"]) if obj.get("memory.usages") is not None else None,
            "network.in": MetricItemFields.from_dict(obj["network.in"]) if obj.get("network.in") is not None else None,
            "network.out": MetricItemFields.from_dict(obj["network.out"]) if obj.get("network.out") is not None else None
        })
        return _obj


