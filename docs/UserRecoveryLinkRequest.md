# UserRecoveryLinkRequest

Payload to create a recovery link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_duration** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.user_recovery_link_request import UserRecoveryLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecoveryLinkRequest from a JSON string
user_recovery_link_request_instance = UserRecoveryLinkRequest.from_json(json)
# print the JSON string representation of the object
print(UserRecoveryLinkRequest.to_json())

# convert the object into a dict
user_recovery_link_request_dict = user_recovery_link_request_instance.to_dict()
# create an instance of UserRecoveryLinkRequest from a dict
user_recovery_link_request_from_dict = UserRecoveryLinkRequest.from_dict(user_recovery_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


