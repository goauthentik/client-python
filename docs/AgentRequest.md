# AgentRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from authentik_client.models.agent_request import AgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRequest from a JSON string
agent_request_instance = AgentRequest.from_json(json)
# print the JSON string representation of the object
print(AgentRequest.to_json())

# convert the object into a dict
agent_request_dict = agent_request_instance.to_dict()
# create an instance of AgentRequest from a dict
agent_request_from_dict = AgentRequest.from_dict(agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


