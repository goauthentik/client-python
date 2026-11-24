# EndpointAgentChallengeResponseRequest

Response to signed challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-endpoint-agent']
**response** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.endpoint_agent_challenge_response_request import EndpointAgentChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentChallengeResponseRequest from a JSON string
endpoint_agent_challenge_response_request_instance = EndpointAgentChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentChallengeResponseRequest.to_json())

# convert the object into a dict
endpoint_agent_challenge_response_request_dict = endpoint_agent_challenge_response_request_instance.to_dict()
# create an instance of EndpointAgentChallengeResponseRequest from a dict
endpoint_agent_challenge_response_request_from_dict = EndpointAgentChallengeResponseRequest.from_dict(endpoint_agent_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


