# SCIMSourceUser

SCIMSourceUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**external_id** | **str** |  | 
**user** | **int** |  | 
**user_obj** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**source** | **UUID** |  | 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.scim_source_user import SCIMSourceUser

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMSourceUser from a JSON string
scim_source_user_instance = SCIMSourceUser.from_json(json)
# print the JSON string representation of the object
print(SCIMSourceUser.to_json())

# convert the object into a dict
scim_source_user_dict = scim_source_user_instance.to_dict()
# create an instance of SCIMSourceUser from a dict
scim_source_user_from_dict = SCIMSourceUser.from_dict(scim_source_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


