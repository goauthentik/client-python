# PatchedAgentRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [optional] 
**name** | **str** | User&#39;s display name. | [optional] 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 

## Example

```python
from authentik_client.models.patched_agent_request import PatchedAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentRequest from a JSON string
patched_agent_request_instance = PatchedAgentRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAgentRequest.to_json())

# convert the object into a dict
patched_agent_request_dict = patched_agent_request_instance.to_dict()
# create an instance of PatchedAgentRequest from a dict
patched_agent_request_from_dict = PatchedAgentRequest.from_dict(patched_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


