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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ..models.contract_eligible_instance_fields import ContractEligibleInstanceFields
from typing import Optional, Set
from typing_extensions import Self

class ContractEligibleInstancesResponse(BaseModel):
    """
    ContractEligibleInstancesResponse
    """ # noqa: E501
    instance_count: Optional[StrictInt] = None
    instances: Optional[List[ContractEligibleInstanceFields]] = None
    message: Optional[StrictStr] = None
    status: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["instance_count", "instances", "message", "status"]

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
        """Create an instance of ContractEligibleInstancesResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in instances (list)
        _items = []
        if self.instances:
            for _item_instances in self.instances:
                if _item_instances:
                    _items.append(_item_instances.to_dict())
            _dict['instances'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractEligibleInstancesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "instance_count": obj.get("instance_count"),
            "instances": [ContractEligibleInstanceFields.from_dict(_item) for _item in obj["instances"]] if obj.get("instances") is not None else None,
            "message": obj.get("message"),
            "status": obj.get("status")
        })
        return _obj

