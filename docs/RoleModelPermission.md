# RoleModelPermission

Role-bound object level permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**codename** | **str** |  | [readonly] 
**model** | **str** |  | [readonly] 
**app_label** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.role_model_permission import RoleModelPermission

# TODO update the JSON string below
json = "{}"
# create an instance of RoleModelPermission from a JSON string
role_model_permission_instance = RoleModelPermission.from_json(json)
# print the JSON string representation of the object
print(RoleModelPermission.to_json())

# convert the object into a dict
role_model_permission_dict = role_model_permission_instance.to_dict()
# create an instance of RoleModelPermission from a dict
role_model_permission_from_dict = RoleModelPermission.from_dict(role_model_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


