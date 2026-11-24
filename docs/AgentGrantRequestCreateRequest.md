# AgentGrantRequestCreateRequest

Body for an agent requesting access for itself. Deliberately narrower than `GrantRequestCreateSerializer`: an agent may not pick its own expiry, which is derived from the granting rules and capped by the agent's own lifetime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pbms** | **List[UUID]** |  | 

## Example

```python
from authentik_client.models.agent_grant_request_create_request import AgentGrantRequestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGrantRequestCreateRequest from a JSON string
agent_grant_request_create_request_instance = AgentGrantRequestCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGrantRequestCreateRequest.to_json())

# convert the object into a dict
agent_grant_request_create_request_dict = agent_grant_request_create_request_instance.to_dict()
# create an instance of AgentGrantRequestCreateRequest from a dict
agent_grant_request_create_request_from_dict = AgentGrantRequestCreateRequest.from_dict(agent_grant_request_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


