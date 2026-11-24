# UserExpirationRulePendingPreview

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly] 
**user** | [**UserExpirationRuleUser**](UserExpirationRuleUser.md) |  | [readonly] 
**previous_action** | [**OffboardingActionEnum**](OffboardingActionEnum.md) |  | [readonly] 
**action** | [**OffboardingActionEnum**](OffboardingActionEnum.md) |  | [readonly] 
**previous_scheduled_at** | **datetime** |  | [readonly] 
**scheduled_at** | **datetime** |  | [readonly] 
**previous_revoke_sessions** | **bool** |  | [readonly] 
**revoke_sessions** | **bool** |  | [readonly] 
**previous_revoke_tokens** | **bool** |  | [readonly] 
**revoke_tokens** | **bool** |  | [readonly] 

## Example

```python
from authentik_client.models.user_expiration_rule_pending_preview import UserExpirationRulePendingPreview

# TODO update the JSON string below
json = "{}"
# create an instance of UserExpirationRulePendingPreview from a JSON string
user_expiration_rule_pending_preview_instance = UserExpirationRulePendingPreview.from_json(json)
# print the JSON string representation of the object
print(UserExpirationRulePendingPreview.to_json())

# convert the object into a dict
user_expiration_rule_pending_preview_dict = user_expiration_rule_pending_preview_instance.to_dict()
# create an instance of UserExpirationRulePendingPreview from a dict
user_expiration_rule_pending_preview_from_dict = UserExpirationRulePendingPreview.from_dict(user_expiration_rule_pending_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


