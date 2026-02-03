# WSFederationProvider

WSFederationProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**authentication_flow** | **UUID** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **UUID** | Flow used when authorizing this provider. | 
**invalidation_flow** | **UUID** | Flow used ending the session from a provider. | 
**property_mappings** | **List[UUID]** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**assigned_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**assigned_backchannel_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_backchannel_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**reply_url** | **str** |  | 
**assertion_valid_not_before** | **str** | Assertion valid not before current time + this value (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3). | [optional] 
**assertion_valid_not_on_or_after** | **str** | Assertion not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**session_valid_not_on_or_after** | **str** | Session not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**name_id_mapping** | **UUID** | Configure how the NameID value will be created. When left empty, the NameIDPolicy of the incoming request will be considered | [optional] 
**authn_context_class_ref_mapping** | **UUID** | Configure how the AuthnContextClassRef value will be created. When left empty, the AuthnContextClassRef will be set based on which authentication methods the user used to authenticate. | [optional] 
**digest_algorithm** | [**DigestAlgorithmEnum**](DigestAlgorithmEnum.md) |  | [optional] 
**signature_algorithm** | [**SignatureAlgorithmEnum**](SignatureAlgorithmEnum.md) |  | [optional] 
**signing_kp** | **UUID** | Keypair used to sign outgoing Responses going to the Service Provider. | [optional] 
**encryption_kp** | **UUID** | When selected, incoming assertions are encrypted by the IdP using the public key of the encryption keypair. The assertion is decrypted by the SP using the the private key. | [optional] 
**sign_assertion** | **bool** |  | [optional] 
**sign_logout_request** | **bool** |  | [optional] 
**default_name_id_policy** | [**SAMLNameIDPolicyEnum**](SAMLNameIDPolicyEnum.md) |  | [optional] 
**url_download_metadata** | **str** | Get metadata download URL | [readonly] 
**url_wsfed** | **str** | Get WS-Fed url | [readonly] 
**wtrealm** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.ws_federation_provider import WSFederationProvider

# TODO update the JSON string below
json = "{}"
# create an instance of WSFederationProvider from a JSON string
ws_federation_provider_instance = WSFederationProvider.from_json(json)
# print the JSON string representation of the object
print(WSFederationProvider.to_json())

# convert the object into a dict
ws_federation_provider_dict = ws_federation_provider_instance.to_dict()
# create an instance of WSFederationProvider from a dict
ws_federation_provider_from_dict = WSFederationProvider.from_dict(ws_federation_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


