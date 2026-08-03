# NativeLogoutChallengeResponseRequest

Response for native browser logout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-provider-saml-native-logout']

## Example

```python
from authentik_client.models.native_logout_challenge_response_request import NativeLogoutChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NativeLogoutChallengeResponseRequest from a JSON string
native_logout_challenge_response_request_instance = NativeLogoutChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(NativeLogoutChallengeResponseRequest.to_json())

# convert the object into a dict
native_logout_challenge_response_request_dict = native_logout_challenge_response_request_instance.to_dict()
# create an instance of NativeLogoutChallengeResponseRequest from a dict
native_logout_challenge_response_request_from_dict = NativeLogoutChallengeResponseRequest.from_dict(native_logout_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


