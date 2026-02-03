# AgentAuthenticationResponse

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from authentik_client.models.agent_authentication_response import AgentAuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAuthenticationResponse from a JSON string
agent_authentication_response_instance = AgentAuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(AgentAuthenticationResponse.to_json())

# convert the object into a dict
agent_authentication_response_dict = agent_authentication_response_instance.to_dict()
# create an instance of AgentAuthenticationResponse from a dict
agent_authentication_response_from_dict = AgentAuthenticationResponse.from_dict(agent_authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


