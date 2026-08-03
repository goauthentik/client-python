# AgentPSSODeviceRegistrationRequest

Register Apple device via Platform SSO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_signing_key** | **str** |  | 
**device_encryption_key** | **str** |  | 
**sign_key_id** | **str** |  | 
**enc_key_id** | **str** |  | 

## Example

```python
from authentik_client.models.agent_psso_device_registration_request import AgentPSSODeviceRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPSSODeviceRegistrationRequest from a JSON string
agent_psso_device_registration_request_instance = AgentPSSODeviceRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(AgentPSSODeviceRegistrationRequest.to_json())

# convert the object into a dict
agent_psso_device_registration_request_dict = agent_psso_device_registration_request_instance.to_dict()
# create an instance of AgentPSSODeviceRegistrationRequest from a dict
agent_psso_device_registration_request_from_dict = AgentPSSODeviceRegistrationRequest.from_dict(agent_psso_device_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


