# DeviceUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**home** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.device_user_request import DeviceUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUserRequest from a JSON string
device_user_request_instance = DeviceUserRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceUserRequest.to_json())

# convert the object into a dict
device_user_request_dict = device_user_request_instance.to_dict()
# create an instance of DeviceUserRequest from a dict
device_user_request_from_dict = DeviceUserRequest.from_dict(device_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


