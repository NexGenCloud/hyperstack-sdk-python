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

class PricebookResourceObjectResponse(BaseModel):
    """
    PricebookResourceObjectResponse
    """ # noqa: E501
    actual_price: Optional[Union[StrictFloat, StrictInt]] = None
    amount: Optional[StrictInt] = None
    discounted_rate: Optional[Union[StrictFloat, StrictInt]] = None
    host_original_price: Optional[Union[StrictFloat, StrictInt]] = None
    host_price: Optional[Union[StrictFloat, StrictInt]] = None
    name: Optional[StrictStr] = None
    nexgen_original_price: Optional[Union[StrictFloat, StrictInt]] = None
    nexgen_price: Optional[Union[StrictFloat, StrictInt]] = None
    price: Optional[Union[StrictFloat, StrictInt]] = None
    rate: Optional[Union[StrictFloat, StrictInt]] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["actual_price", "amount", "discounted_rate", "host_original_price", "host_price", "name", "nexgen_original_price", "nexgen_price", "price", "rate", "type"]

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
        """Create an instance of PricebookResourceObjectResponse from a JSON string"""
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
        """Create an instance of PricebookResourceObjectResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actual_price": obj.get("actual_price"),
            "amount": obj.get("amount"),
            "discounted_rate": obj.get("discounted_rate"),
            "host_original_price": obj.get("host_original_price"),
            "host_price": obj.get("host_price"),
            "name": obj.get("name"),
            "nexgen_original_price": obj.get("nexgen_original_price"),
            "nexgen_price": obj.get("nexgen_price"),
            "price": obj.get("price"),
            "rate": obj.get("rate"),
            "type": obj.get("type")
        })
        return _obj


