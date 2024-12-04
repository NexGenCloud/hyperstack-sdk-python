# Userinfopostpayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address1** | **str** |  | [optional] 
**billing_address2** | **str** |  | [optional] 
**business** | **bool** |  | 
**company_name** | **str** |  | [optional] 
**country** | **str** |  | 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**zip_code** | **str** |  | 

## Example

```python
from hyperstack.models.userinfopostpayload import Userinfopostpayload

# TODO update the JSON string below
json = "{}"
# create an instance of Userinfopostpayload from a JSON string
userinfopostpayload_instance = Userinfopostpayload.from_json(json)
# print the JSON string representation of the object
print(Userinfopostpayload.to_json())

# convert the object into a dict
userinfopostpayload_dict = userinfopostpayload_instance.to_dict()
# create an instance of Userinfopostpayload from a dict
userinfopostpayload_from_dict = Userinfopostpayload.from_dict(userinfopostpayload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


