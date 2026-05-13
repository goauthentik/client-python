# EndpointAgentChallenge

Signed challenge for authentik agent to respond to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-endpoint-agent']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**challenge** | **str** |  | 
**challenge_idle_timeout** | **int** |  | 

## Example

```python
from authentik_client.models.endpoint_agent_challenge import EndpointAgentChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentChallenge from a JSON string
endpoint_agent_challenge_instance = EndpointAgentChallenge.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentChallenge.to_json())

# convert the object into a dict
endpoint_agent_challenge_dict = endpoint_agent_challenge_instance.to_dict()
# create an instance of EndpointAgentChallenge from a dict
endpoint_agent_challenge_from_dict = EndpointAgentChallenge.from_dict(endpoint_agent_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


