# UserExpirationRule

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [optional] 
**pbm_uuid** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**activity_basis** | [**ActivityBasisEnum**](ActivityBasisEnum.md) | Measure inactivity from the last login or successful user activity. | [optional] 
**group** | **UUID** | Only expire members of this group (including descendant groups). Leave empty to apply to every user. | [optional] 
**group_obj** | [**UserExpirationRuleGroup**](UserExpirationRuleGroup.md) |  | [readonly] 
**user_types** | [**List[UserTypeEnum]**](UserTypeEnum.md) | Only expire users of these types. Service accounts are excluded by default. | [optional] 
**inactivity_duration** | **str** | How long a user may be inactive before they are expired. | [optional] 
**action** | [**OffboardingActionEnum**](OffboardingActionEnum.md) |  | [optional] 
**revoke_sessions** | **bool** |  | [optional] 
**revoke_tokens** | **bool** |  | [optional] 
**warn_before** | **str** | Schedule the offboarding and notify the user this long before they expire. Leave empty to expire users without warning. | [optional] 
**notification_transports** | **List[UUID]** | Select which transports should be used to warn the user. If none are selected, the notification will only be shown in the authentik UI. | [optional] 
**exclude_superusers** | **bool** | Never expire members of a superuser group. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 

## Example

```python
from authentik_client.models.user_expiration_rule import UserExpirationRule

# TODO update the JSON string below
json = "{}"
# create an instance of UserExpirationRule from a JSON string
user_expiration_rule_instance = UserExpirationRule.from_json(json)
# print the JSON string representation of the object
print(UserExpirationRule.to_json())

# convert the object into a dict
user_expiration_rule_dict = user_expiration_rule_instance.to_dict()
# create an instance of UserExpirationRule from a dict
user_expiration_rule_from_dict = UserExpirationRule.from_dict(user_expiration_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


