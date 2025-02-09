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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from ..models.graph_datetime_value_model import GraphDatetimeValueModel
from typing import Optional, Set
from typing_extensions import Self

class SubResourceGraphBillingDetailsMetrics(BaseModel):
    """
    SubResourceGraphBillingDetailsMetrics
    """ # noqa: E501
    cpu_incurred_bill: Optional[Union[StrictFloat, StrictInt]] = None
    cpu_incurred_bill_graph: Optional[List[GraphDatetimeValueModel]] = None
    disk_incurred_bill: Optional[Union[StrictFloat, StrictInt]] = None
    disk_incurred_bill_graph: Optional[List[GraphDatetimeValueModel]] = None
    ephemeral_incurred_bill: Optional[Union[StrictFloat, StrictInt]] = None
    ephemeral_incurred_bill_graph: Optional[List[GraphDatetimeValueModel]] = None
    gpu_incurred_bill: Optional[Union[StrictFloat, StrictInt]] = None
    gpu_incurred_bill_graph: Optional[List[GraphDatetimeValueModel]] = None
    publicip_incurred_bill: Optional[Union[StrictFloat, StrictInt]] = None
    publicip_incurred_bill_graph: Optional[List[GraphDatetimeValueModel]] = None
    ram_incurred_bill: Optional[Union[StrictFloat, StrictInt]] = None
    ram_incurred_bill_graph: Optional[List[GraphDatetimeValueModel]] = None
    __properties: ClassVar[List[str]] = ["cpu_incurred_bill", "cpu_incurred_bill_graph", "disk_incurred_bill", "disk_incurred_bill_graph", "ephemeral_incurred_bill", "ephemeral_incurred_bill_graph", "gpu_incurred_bill", "gpu_incurred_bill_graph", "publicip_incurred_bill", "publicip_incurred_bill_graph", "ram_incurred_bill", "ram_incurred_bill_graph"]

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
        """Create an instance of SubResourceGraphBillingDetailsMetrics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cpu_incurred_bill_graph (list)
        _items = []
        if self.cpu_incurred_bill_graph:
            for _item_cpu_incurred_bill_graph in self.cpu_incurred_bill_graph:
                if _item_cpu_incurred_bill_graph:
                    _items.append(_item_cpu_incurred_bill_graph.to_dict())
            _dict['cpu_incurred_bill_graph'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in disk_incurred_bill_graph (list)
        _items = []
        if self.disk_incurred_bill_graph:
            for _item_disk_incurred_bill_graph in self.disk_incurred_bill_graph:
                if _item_disk_incurred_bill_graph:
                    _items.append(_item_disk_incurred_bill_graph.to_dict())
            _dict['disk_incurred_bill_graph'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ephemeral_incurred_bill_graph (list)
        _items = []
        if self.ephemeral_incurred_bill_graph:
            for _item_ephemeral_incurred_bill_graph in self.ephemeral_incurred_bill_graph:
                if _item_ephemeral_incurred_bill_graph:
                    _items.append(_item_ephemeral_incurred_bill_graph.to_dict())
            _dict['ephemeral_incurred_bill_graph'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in gpu_incurred_bill_graph (list)
        _items = []
        if self.gpu_incurred_bill_graph:
            for _item_gpu_incurred_bill_graph in self.gpu_incurred_bill_graph:
                if _item_gpu_incurred_bill_graph:
                    _items.append(_item_gpu_incurred_bill_graph.to_dict())
            _dict['gpu_incurred_bill_graph'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in publicip_incurred_bill_graph (list)
        _items = []
        if self.publicip_incurred_bill_graph:
            for _item_publicip_incurred_bill_graph in self.publicip_incurred_bill_graph:
                if _item_publicip_incurred_bill_graph:
                    _items.append(_item_publicip_incurred_bill_graph.to_dict())
            _dict['publicip_incurred_bill_graph'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ram_incurred_bill_graph (list)
        _items = []
        if self.ram_incurred_bill_graph:
            for _item_ram_incurred_bill_graph in self.ram_incurred_bill_graph:
                if _item_ram_incurred_bill_graph:
                    _items.append(_item_ram_incurred_bill_graph.to_dict())
            _dict['ram_incurred_bill_graph'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubResourceGraphBillingDetailsMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpu_incurred_bill": obj.get("cpu_incurred_bill"),
            "cpu_incurred_bill_graph": [GraphDatetimeValueModel.from_dict(_item) for _item in obj["cpu_incurred_bill_graph"]] if obj.get("cpu_incurred_bill_graph") is not None else None,
            "disk_incurred_bill": obj.get("disk_incurred_bill"),
            "disk_incurred_bill_graph": [GraphDatetimeValueModel.from_dict(_item) for _item in obj["disk_incurred_bill_graph"]] if obj.get("disk_incurred_bill_graph") is not None else None,
            "ephemeral_incurred_bill": obj.get("ephemeral_incurred_bill"),
            "ephemeral_incurred_bill_graph": [GraphDatetimeValueModel.from_dict(_item) for _item in obj["ephemeral_incurred_bill_graph"]] if obj.get("ephemeral_incurred_bill_graph") is not None else None,
            "gpu_incurred_bill": obj.get("gpu_incurred_bill"),
            "gpu_incurred_bill_graph": [GraphDatetimeValueModel.from_dict(_item) for _item in obj["gpu_incurred_bill_graph"]] if obj.get("gpu_incurred_bill_graph") is not None else None,
            "publicip_incurred_bill": obj.get("publicip_incurred_bill"),
            "publicip_incurred_bill_graph": [GraphDatetimeValueModel.from_dict(_item) for _item in obj["publicip_incurred_bill_graph"]] if obj.get("publicip_incurred_bill_graph") is not None else None,
            "ram_incurred_bill": obj.get("ram_incurred_bill"),
            "ram_incurred_bill_graph": [GraphDatetimeValueModel.from_dict(_item) for _item in obj["ram_incurred_bill_graph"]] if obj.get("ram_incurred_bill_graph") is not None else None
        })
        return _obj


