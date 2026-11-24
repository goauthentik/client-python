# UserExpirationRuleUser

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.user_expiration_rule_user import UserExpirationRuleUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserExpirationRuleUser from a JSON string
user_expiration_rule_user_instance = UserExpirationRuleUser.from_json(json)
# print the JSON string representation of the object
print(UserExpirationRuleUser.to_json())

# convert the object into a dict
user_expiration_rule_user_dict = user_expiration_rule_user_instance.to_dict()
# create an instance of UserExpirationRuleUser from a dict
user_expiration_rule_user_from_dict = UserExpirationRuleUser.from_dict(user_expiration_rule_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


