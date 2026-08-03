# UserOffboarding

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly] 
**user** | **int** |  | 
**user_obj** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**scheduled_at** | **datetime** | Absolute time at which the offboarding action is executed. | 
**action** | [**OffboardingActionEnum**](OffboardingActionEnum.md) |  | [optional] 
**revoke_sessions** | **bool** | Revoke all of the user&#39;s sessions when offboarding. | [optional] 
**revoke_tokens** | **bool** | Revoke all of the user&#39;s tokens when offboarding. | [optional] 
**status** | [**OffboardingStatusEnum**](OffboardingStatusEnum.md) |  | [readonly] 
**created_by_obj** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**executed_at** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.user_offboarding import UserOffboarding

# TODO update the JSON string below
json = "{}"
# create an instance of UserOffboarding from a JSON string
user_offboarding_instance = UserOffboarding.from_json(json)
# print the JSON string representation of the object
print(UserOffboarding.to_json())

# convert the object into a dict
user_offboarding_dict = user_offboarding_instance.to_dict()
# create an instance of UserOffboarding from a dict
user_offboarding_from_dict = UserOffboarding.from_dict(user_offboarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


