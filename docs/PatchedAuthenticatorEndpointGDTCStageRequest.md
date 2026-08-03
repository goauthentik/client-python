# PatchedAuthenticatorEndpointGDTCStageRequest

AuthenticatorEndpointGDTCStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**configure_flow** | **UUID** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**credentials** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_authenticator_endpoint_gdtc_stage_request import PatchedAuthenticatorEndpointGDTCStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAuthenticatorEndpointGDTCStageRequest from a JSON string
patched_authenticator_endpoint_gdtc_stage_request_instance = PatchedAuthenticatorEndpointGDTCStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAuthenticatorEndpointGDTCStageRequest.to_json())

# convert the object into a dict
patched_authenticator_endpoint_gdtc_stage_request_dict = patched_authenticator_endpoint_gdtc_stage_request_instance.to_dict()
# create an instance of PatchedAuthenticatorEndpointGDTCStageRequest from a dict
patched_authenticator_endpoint_gdtc_stage_request_from_dict = PatchedAuthenticatorEndpointGDTCStageRequest.from_dict(patched_authenticator_endpoint_gdtc_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


