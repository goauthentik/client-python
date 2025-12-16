# AgentConfig

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [readonly] 
**refresh_interval** | **int** |  | [readonly] 
**authorization_flow** | **str** |  | [readonly] 
**jwks_auth** | **Dict[str, object]** |  | [readonly] 
**jwks_challenge** | **Dict[str, object]** |  | [readonly] 
**nss_uid_offset** | **int** |  | 
**nss_gid_offset** | **int** |  | 
**auth_terminate_session_on_expiry** | **bool** |  | 
**system_config** | [**Config**](Config.md) |  | [readonly] 

## Example

```python
from authentik_client.models.agent_config import AgentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConfig from a JSON string
agent_config_instance = AgentConfig.from_json(json)
# print the JSON string representation of the object
print(AgentConfig.to_json())

# convert the object into a dict
agent_config_dict = agent_config_instance.to_dict()
# create an instance of AgentConfig from a dict
agent_config_from_dict = AgentConfig.from_dict(agent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


