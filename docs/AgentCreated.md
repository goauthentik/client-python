# AgentCreated

Response returned once when an agent is created, carrying the one-time API token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**Agent**](Agent.md) |  | [readonly] 
**token** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.agent_created import AgentCreated

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCreated from a JSON string
agent_created_instance = AgentCreated.from_json(json)
# print the JSON string representation of the object
print(AgentCreated.to_json())

# convert the object into a dict
agent_created_dict = agent_created_instance.to_dict()
# create an instance of AgentCreated from a dict
agent_created_from_dict = AgentCreated.from_dict(agent_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


