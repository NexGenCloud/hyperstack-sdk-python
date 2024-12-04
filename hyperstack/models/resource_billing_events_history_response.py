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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ..models.resource_billing_events_history_metrics import ResourceBillingEventsHistoryMetrics
from typing import Optional, Set
from typing_extensions import Self

class ResourceBillingEventsHistoryResponse(BaseModel):
    """
    ResourceBillingEventsHistoryResponse
    """ # noqa: E501
    billing_events_history: Optional[List[ResourceBillingEventsHistoryMetrics]] = None
    message: Optional[StrictStr] = None
    status: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["billing_events_history", "message", "status"]

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
        """Create an instance of ResourceBillingEventsHistoryResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in billing_events_history (list)
        _items = []
        if self.billing_events_history:
            for _item_billing_events_history in self.billing_events_history:
                if _item_billing_events_history:
                    _items.append(_item_billing_events_history.to_dict())
            _dict['billing_events_history'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceBillingEventsHistoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billing_events_history": [ResourceBillingEventsHistoryMetrics.from_dict(_item) for _item in obj["billing_events_history"]] if obj.get("billing_events_history") is not None else None,
            "message": obj.get("message"),
            "status": obj.get("status")
        })
        return _obj


