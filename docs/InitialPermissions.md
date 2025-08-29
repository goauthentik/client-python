# InitialPermissions

InitialPermissions serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**mode** | [**InitialPermissionsModeEnum**](InitialPermissionsModeEnum.md) |  | 
**role** | **str** |  | 
**permissions** | **List[int]** |  | [optional] 
**permissions_obj** | [**List[Permission]**](Permission.md) |  | [readonly] 

## Example

```python
from authentik_client.models.initial_permissions import InitialPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of InitialPermissions from a JSON string
initial_permissions_instance = InitialPermissions.from_json(json)
# print the JSON string representation of the object
print(InitialPermissions.to_json())

# convert the object into a dict
initial_permissions_dict = initial_permissions_instance.to_dict()
# create an instance of InitialPermissions from a dict
initial_permissions_from_dict = InitialPermissions.from_dict(initial_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


