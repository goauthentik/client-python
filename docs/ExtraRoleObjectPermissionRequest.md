# ExtraRoleObjectPermissionRequest

User permission with additional object-related data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_pk** | **str** |  | 

## Example

```python
from authentik_client.models.extra_role_object_permission_request import ExtraRoleObjectPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraRoleObjectPermissionRequest from a JSON string
extra_role_object_permission_request_instance = ExtraRoleObjectPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(ExtraRoleObjectPermissionRequest.to_json())

# convert the object into a dict
extra_role_object_permission_request_dict = extra_role_object_permission_request_instance.to_dict()
# create an instance of ExtraRoleObjectPermissionRequest from a dict
extra_role_object_permission_request_from_dict = ExtraRoleObjectPermissionRequest.from_dict(extra_role_object_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


