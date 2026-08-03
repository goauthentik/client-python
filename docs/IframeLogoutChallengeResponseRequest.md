# IframeLogoutChallengeResponseRequest

Response for iframe logout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-provider-iframe-logout']

## Example

```python
from authentik_client.models.iframe_logout_challenge_response_request import IframeLogoutChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IframeLogoutChallengeResponseRequest from a JSON string
iframe_logout_challenge_response_request_instance = IframeLogoutChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(IframeLogoutChallengeResponseRequest.to_json())

# convert the object into a dict
iframe_logout_challenge_response_request_dict = iframe_logout_challenge_response_request_instance.to_dict()
# create an instance of IframeLogoutChallengeResponseRequest from a dict
iframe_logout_challenge_response_request_from_dict = IframeLogoutChallengeResponseRequest.from_dict(iframe_logout_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


