# PatchedPermissionCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**endpoints** | **List[str]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_permission_check_request import PatchedPermissionCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPermissionCheckRequest from a JSON string
patched_permission_check_request_instance = PatchedPermissionCheckRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPermissionCheckRequest.to_json())

# convert the object into a dict
patched_permission_check_request_dict = patched_permission_check_request_instance.to_dict()
# create an instance of PatchedPermissionCheckRequest from a dict
patched_permission_check_request_from_dict = PatchedPermissionCheckRequest.from_dict(patched_permission_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


