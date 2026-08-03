# DeviceUserBindingRequest

PolicyBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **UUID** |  | [optional] 
**group** | **UUID** |  | [optional] 
**user** | **int** |  | [optional] 
**target** | **UUID** |  | 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 
**is_primary** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.device_user_binding_request import DeviceUserBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUserBindingRequest from a JSON string
device_user_binding_request_instance = DeviceUserBindingRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceUserBindingRequest.to_json())

# convert the object into a dict
device_user_binding_request_dict = device_user_binding_request_instance.to_dict()
# create an instance of DeviceUserBindingRequest from a dict
device_user_binding_request_from_dict = DeviceUserBindingRequest.from_dict(device_user_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


