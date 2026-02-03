# AgentPSSOUserRegistrationRequest

Register Apple device user via Platform SSO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_auth** | **str** |  | 
**user_secure_enclave_key** | **str** |  | 
**enclave_key_id** | **str** |  | 

## Example

```python
from authentik_client.models.agent_psso_user_registration_request import AgentPSSOUserRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPSSOUserRegistrationRequest from a JSON string
agent_psso_user_registration_request_instance = AgentPSSOUserRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(AgentPSSOUserRegistrationRequest.to_json())

# convert the object into a dict
agent_psso_user_registration_request_dict = agent_psso_user_registration_request_instance.to_dict()
# create an instance of AgentPSSOUserRegistrationRequest from a dict
agent_psso_user_registration_request_from_dict = AgentPSSOUserRegistrationRequest.from_dict(agent_psso_user_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


