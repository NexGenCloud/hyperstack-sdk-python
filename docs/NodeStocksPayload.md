# NodeStocksPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_use** | **int** |  | 
**name** | **str** |  | [optional] 
**total** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from hyperstack.models.node_stocks_payload import NodeStocksPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStocksPayload from a JSON string
node_stocks_payload_instance = NodeStocksPayload.from_json(json)
# print the JSON string representation of the object
print(NodeStocksPayload.to_json())

# convert the object into a dict
node_stocks_payload_dict = node_stocks_payload_instance.to_dict()
# create an instance of NodeStocksPayload from a dict
node_stocks_payload_from_dict = NodeStocksPayload.from_dict(node_stocks_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


