# PermissionCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**expression** | **str** |  | 
**endpoints** | **List[str]** |  | 
**unknown_endpoints** | **List[str]** |  | [readonly] 
**unknown_fields** | **Dict[str, List[str]]** |  | [readonly] 

## Example

```python
from authentik_client.models.permission_check import PermissionCheck

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheck from a JSON string
permission_check_instance = PermissionCheck.from_json(json)
# print the JSON string representation of the object
print(PermissionCheck.to_json())

# convert the object into a dict
permission_check_dict = permission_check_instance.to_dict()
# create an instance of PermissionCheck from a dict
permission_check_from_dict = PermissionCheck.from_dict(permission_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


