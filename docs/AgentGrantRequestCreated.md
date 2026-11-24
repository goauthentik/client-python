# AgentGrantRequestCreated

Response to an agent's access request: the request it created, plus the URL to hand to the human it acts for. An agent has no browser, so it cannot run the approval itself -- `fulfill_url` is what its owner opens to approve or deny.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_request** | [**GrantRequest**](GrantRequest.md) |  | [readonly] 
**fulfill_url** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.agent_grant_request_created import AgentGrantRequestCreated

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGrantRequestCreated from a JSON string
agent_grant_request_created_instance = AgentGrantRequestCreated.from_json(json)
# print the JSON string representation of the object
print(AgentGrantRequestCreated.to_json())

# convert the object into a dict
agent_grant_request_created_dict = agent_grant_request_created_instance.to_dict()
# create an instance of AgentGrantRequestCreated from a dict
agent_grant_request_created_from_dict = AgentGrantRequestCreated.from_dict(agent_grant_request_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


