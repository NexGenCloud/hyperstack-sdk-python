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
from ..models.rbac_role_field import RbacRoleField
from typing import Optional, Set
from typing_extensions import Self

class OrganizationUserResponseModel(BaseModel):
    """
    OrganizationUserResponseModel
    """ # noqa: E501
    email: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    joined_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    name: Optional[StrictStr] = None
    rbac_roles: Optional[List[RbacRoleField]] = None
    role: Optional[StrictStr] = None
    sub: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["email", "id", "joined_at", "last_login", "name", "rbac_roles", "role", "sub", "username"]

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
        """Create an instance of OrganizationUserResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rbac_roles (list)
        _items = []
        if self.rbac_roles:
            for _item_rbac_roles in self.rbac_roles:
                if _item_rbac_roles:
                    _items.append(_item_rbac_roles.to_dict())
            _dict['rbac_roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationUserResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "id": obj.get("id"),
            "joined_at": obj.get("joined_at"),
            "last_login": obj.get("last_login"),
            "name": obj.get("name"),
            "rbac_roles": [RbacRoleField.from_dict(_item) for _item in obj["rbac_roles"]] if obj.get("rbac_roles") is not None else None,
            "role": obj.get("role"),
            "sub": obj.get("sub"),
            "username": obj.get("username")
        })
        return _obj


