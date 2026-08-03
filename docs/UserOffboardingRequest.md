# UserOffboardingRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**scheduled_at** | **datetime** | Absolute time at which the offboarding action is executed. | 
**action** | [**OffboardingActionEnum**](OffboardingActionEnum.md) |  | [optional] 
**revoke_sessions** | **bool** | Revoke all of the user&#39;s sessions when offboarding. | [optional] 
**revoke_tokens** | **bool** | Revoke all of the user&#39;s tokens when offboarding. | [optional] 

## Example

```python
from authentik_client.models.user_offboarding_request import UserOffboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserOffboardingRequest from a JSON string
user_offboarding_request_instance = UserOffboardingRequest.from_json(json)
# print the JSON string representation of the object
print(UserOffboardingRequest.to_json())

# convert the object into a dict
user_offboarding_request_dict = user_offboarding_request_instance.to_dict()
# create an instance of UserOffboardingRequest from a dict
user_offboarding_request_from_dict = UserOffboardingRequest.from_dict(user_offboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


