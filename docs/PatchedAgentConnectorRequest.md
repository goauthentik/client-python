# PatchedAgentConnectorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**snapshot_expiry** | **str** |  | [optional] 
**auth_session_duration** | **str** |  | [optional] 
**auth_terminate_session_on_expiry** | **bool** |  | [optional] 
**refresh_interval** | **str** |  | [optional] 
**authorization_flow** | **UUID** |  | [optional] 
**nss_uid_offset** | **int** |  | [optional] 
**nss_gid_offset** | **int** |  | [optional] 
**challenge_key** | **UUID** |  | [optional] 
**challenge_idle_timeout** | **str** |  | [optional] 
**challenge_trigger_check_in** | **bool** |  | [optional] 
**jwt_federation_providers** | **List[int]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_agent_connector_request import PatchedAgentConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentConnectorRequest from a JSON string
patched_agent_connector_request_instance = PatchedAgentConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAgentConnectorRequest.to_json())

# convert the object into a dict
patched_agent_connector_request_dict = patched_agent_connector_request_instance.to_dict()
# create an instance of PatchedAgentConnectorRequest from a dict
patched_agent_connector_request_from_dict = PatchedAgentConnectorRequest.from_dict(patched_agent_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


