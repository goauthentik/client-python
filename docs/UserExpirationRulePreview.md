# UserExpirationRulePreview

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [readonly] 
**users** | [**List[UserExpirationRuleUser]**](UserExpirationRuleUser.md) |  | [readonly] 
**updated** | [**UserExpirationRulePendingPreviewGroup**](UserExpirationRulePendingPreviewGroup.md) |  | [readonly] 
**taken_over** | [**UserExpirationRulePendingPreviewGroup**](UserExpirationRulePendingPreviewGroup.md) |  | [readonly] 
**removed** | [**UserExpirationRulePendingPreviewGroup**](UserExpirationRulePendingPreviewGroup.md) |  | [readonly] 

## Example

```python
from authentik_client.models.user_expiration_rule_preview import UserExpirationRulePreview

# TODO update the JSON string below
json = "{}"
# create an instance of UserExpirationRulePreview from a JSON string
user_expiration_rule_preview_instance = UserExpirationRulePreview.from_json(json)
# print the JSON string representation of the object
print(UserExpirationRulePreview.to_json())

# convert the object into a dict
user_expiration_rule_preview_dict = user_expiration_rule_preview_instance.to_dict()
# create an instance of UserExpirationRulePreview from a dict
user_expiration_rule_preview_from_dict = UserExpirationRulePreview.from_dict(user_expiration_rule_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


