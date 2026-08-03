# PatchedAccountLockdownStageRequest

AccountLockdownStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**deactivate_user** | **bool** | Deactivate the user account (set is_active to False) | [optional] 
**set_unusable_password** | **bool** | Set an unusable password for the user | [optional] 
**delete_sessions** | **bool** | Delete all active sessions for the user | [optional] 
**revoke_tokens** | **bool** | Revoke all tokens for the user (API, app password, recovery, verification, OAuth) | [optional] 
**self_service_completion_flow** | **UUID** | Flow to redirect users to after self-service lockdown. This flow should not require authentication since the user&#39;s session is deleted. | [optional] 

## Example

```python
from authentik_client.models.patched_account_lockdown_stage_request import PatchedAccountLockdownStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAccountLockdownStageRequest from a JSON string
patched_account_lockdown_stage_request_instance = PatchedAccountLockdownStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAccountLockdownStageRequest.to_json())

# convert the object into a dict
patched_account_lockdown_stage_request_dict = patched_account_lockdown_stage_request_instance.to_dict()
# create an instance of PatchedAccountLockdownStageRequest from a dict
patched_account_lockdown_stage_request_from_dict = PatchedAccountLockdownStageRequest.from_dict(patched_account_lockdown_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


