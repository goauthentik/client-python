# PatchedDeviceAccessGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_device_access_group_request import PatchedDeviceAccessGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDeviceAccessGroupRequest from a JSON string
patched_device_access_group_request_instance = PatchedDeviceAccessGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDeviceAccessGroupRequest.to_json())

# convert the object into a dict
patched_device_access_group_request_dict = patched_device_access_group_request_instance.to_dict()
# create an instance of PatchedDeviceAccessGroupRequest from a dict
patched_device_access_group_request_from_dict = PatchedDeviceAccessGroupRequest.from_dict(patched_device_access_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


