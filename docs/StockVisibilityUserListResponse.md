# StockVisibilityUserListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**users** | [**List[SingleVisibilityUserResponse]**](SingleVisibilityUserResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.stock_visibility_user_list_response import StockVisibilityUserListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StockVisibilityUserListResponse from a JSON string
stock_visibility_user_list_response_instance = StockVisibilityUserListResponse.from_json(json)
# print the JSON string representation of the object
print(StockVisibilityUserListResponse.to_json())

# convert the object into a dict
stock_visibility_user_list_response_dict = stock_visibility_user_list_response_instance.to_dict()
# create an instance of StockVisibilityUserListResponse from a dict
stock_visibility_user_list_response_from_dict = StockVisibilityUserListResponse.from_dict(stock_visibility_user_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


