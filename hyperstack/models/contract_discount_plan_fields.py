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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ContractDiscountPlanFields(BaseModel):
    """
    ContractDiscountPlanFields
    """ # noqa: E501
    discount_amount: Optional[Union[StrictFloat, StrictInt]] = None
    discount_code: Optional[StrictStr] = None
    discount_percent: Optional[Union[StrictFloat, StrictInt]] = None
    discount_status: Optional[StrictStr] = None
    discount_type: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    resource_count: Optional[StrictInt] = None
    resource_id: Optional[StrictInt] = None
    resource_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["discount_amount", "discount_code", "discount_percent", "discount_status", "discount_type", "id", "resource_count", "resource_id", "resource_name"]

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
        """Create an instance of ContractDiscountPlanFields from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractDiscountPlanFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "discount_amount": obj.get("discount_amount"),
            "discount_code": obj.get("discount_code"),
            "discount_percent": obj.get("discount_percent"),
            "discount_status": obj.get("discount_status"),
            "discount_type": obj.get("discount_type"),
            "id": obj.get("id"),
            "resource_count": obj.get("resource_count"),
            "resource_id": obj.get("resource_id"),
            "resource_name": obj.get("resource_name")
        })
        return _obj


