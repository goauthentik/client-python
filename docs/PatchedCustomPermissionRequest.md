# PatchedCustomPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codename** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**model** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_custom_permission_request import PatchedCustomPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCustomPermissionRequest from a JSON string
patched_custom_permission_request_instance = PatchedCustomPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedCustomPermissionRequest.to_json())

# convert the object into a dict
patched_custom_permission_request_dict = patched_custom_permission_request_instance.to_dict()
# create an instance of PatchedCustomPermissionRequest from a dict
patched_custom_permission_request_from_dict = PatchedCustomPermissionRequest.from_dict(patched_custom_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


