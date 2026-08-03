# AuthenticatorEmailChallengeResponseRequest

Authenticator Email Challenge response, device is set by get_response_instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-email']
**code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.authenticator_email_challenge_response_request import AuthenticatorEmailChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEmailChallengeResponseRequest from a JSON string
authenticator_email_challenge_response_request_instance = AuthenticatorEmailChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEmailChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_email_challenge_response_request_dict = authenticator_email_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorEmailChallengeResponseRequest from a dict
authenticator_email_challenge_response_request_from_dict = AuthenticatorEmailChallengeResponseRequest.from_dict(authenticator_email_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


