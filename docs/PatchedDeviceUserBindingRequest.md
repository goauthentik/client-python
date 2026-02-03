# PatchedDeviceUserBindingRequest

PolicyBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **UUID** |  | [optional] 
**group** | **UUID** |  | [optional] 
**user** | **int** |  | [optional] 
**target** | **UUID** |  | [optional] 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 
**is_primary** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.patched_device_user_binding_request import PatchedDeviceUserBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDeviceUserBindingRequest from a JSON string
patched_device_user_binding_request_instance = PatchedDeviceUserBindingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDeviceUserBindingRequest.to_json())

# convert the object into a dict
patched_device_user_binding_request_dict = patched_device_user_binding_request_instance.to_dict()
# create an instance of PatchedDeviceUserBindingRequest from a dict
patched_device_user_binding_request_from_dict = PatchedDeviceUserBindingRequest.from_dict(patched_device_user_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


