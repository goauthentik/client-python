# PatchedExtraUserObjectPermissionRequest

User permission with additional object-related data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_pk** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_extra_user_object_permission_request import PatchedExtraUserObjectPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedExtraUserObjectPermissionRequest from a JSON string
patched_extra_user_object_permission_request_instance = PatchedExtraUserObjectPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedExtraUserObjectPermissionRequest.to_json())

# convert the object into a dict
patched_extra_user_object_permission_request_dict = patched_extra_user_object_permission_request_instance.to_dict()
# create an instance of PatchedExtraUserObjectPermissionRequest from a dict
patched_extra_user_object_permission_request_from_dict = PatchedExtraUserObjectPermissionRequest.from_dict(patched_extra_user_object_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


