# IdentificationChallenge

Identification challenges with all UI elements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-identification']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**user_fields** | **List[str]** |  | 
**password_fields** | **bool** |  | 
**allow_show_password** | **bool** |  | [optional] [default to False]
**application_pre** | **str** |  | [optional] 
**flow_designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) |  | 
**captcha_stage** | [**CaptchaChallenge**](CaptchaChallenge.md) |  | [optional] 
**enroll_url** | **str** |  | [optional] 
**recovery_url** | **str** |  | [optional] 
**passwordless_url** | **str** |  | [optional] 
**primary_action** | **str** |  | 
**sources** | [**List[LoginSource]**](LoginSource.md) |  | [optional] 
**show_source_labels** | **bool** |  | 
**enable_remember_me** | **bool** |  | [optional] [default to True]

## Example

```python
from authentik_client.models.identification_challenge import IdentificationChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationChallenge from a JSON string
identification_challenge_instance = IdentificationChallenge.from_json(json)
# print the JSON string representation of the object
print(IdentificationChallenge.to_json())

# convert the object into a dict
identification_challenge_dict = identification_challenge_instance.to_dict()
# create an instance of IdentificationChallenge from a dict
identification_challenge_from_dict = IdentificationChallenge.from_dict(identification_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


