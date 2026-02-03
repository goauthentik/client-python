# DeviceGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.device_group_request import DeviceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGroupRequest from a JSON string
device_group_request_instance = DeviceGroupRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceGroupRequest.to_json())

# convert the object into a dict
device_group_request_dict = device_group_request_instance.to_dict()
# create an instance of DeviceGroupRequest from a dict
device_group_request_from_dict = DeviceGroupRequest.from_dict(device_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


