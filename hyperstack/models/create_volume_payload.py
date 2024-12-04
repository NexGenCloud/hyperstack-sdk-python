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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateVolumePayload(BaseModel):
    """
    CreateVolumePayload
    """ # noqa: E501
    callback_url: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="A URL that can be attached to the volume you are creating. This `callback_url` will post any action events that occur to your volume to the provided URL.")
    description: Optional[StrictStr] = Field(default=None, description="A brief description or comment about the volume.")
    environment_name: StrictStr = Field(description="The name of the [environment](https://infrahub-doc.nexgencloud.com/docs/features/environments-available-features) within which the volume is being created.")
    image_id: Optional[StrictInt] = Field(default=None, description="The ID of the operating system image that will be associated with the volume. By providing an `image_id` in the create volume request, you will create a bootable volume.")
    name: Annotated[str, Field(strict=True, max_length=50)] = Field(description="The name of the volume being created.")
    size: StrictInt = Field(description="The size of the volume in GB. 1048576GB storage capacity per volume.")
    volume_type: StrictStr = Field(description="Specifies the type of volume being created, which determines the storage technology it will use. Call the [List volume types](https://infrahub-api-doc.nexgencloud.com/#get-/core/volumes) endpoint to retrieve a list of available volume model types.")
    __properties: ClassVar[List[str]] = ["callback_url", "description", "environment_name", "image_id", "name", "size", "volume_type"]

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
        """Create an instance of CreateVolumePayload from a JSON string"""
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
        """Create an instance of CreateVolumePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "callback_url": obj.get("callback_url"),
            "description": obj.get("description"),
            "environment_name": obj.get("environment_name"),
            "image_id": obj.get("image_id"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "volume_type": obj.get("volume_type")
        })
        return _obj


