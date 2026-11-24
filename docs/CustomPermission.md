# CustomPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**codename** | **str** |  | 
**name** | **str** |  | 
**model** | **str** |  | 
**permission** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.custom_permission import CustomPermission

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPermission from a JSON string
custom_permission_instance = CustomPermission.from_json(json)
# print the JSON string representation of the object
print(CustomPermission.to_json())

# convert the object into a dict
custom_permission_dict = custom_permission_instance.to_dict()
# create an instance of CustomPermission from a dict
custom_permission_from_dict = CustomPermission.from_dict(custom_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


