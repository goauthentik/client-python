# DummyChallenge

Dummy challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-dummy']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from authentik_client.models.dummy_challenge import DummyChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of DummyChallenge from a JSON string
dummy_challenge_instance = DummyChallenge.from_json(json)
# print the JSON string representation of the object
print(DummyChallenge.to_json())

# convert the object into a dict
dummy_challenge_dict = dummy_challenge_instance.to_dict()
# create an instance of DummyChallenge from a dict
dummy_challenge_from_dict = DummyChallenge.from_dict(dummy_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


