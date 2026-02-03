# AgentTokenResponse

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**expires_in** | **int** |  | [optional] 

## Example

```python
from authentik_client.models.agent_token_response import AgentTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTokenResponse from a JSON string
agent_token_response_instance = AgentTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AgentTokenResponse.to_json())

# convert the object into a dict
agent_token_response_dict = agent_token_response_instance.to_dict()
# create an instance of AgentTokenResponse from a dict
agent_token_response_from_dict = AgentTokenResponse.from_dict(agent_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


