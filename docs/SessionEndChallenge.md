# SessionEndChallenge

Challenge for ending a session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-session-end']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**application_name** | **str** |  | [optional] 
**application_launch_url** | **str** |  | [optional] 
**invalidation_flow_url** | **str** |  | [optional] 
**brand_name** | **str** |  | 

## Example

```python
from authentik_client.models.session_end_challenge import SessionEndChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of SessionEndChallenge from a JSON string
session_end_challenge_instance = SessionEndChallenge.from_json(json)
# print the JSON string representation of the object
print(SessionEndChallenge.to_json())

# convert the object into a dict
session_end_challenge_dict = session_end_challenge_instance.to_dict()
# create an instance of SessionEndChallenge from a dict
session_end_challenge_from_dict = SessionEndChallenge.from_dict(session_end_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


