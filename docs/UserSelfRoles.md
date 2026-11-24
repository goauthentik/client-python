# UserSelfRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**pk** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.user_self_roles import UserSelfRoles

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelfRoles from a JSON string
user_self_roles_instance = UserSelfRoles.from_json(json)
# print the JSON string representation of the object
print(UserSelfRoles.to_json())

# convert the object into a dict
user_self_roles_dict = user_self_roles_instance.to_dict()
# create an instance of UserSelfRoles from a dict
user_self_roles_from_dict = UserSelfRoles.from_dict(user_self_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


