# DummyChallengeResponseRequest

Dummy challenge response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-dummy']

## Example

```python
from authentik_client.models.dummy_challenge_response_request import DummyChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DummyChallengeResponseRequest from a JSON string
dummy_challenge_response_request_instance = DummyChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(DummyChallengeResponseRequest.to_json())

# convert the object into a dict
dummy_challenge_response_request_dict = dummy_challenge_response_request_instance.to_dict()
# create an instance of DummyChallengeResponseRequest from a dict
dummy_challenge_response_request_from_dict = DummyChallengeResponseRequest.from_dict(dummy_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


