# UserAccountLockdownRequest

Choose the target account before starting the lockdown flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** | User to lock. If omitted, locks the current user (self-service). | [optional] 

## Example

```python
from authentik_client.models.user_account_lockdown_request import UserAccountLockdownRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountLockdownRequest from a JSON string
user_account_lockdown_request_instance = UserAccountLockdownRequest.from_json(json)
# print the JSON string representation of the object
print(UserAccountLockdownRequest.to_json())

# convert the object into a dict
user_account_lockdown_request_dict = user_account_lockdown_request_instance.to_dict()
# create an instance of UserAccountLockdownRequest from a dict
user_account_lockdown_request_from_dict = UserAccountLockdownRequest.from_dict(user_account_lockdown_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


