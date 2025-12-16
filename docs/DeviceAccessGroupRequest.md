# DeviceAccessGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from authentik_client.models.device_access_group_request import DeviceAccessGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAccessGroupRequest from a JSON string
device_access_group_request_instance = DeviceAccessGroupRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceAccessGroupRequest.to_json())

# convert the object into a dict
device_access_group_request_dict = device_access_group_request_instance.to_dict()
# create an instance of DeviceAccessGroupRequest from a dict
device_access_group_request_from_dict = DeviceAccessGroupRequest.from_dict(device_access_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


