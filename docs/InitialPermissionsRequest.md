# InitialPermissionsRequest

InitialPermissions serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mode** | [**InitialPermissionsModeEnum**](InitialPermissionsModeEnum.md) |  | 
**role** | **str** |  | 
**permissions** | **List[int]** |  | [optional] 

## Example

```python
from authentik_client.models.initial_permissions_request import InitialPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitialPermissionsRequest from a JSON string
initial_permissions_request_instance = InitialPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(InitialPermissionsRequest.to_json())

# convert the object into a dict
initial_permissions_request_dict = initial_permissions_request_instance.to_dict()
# create an instance of InitialPermissionsRequest from a dict
initial_permissions_request_from_dict = InitialPermissionsRequest.from_dict(initial_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


