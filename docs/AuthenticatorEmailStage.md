# AuthenticatorEmailStage

AuthenticatorEmailStage Serializer

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
**use_global_settings** | **bool** | When enabled, global Email connection settings will be used and connection settings below will be ignored. | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 
**use_ssl** | **bool** |  | [optional] 
**timeout** | **int** |  | [optional] 
**from_address** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**token_expiry** | **str** | Time the token sent is valid (Format: hours&#x3D;3,minutes&#x3D;17,seconds&#x3D;300). | [optional] 
**template** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.authenticator_email_stage import AuthenticatorEmailStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEmailStage from a JSON string
authenticator_email_stage_instance = AuthenticatorEmailStage.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEmailStage.to_json())

# convert the object into a dict
authenticator_email_stage_dict = authenticator_email_stage_instance.to_dict()
# create an instance of AuthenticatorEmailStage from a dict
authenticator_email_stage_from_dict = AuthenticatorEmailStage.from_dict(authenticator_email_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


