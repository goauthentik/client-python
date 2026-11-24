# UserExpirationRulePendingPreviewGroup

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [readonly] 
**offboardings** | [**List[UserExpirationRulePendingPreview]**](UserExpirationRulePendingPreview.md) |  | [readonly] 

## Example

```python
from authentik_client.models.user_expiration_rule_pending_preview_group import UserExpirationRulePendingPreviewGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserExpirationRulePendingPreviewGroup from a JSON string
user_expiration_rule_pending_preview_group_instance = UserExpirationRulePendingPreviewGroup.from_json(json)
# print the JSON string representation of the object
print(UserExpirationRulePendingPreviewGroup.to_json())

# convert the object into a dict
user_expiration_rule_pending_preview_group_dict = user_expiration_rule_pending_preview_group_instance.to_dict()
# create an instance of UserExpirationRulePendingPreviewGroup from a dict
user_expiration_rule_pending_preview_group_from_dict = UserExpirationRulePendingPreviewGroup.from_dict(user_expiration_rule_pending_preview_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


