# AgentPSSODeviceRegistrationResponse

authentik settings for Platform SSO tokens

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**issuer** | **str** |  | 
**token_endpoint** | **str** |  | 
**jwks_endpoint** | **str** |  | 
**audience** | **str** |  | 
**nonce_endpoint** | **str** |  | 

## Example

```python
from authentik_client.models.agent_psso_device_registration_response import AgentPSSODeviceRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPSSODeviceRegistrationResponse from a JSON string
agent_psso_device_registration_response_instance = AgentPSSODeviceRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(AgentPSSODeviceRegistrationResponse.to_json())

# convert the object into a dict
agent_psso_device_registration_response_dict = agent_psso_device_registration_response_instance.to_dict()
# create an instance of AgentPSSODeviceRegistrationResponse from a dict
agent_psso_device_registration_response_from_dict = AgentPSSODeviceRegistrationResponse.from_dict(agent_psso_device_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


