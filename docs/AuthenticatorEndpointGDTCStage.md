# AuthenticatorEndpointGDTCStage

AuthenticatorEndpointGDTCStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**credentials** | **object** |  | 

## Example

```python
from authentik_client.models.authenticator_endpoint_gdtc_stage import AuthenticatorEndpointGDTCStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEndpointGDTCStage from a JSON string
authenticator_endpoint_gdtc_stage_instance = AuthenticatorEndpointGDTCStage.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEndpointGDTCStage.to_json())

# convert the object into a dict
authenticator_endpoint_gdtc_stage_dict = authenticator_endpoint_gdtc_stage_instance.to_dict()
# create an instance of AuthenticatorEndpointGDTCStage from a dict
authenticator_endpoint_gdtc_stage_from_dict = AuthenticatorEndpointGDTCStage.from_dict(authenticator_endpoint_gdtc_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


