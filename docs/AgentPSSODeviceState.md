# AgentPSSODeviceState

What authentik currently has stored for this device's Platform SSO registration, so the client can detect drift and repair it

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_registered** | **bool** |  | 
**sign_key_id** | **str** |  | 
**enc_key_id** | **str** |  | 
**users** | [**List[AgentPSSODeviceStateUser]**](AgentPSSODeviceStateUser.md) |  | 

## Example

```python
from authentik_client.models.agent_psso_device_state import AgentPSSODeviceState

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPSSODeviceState from a JSON string
agent_psso_device_state_instance = AgentPSSODeviceState.from_json(json)
# print the JSON string representation of the object
print(AgentPSSODeviceState.to_json())

# convert the object into a dict
agent_psso_device_state_dict = agent_psso_device_state_instance.to_dict()
# create an instance of AgentPSSODeviceState from a dict
agent_psso_device_state_from_dict = AgentPSSODeviceState.from_dict(agent_psso_device_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


