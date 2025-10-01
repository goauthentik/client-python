# FlowChallengeResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-user-login']
**code** | **str** |  | 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**selected_challenge** | [**DeviceChallengeRequest**](DeviceChallengeRequest.md) |  | [optional] 
**selected_stage** | **str** |  | [optional] 
**webauthn** | **Dict[str, object]** |  | [optional] 
**duo** | **int** |  | [optional] 
**response** | **Dict[str, object]** |  | 
**token** | **str** |  | 
**uid_field** | **str** |  | 
**password** | **str** |  | 
**captcha_token** | **str** |  | [optional] 
**to** | **str** |  | 
**id** | **int** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**auth_date** | **int** |  | 
**hash** | **str** |  | 
**remember_me** | **bool** |  | 

## Example

```python
from authentik_client.models.flow_challenge_response_request import FlowChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowChallengeResponseRequest from a JSON string
flow_challenge_response_request_instance = FlowChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(FlowChallengeResponseRequest.to_json())

# convert the object into a dict
flow_challenge_response_request_dict = flow_challenge_response_request_instance.to_dict()
# create an instance of FlowChallengeResponseRequest from a dict
flow_challenge_response_request_from_dict = FlowChallengeResponseRequest.from_dict(flow_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


