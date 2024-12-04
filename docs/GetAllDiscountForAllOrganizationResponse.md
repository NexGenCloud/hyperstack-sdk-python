# GetAllDiscountForAllOrganizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_plans** | [**List[GetAllDiscountsFields]**](GetAllDiscountsFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_all_discount_for_all_organization_response import GetAllDiscountForAllOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllDiscountForAllOrganizationResponse from a JSON string
get_all_discount_for_all_organization_response_instance = GetAllDiscountForAllOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllDiscountForAllOrganizationResponse.to_json())

# convert the object into a dict
get_all_discount_for_all_organization_response_dict = get_all_discount_for_all_organization_response_instance.to_dict()
# create an instance of GetAllDiscountForAllOrganizationResponse from a dict
get_all_discount_for_all_organization_response_from_dict = GetAllDiscountForAllOrganizationResponse.from_dict(get_all_discount_for_all_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


