# UserAccountSerializerForRoleRequest

Account adding/removing operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | 

## Example

```python
from authentik_client.models.user_account_serializer_for_role_request import UserAccountSerializerForRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountSerializerForRoleRequest from a JSON string
user_account_serializer_for_role_request_instance = UserAccountSerializerForRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UserAccountSerializerForRoleRequest.to_json())

# convert the object into a dict
user_account_serializer_for_role_request_dict = user_account_serializer_for_role_request_instance.to_dict()
# create an instance of UserAccountSerializerForRoleRequest from a dict
user_account_serializer_for_role_request_from_dict = UserAccountSerializerForRoleRequest.from_dict(user_account_serializer_for_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


