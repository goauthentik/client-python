# Agent

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**uid** | **str** |  | [readonly] 
**uuid** | **UUID** |  | [readonly] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**parent** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**policy_behavior** | [**PolicyBehaviorEnum**](PolicyBehaviorEnum.md) |  | [readonly] 
**token_identifier** | **str** | Identifier of the agent&#39;s API token, so its key can be retrieved/copied later. | [readonly] 

## Example

```python
from authentik_client.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


