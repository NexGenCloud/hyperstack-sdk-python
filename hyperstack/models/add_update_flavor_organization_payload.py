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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AddUpdateFlavorOrganizationPayload(BaseModel):
    """
    AddUpdateFlavorOrganizationPayload
    """ # noqa: E501
    cpu: StrictInt
    description: Optional[StrictStr] = None
    disk: StrictInt
    ephemeral: Optional[StrictInt] = None
    gpu_count: StrictInt
    gpu_id: StrictInt
    is_public: StrictBool
    labels: Optional[List[StrictStr]] = None
    name: StrictStr
    openstack_id: StrictStr
    organizations: List[StrictInt]
    ram: Union[StrictFloat, StrictInt]
    region_id: StrictInt
    __properties: ClassVar[List[str]] = ["cpu", "description", "disk", "ephemeral", "gpu_count", "gpu_id", "is_public", "labels", "name", "openstack_id", "organizations", "ram", "region_id"]

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
        """Create an instance of AddUpdateFlavorOrganizationPayload from a JSON string"""
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
        """Create an instance of AddUpdateFlavorOrganizationPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpu": obj.get("cpu"),
            "description": obj.get("description"),
            "disk": obj.get("disk"),
            "ephemeral": obj.get("ephemeral"),
            "gpu_count": obj.get("gpu_count"),
            "gpu_id": obj.get("gpu_id"),
            "is_public": obj.get("is_public"),
            "labels": obj.get("labels"),
            "name": obj.get("name"),
            "openstack_id": obj.get("openstack_id"),
            "organizations": obj.get("organizations"),
            "ram": obj.get("ram"),
            "region_id": obj.get("region_id")
        })
        return _obj

