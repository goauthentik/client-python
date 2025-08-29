# PatchedInitialPermissionsRequest

InitialPermissions serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**mode** | [**InitialPermissionsModeEnum**](InitialPermissionsModeEnum.md) |  | [optional] 
**role** | **str** |  | [optional] 
**permissions** | **List[int]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_initial_permissions_request import PatchedInitialPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInitialPermissionsRequest from a JSON string
patched_initial_permissions_request_instance = PatchedInitialPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedInitialPermissionsRequest.to_json())

# convert the object into a dict
patched_initial_permissions_request_dict = patched_initial_permissions_request_instance.to_dict()
# create an instance of PatchedInitialPermissionsRequest from a dict
patched_initial_permissions_request_from_dict = PatchedInitialPermissionsRequest.from_dict(patched_initial_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


