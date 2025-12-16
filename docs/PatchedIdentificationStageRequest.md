# PatchedIdentificationStageRequest

IdentificationStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**user_fields** | [**List[UserFieldsEnum]**](UserFieldsEnum.md) | Fields of the user object to match against. (Hold shift to select multiple options) | [optional] 
**password_stage** | **str** | When set, shows a password field, instead of showing the password field as separate step. | [optional] 
**captcha_stage** | **str** | When set, adds functionality exactly like a Captcha stage, but baked into the Identification stage. | [optional] 
**case_insensitive_matching** | **bool** | When enabled, user fields are matched regardless of their casing. | [optional] 
**show_matched_user** | **bool** | When a valid username/email has been entered, and this option is enabled, the user&#39;s username and avatar will be shown. Otherwise, the text that the user entered will be shown | [optional] 
**enrollment_flow** | **str** | Optional enrollment flow, which is linked at the bottom of the page. | [optional] 
**recovery_flow** | **str** | Optional recovery flow, which is linked at the bottom of the page. | [optional] 
**passwordless_flow** | **str** | Optional passwordless flow, which is linked at the bottom of the page. | [optional] 
**sources** | **List[str]** | Specify which sources should be shown. | [optional] 
**show_source_labels** | **bool** |  | [optional] 
**pretend_user_exists** | **bool** | When enabled, the stage will succeed and continue even when incorrect user info is entered. | [optional] 
**enable_remember_me** | **bool** | Show the user the &#39;Remember me on this device&#39; toggle, allowing repeat users to skip straight to entering their password. | [optional] 
**webauthn_stage** | **str** | When set, and conditional WebAuthn is available, allow the user to use their passkey as a first factor. | [optional] 

## Example

```python
from authentik_client.models.patched_identification_stage_request import PatchedIdentificationStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedIdentificationStageRequest from a JSON string
patched_identification_stage_request_instance = PatchedIdentificationStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedIdentificationStageRequest.to_json())

# convert the object into a dict
patched_identification_stage_request_dict = patched_identification_stage_request_instance.to_dict()
# create an instance of PatchedIdentificationStageRequest from a dict
patched_identification_stage_request_from_dict = PatchedIdentificationStageRequest.from_dict(patched_identification_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


