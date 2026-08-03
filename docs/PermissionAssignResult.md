# PermissionAssignResult

Result from assigning permissions to a user/role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from authentik_client.models.permission_assign_result import PermissionAssignResult

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAssignResult from a JSON string
permission_assign_result_instance = PermissionAssignResult.from_json(json)
# print the JSON string representation of the object
print(PermissionAssignResult.to_json())

# convert the object into a dict
permission_assign_result_dict = permission_assign_result_instance.to_dict()
# create an instance of PermissionAssignResult from a dict
permission_assign_result_from_dict = PermissionAssignResult.from_dict(permission_assign_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


