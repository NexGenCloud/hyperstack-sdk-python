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
from ..models.firewall_attachment_model import FirewallAttachmentModel
from ..models.firewall_environment_fields import FirewallEnvironmentFields
from ..models.security_group_rule_fields import SecurityGroupRuleFields
from typing import Optional, Set
from typing_extensions import Self

class FirewallDetailFields(BaseModel):
    """
    FirewallDetailFields
    """ # noqa: E501
    attachments: Optional[List[FirewallAttachmentModel]] = None
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    environment: Optional[FirewallEnvironmentFields] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    rules: Optional[List[SecurityGroupRuleFields]] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["attachments", "created_at", "description", "environment", "id", "name", "rules", "status"]

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
        """Create an instance of FirewallDetailFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item_rules in self.rules:
                if _item_rules:
                    _items.append(_item_rules.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FirewallDetailFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attachments": [FirewallAttachmentModel.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "environment": FirewallEnvironmentFields.from_dict(obj["environment"]) if obj.get("environment") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "rules": [SecurityGroupRuleFields.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "status": obj.get("status")
        })
        return _obj


