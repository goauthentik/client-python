# UserExpirationRuleGroup

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.user_expiration_rule_group import UserExpirationRuleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserExpirationRuleGroup from a JSON string
user_expiration_rule_group_instance = UserExpirationRuleGroup.from_json(json)
# print the JSON string representation of the object
print(UserExpirationRuleGroup.to_json())

# convert the object into a dict
user_expiration_rule_group_dict = user_expiration_rule_group_instance.to_dict()
# create an instance of UserExpirationRuleGroup from a dict
user_expiration_rule_group_from_dict = UserExpirationRuleGroup.from_dict(user_expiration_rule_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


