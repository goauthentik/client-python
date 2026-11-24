# RedirectChallengeResponseRequest

Redirect challenge response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'xak-flow-redirect']
**to** | **str** |  | 

## Example

```python
from authentik_client.models.redirect_challenge_response_request import RedirectChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectChallengeResponseRequest from a JSON string
redirect_challenge_response_request_instance = RedirectChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectChallengeResponseRequest.to_json())

# convert the object into a dict
redirect_challenge_response_request_dict = redirect_challenge_response_request_instance.to_dict()
# create an instance of RedirectChallengeResponseRequest from a dict
redirect_challenge_response_request_from_dict = RedirectChallengeResponseRequest.from_dict(redirect_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


