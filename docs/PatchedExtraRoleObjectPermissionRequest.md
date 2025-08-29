# PatchedExtraRoleObjectPermissionRequest

User permission with additional object-related data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_pk** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_extra_role_object_permission_request import PatchedExtraRoleObjectPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedExtraRoleObjectPermissionRequest from a JSON string
patched_extra_role_object_permission_request_instance = PatchedExtraRoleObjectPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedExtraRoleObjectPermissionRequest.to_json())

# convert the object into a dict
patched_extra_role_object_permission_request_dict = patched_extra_role_object_permission_request_instance.to_dict()
# create an instance of PatchedExtraRoleObjectPermissionRequest from a dict
patched_extra_role_object_permission_request_from_dict = PatchedExtraRoleObjectPermissionRequest.from_dict(patched_extra_role_object_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


