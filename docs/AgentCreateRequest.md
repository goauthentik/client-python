# AgentCreateRequest

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**expiring** | **bool** |  | [optional] [default to False]
**expires** | **datetime** |  | [optional] 
**policy_behavior** | [**PolicyBehaviorEnum**](PolicyBehaviorEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.agent_create_request import AgentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCreateRequest from a JSON string
agent_create_request_instance = AgentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentCreateRequest.to_json())

# convert the object into a dict
agent_create_request_dict = agent_create_request_instance.to_dict()
# create an instance of AgentCreateRequest from a dict
agent_create_request_from_dict = AgentCreateRequest.from_dict(agent_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


