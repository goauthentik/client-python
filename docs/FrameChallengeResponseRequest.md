# FrameChallengeResponseRequest

Base class for all challenge responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'xak-flow-frame']

## Example

```python
from authentik_client.models.frame_challenge_response_request import FrameChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrameChallengeResponseRequest from a JSON string
frame_challenge_response_request_instance = FrameChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(FrameChallengeResponseRequest.to_json())

# convert the object into a dict
frame_challenge_response_request_dict = frame_challenge_response_request_instance.to_dict()
# create an instance of FrameChallengeResponseRequest from a dict
frame_challenge_response_request_from_dict = FrameChallengeResponseRequest.from_dict(frame_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


