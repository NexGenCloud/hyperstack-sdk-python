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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ..models.organization_level_billing_history_response_attributes import OrganizationLevelBillingHistoryResponseAttributes
from ..models.organization_level_billing_history_response_metrics import OrganizationLevelBillingHistoryResponseMetrics
from typing import Optional, Set
from typing_extensions import Self

class OrganizationLevelBillingHistoryResources(BaseModel):
    """
    OrganizationLevelBillingHistoryResources
    """ # noqa: E501
    attributes: Optional[OrganizationLevelBillingHistoryResponseAttributes] = None
    metrics: Optional[OrganizationLevelBillingHistoryResponseMetrics] = None
    __properties: ClassVar[List[str]] = ["attributes", "metrics"]

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
        """Create an instance of OrganizationLevelBillingHistoryResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metrics
        if self.metrics:
            _dict['metrics'] = self.metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationLevelBillingHistoryResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributes": OrganizationLevelBillingHistoryResponseAttributes.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None,
            "metrics": OrganizationLevelBillingHistoryResponseMetrics.from_dict(obj["metrics"]) if obj.get("metrics") is not None else None
        })
        return _obj


