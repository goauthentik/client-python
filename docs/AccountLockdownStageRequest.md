# AccountLockdownStageRequest

AccountLockdownStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**deactivate_user** | **bool** | Deactivate the user account (set is_active to False) | [optional] 
**set_unusable_password** | **bool** | Set an unusable password for the user | [optional] 
**delete_sessions** | **bool** | Delete all active sessions for the user | [optional] 
**revoke_tokens** | **bool** | Revoke all tokens for the user (API, app password, recovery, verification, OAuth) | [optional] 
**self_service_completion_flow** | **UUID** | Flow to redirect users to after self-service lockdown. This flow should not require authentication since the user&#39;s session is deleted. | [optional] 

## Example

```python
from authentik_client.models.account_lockdown_stage_request import AccountLockdownStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLockdownStageRequest from a JSON string
account_lockdown_stage_request_instance = AccountLockdownStageRequest.from_json(json)
# print the JSON string representation of the object
print(AccountLockdownStageRequest.to_json())

# convert the object into a dict
account_lockdown_stage_request_dict = account_lockdown_stage_request_instance.to_dict()
# create an instance of AccountLockdownStageRequest from a dict
account_lockdown_stage_request_from_dict = AccountLockdownStageRequest.from_dict(account_lockdown_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


