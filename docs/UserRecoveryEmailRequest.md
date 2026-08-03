# UserRecoveryEmailRequest

Payload to create and email a recovery link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_duration** | **str** |  | [optional] 
**email_stage** | **UUID** |  | 

## Example

```python
from authentik_client.models.user_recovery_email_request import UserRecoveryEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecoveryEmailRequest from a JSON string
user_recovery_email_request_instance = UserRecoveryEmailRequest.from_json(json)
# print the JSON string representation of the object
print(UserRecoveryEmailRequest.to_json())

# convert the object into a dict
user_recovery_email_request_dict = user_recovery_email_request_instance.to_dict()
# create an instance of UserRecoveryEmailRequest from a dict
user_recovery_email_request_from_dict = UserRecoveryEmailRequest.from_dict(user_recovery_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


