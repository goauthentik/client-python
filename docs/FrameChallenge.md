# FrameChallenge

Challenge type to render a frame

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'xak-flow-frame']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**url** | **str** |  | 
**loading_overlay** | **bool** |  | [optional] [default to False]
**loading_text** | **str** |  | 

## Example

```python
from authentik_client.models.frame_challenge import FrameChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of FrameChallenge from a JSON string
frame_challenge_instance = FrameChallenge.from_json(json)
# print the JSON string representation of the object
print(FrameChallenge.to_json())

# convert the object into a dict
frame_challenge_dict = frame_challenge_instance.to_dict()
# create an instance of FrameChallenge from a dict
frame_challenge_from_dict = FrameChallenge.from_dict(frame_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


