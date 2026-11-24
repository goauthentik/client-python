# AgentPSSODeviceStateUser

A user currently registered for Platform SSO on this device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**enclave_key_id** | **str** |  | 

## Example

```python
from authentik_client.models.agent_psso_device_state_user import AgentPSSODeviceStateUser

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPSSODeviceStateUser from a JSON string
agent_psso_device_state_user_instance = AgentPSSODeviceStateUser.from_json(json)
# print the JSON string representation of the object
print(AgentPSSODeviceStateUser.to_json())

# convert the object into a dict
agent_psso_device_state_user_dict = agent_psso_device_state_user_instance.to_dict()
# create an instance of AgentPSSODeviceStateUser from a dict
agent_psso_device_state_user_from_dict = AgentPSSODeviceStateUser.from_dict(agent_psso_device_state_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


