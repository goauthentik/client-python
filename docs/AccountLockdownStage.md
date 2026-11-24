# AccountLockdownStage

AccountLockdownStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [readonly] 
**deactivate_user** | **bool** | Deactivate the user account (set is_active to False) | [optional] 
**set_unusable_password** | **bool** | Set an unusable password for the user | [optional] 
**delete_sessions** | **bool** | Delete all active sessions for the user | [optional] 
**revoke_tokens** | **bool** | Revoke all tokens for the user (API, app password, recovery, verification, OAuth) | [optional] 
**self_service_completion_flow** | **UUID** | Flow to redirect users to after self-service lockdown. This flow should not require authentication since the user&#39;s session is deleted. | [optional] 

## Example

```python
from authentik_client.models.account_lockdown_stage import AccountLockdownStage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLockdownStage from a JSON string
account_lockdown_stage_instance = AccountLockdownStage.from_json(json)
# print the JSON string representation of the object
print(AccountLockdownStage.to_json())

# convert the object into a dict
account_lockdown_stage_dict = account_lockdown_stage_instance.to_dict()
# create an instance of AccountLockdownStage from a dict
account_lockdown_stage_from_dict = AccountLockdownStage.from_dict(account_lockdown_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


