# CustomPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codename** | **str** |  | 
**name** | **str** |  | 
**model** | **str** |  | 

## Example

```python
from authentik_client.models.custom_permission_request import CustomPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPermissionRequest from a JSON string
custom_permission_request_instance = CustomPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(CustomPermissionRequest.to_json())

# convert the object into a dict
custom_permission_request_dict = custom_permission_request_instance.to_dict()
# create an instance of CustomPermissionRequest from a dict
custom_permission_request_from_dict = CustomPermissionRequest.from_dict(custom_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


