# PermissionRequest

Global permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**codename** | **str** |  | 

## Example

```python
from authentik_client.models.permission_request import PermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionRequest from a JSON string
permission_request_instance = PermissionRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionRequest.to_json())

# convert the object into a dict
permission_request_dict = permission_request_instance.to_dict()
# create an instance of PermissionRequest from a dict
permission_request_from_dict = PermissionRequest.from_dict(permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


