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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ..models.node_stocks_payload import NodeStocksPayload
from ..models.power_usage_model import PowerUsageModel
from typing import Optional, Set
from typing_extensions import Self

class NodePowerUsageModel(BaseModel):
    """
    NodePowerUsageModel
    """ # noqa: E501
    flavors: Optional[List[StrictStr]] = None
    nexgen_name: Optional[StrictStr] = None
    openstack_id: StrictStr
    openstack_name: Optional[StrictStr] = None
    organizations: Optional[List[StrictInt]] = None
    power_usages: Optional[PowerUsageModel] = None
    projects: Optional[List[StrictStr]] = None
    provision_date: Optional[datetime] = None
    status: Optional[StrictStr] = None
    stocks: Optional[List[NodeStocksPayload]] = None
    sunset_date: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["flavors", "nexgen_name", "openstack_id", "openstack_name", "organizations", "power_usages", "projects", "provision_date", "status", "stocks", "sunset_date"]

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
        """Create an instance of NodePowerUsageModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of power_usages
        if self.power_usages:
            _dict['power_usages'] = self.power_usages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stocks (list)
        _items = []
        if self.stocks:
            for _item_stocks in self.stocks:
                if _item_stocks:
                    _items.append(_item_stocks.to_dict())
            _dict['stocks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodePowerUsageModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "flavors": obj.get("flavors"),
            "nexgen_name": obj.get("nexgen_name"),
            "openstack_id": obj.get("openstack_id"),
            "openstack_name": obj.get("openstack_name"),
            "organizations": obj.get("organizations"),
            "power_usages": PowerUsageModel.from_dict(obj["power_usages"]) if obj.get("power_usages") is not None else None,
            "projects": obj.get("projects"),
            "provision_date": obj.get("provision_date"),
            "status": obj.get("status"),
            "stocks": [NodeStocksPayload.from_dict(_item) for _item in obj["stocks"]] if obj.get("stocks") is not None else None,
            "sunset_date": obj.get("sunset_date")
        })
        return _obj


