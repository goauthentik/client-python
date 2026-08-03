# AuthenticatorEmailChallenge

Authenticator Email Setup challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-email']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**email** | **str** |  | [optional] 
**email_required** | **bool** |  | [optional] [default to True]

## Example

```python
from authentik_client.models.authenticator_email_challenge import AuthenticatorEmailChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEmailChallenge from a JSON string
authenticator_email_challenge_instance = AuthenticatorEmailChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEmailChallenge.to_json())

# convert the object into a dict
authenticator_email_challenge_dict = authenticator_email_challenge_instance.to_dict()
# create an instance of AuthenticatorEmailChallenge from a dict
authenticator_email_challenge_from_dict = AuthenticatorEmailChallenge.from_dict(authenticator_email_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


