# AuthenticatorEndpointGDTCStageRequest

AuthenticatorEndpointGDTCStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**configure_flow** | **UUID** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**credentials** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.authenticator_endpoint_gdtc_stage_request import AuthenticatorEndpointGDTCStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEndpointGDTCStageRequest from a JSON string
authenticator_endpoint_gdtc_stage_request_instance = AuthenticatorEndpointGDTCStageRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEndpointGDTCStageRequest.to_json())

# convert the object into a dict
authenticator_endpoint_gdtc_stage_request_dict = authenticator_endpoint_gdtc_stage_request_instance.to_dict()
# create an instance of AuthenticatorEndpointGDTCStageRequest from a dict
authenticator_endpoint_gdtc_stage_request_from_dict = AuthenticatorEndpointGDTCStageRequest.from_dict(authenticator_endpoint_gdtc_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


