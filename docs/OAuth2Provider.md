# OAuth2Provider

OAuth2Provider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**invalidation_flow** | **str** | Flow used ending the session from a provider. | 
**property_mappings** | **List[str]** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**assigned_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**assigned_backchannel_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_backchannel_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**client_type** | [**ClientTypeEnum**](ClientTypeEnum.md) | Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**access_code_validity** | **str** | Access codes not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**access_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_threshold** | **str** | When refreshing a token, if the refresh token is valid for less than this duration, it will be renewed. When set to seconds&#x3D;0, token will always be renewed. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**include_claims_in_id_token** | **bool** | Include User claims from scopes in the id_token, for applications that don&#39;t access the userinfo endpoint. | [optional] 
**signing_key** | **str** | Key used to sign the tokens. | [optional] 
**encryption_key** | **str** | Key used to encrypt the tokens. When set, tokens will be encrypted and returned as JWEs. | [optional] 
**redirect_uris** | [**List[RedirectURI]**](RedirectURI.md) |  | 
**logout_uri** | **str** |  | [optional] 
**logout_method** | [**OAuth2ProviderLogoutMethodEnum**](OAuth2ProviderLogoutMethodEnum.md) | Backchannel logs out with server to server calls. Frontchannel uses iframes in your browser | [optional] 
**sub_mode** | [**SubModeEnum**](SubModeEnum.md) | Configure what data should be used as unique User Identifier. For most cases, the default should be fine. | [optional] 
**issuer_mode** | [**IssuerModeEnum**](IssuerModeEnum.md) | Configure how the issuer field of the ID Token should be filled. | [optional] 
**jwt_federation_sources** | **List[str]** |  | [optional] 
**jwt_federation_providers** | **List[int]** |  | [optional] 

## Example

```python
from authentik_client.models.o_auth2_provider import OAuth2Provider

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Provider from a JSON string
o_auth2_provider_instance = OAuth2Provider.from_json(json)
# print the JSON string representation of the object
print(OAuth2Provider.to_json())

# convert the object into a dict
o_auth2_provider_dict = o_auth2_provider_instance.to_dict()
# create an instance of OAuth2Provider from a dict
o_auth2_provider_from_dict = OAuth2Provider.from_dict(o_auth2_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


