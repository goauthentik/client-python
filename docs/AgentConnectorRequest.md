# AgentConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **str** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**snapshot_expiry** | **str** |  | [optional] 
**auth_session_duration** | **str** |  | [optional] 
**auth_terminate_session_on_expiry** | **bool** |  | [optional] 
**refresh_interval** | **str** |  | [optional] 
**authorization_flow** | **str** |  | [optional] 
**nss_uid_offset** | **int** |  | [optional] 
**nss_gid_offset** | **int** |  | [optional] 
**challenge_key** | **str** |  | [optional] 
**challenge_idle_timeout** | **str** |  | [optional] 
**challenge_trigger_check_in** | **bool** |  | [optional] 
**jwt_federation_providers** | **List[int]** |  | [optional] 

## Example

```python
from authentik_client.models.agent_connector_request import AgentConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConnectorRequest from a JSON string
agent_connector_request_instance = AgentConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(AgentConnectorRequest.to_json())

# convert the object into a dict
agent_connector_request_dict = agent_connector_request_instance.to_dict()
# create an instance of AgentConnectorRequest from a dict
agent_connector_request_from_dict = AgentConnectorRequest.from_dict(agent_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


