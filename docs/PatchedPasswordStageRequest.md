# PatchedPasswordStageRequest

PasswordStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**backends** | [**List[BackendsEnum]**](BackendsEnum.md) | Selection of backends to test the password against. | [optional] 
**configure_flow** | **UUID** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**failed_attempts_before_cancel** | **int** | How many attempts a user has before the flow is canceled. This only cancels the flow, it does not lock the user&#39;s password. | [optional] 
**failed_attempts_before_lockout** | **int** | How many consecutive failed attempts lock the user&#39;s password until an administrator unlocks it. Set to 0 to never lock. | [optional] 
**last_attempt_warning_message** | **str** | Warning shown when the user has one password attempt remaining. Leave blank to show no warning. | [optional] 
**lockout_message** | **str** | Message shown when the user&#39;s password has been locked. Leave blank to show a generic authentication error. | [optional] 
**allow_show_password** | **bool** | When enabled, provides a &#39;show password&#39; button with the password input field. | [optional] 

## Example

```python
from authentik_client.models.patched_password_stage_request import PatchedPasswordStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPasswordStageRequest from a JSON string
patched_password_stage_request_instance = PatchedPasswordStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPasswordStageRequest.to_json())

# convert the object into a dict
patched_password_stage_request_dict = patched_password_stage_request_instance.to_dict()
# create an instance of PatchedPasswordStageRequest from a dict
patched_password_stage_request_from_dict = PatchedPasswordStageRequest.from_dict(patched_password_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


