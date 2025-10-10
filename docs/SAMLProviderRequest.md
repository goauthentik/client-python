# SAMLProviderRequest

SAMLProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**invalidation_flow** | **str** | Flow used ending the session from a provider. | 
**property_mappings** | **List[str]** |  | [optional] 
**acs_url** | **str** |  | 
**sls_url** | **str** | Single Logout Service URL where the logout response should be sent. | [optional] 
**audience** | **str** | Value of the audience restriction field of the assertion. When left empty, no audience restriction will be added. | [optional] 
**issuer** | **str** | Also known as EntityID | [optional] 
**assertion_valid_not_before** | **str** | Assertion valid not before current time + this value (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3). | [optional] 
**assertion_valid_not_on_or_after** | **str** | Assertion not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**session_valid_not_on_or_after** | **str** | Session not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**name_id_mapping** | **str** | Configure how the NameID value will be created. When left empty, the NameIDPolicy of the incoming request will be considered | [optional] 
**authn_context_class_ref_mapping** | **str** | Configure how the AuthnContextClassRef value will be created. When left empty, the AuthnContextClassRef will be set based on which authentication methods the user used to authenticate. | [optional] 
**digest_algorithm** | [**DigestAlgorithmEnum**](DigestAlgorithmEnum.md) |  | [optional] 
**signature_algorithm** | [**SignatureAlgorithmEnum**](SignatureAlgorithmEnum.md) |  | [optional] 
**signing_kp** | **str** | Keypair used to sign outgoing Responses going to the Service Provider. | [optional] 
**verification_kp** | **str** | When selected, incoming assertion&#39;s Signatures will be validated against this certificate. To allow unsigned Requests, leave on default. | [optional] 
**encryption_kp** | **str** | When selected, incoming assertions are encrypted by the IdP using the public key of the encryption keypair. The assertion is decrypted by the SP using the the private key. | [optional] 
**sign_assertion** | **bool** |  | [optional] 
**sign_response** | **bool** |  | [optional] 
**sign_logout_request** | **bool** |  | [optional] 
**sp_binding** | [**SAMLBindingsEnum**](SAMLBindingsEnum.md) | This determines how authentik sends the response back to the Service Provider. | [optional] 
**sls_binding** | [**SAMLBindingsEnum**](SAMLBindingsEnum.md) | This determines how authentik sends the logout response back to the Service Provider. | [optional] 
**logout_method** | [**SAMLProviderLogoutMethodEnum**](SAMLProviderLogoutMethodEnum.md) | Method to use for logout. Front-channel iframe loads all logout URLs simultaneously in hidden iframes. Front-channel native uses your active browser tab to send post requests and redirect to providers. Back-channel sends logout requests directly from the server without user interaction (requires POST SLS binding). | [optional] 
**default_relay_state** | **str** | Default relay_state value for IDP-initiated logins | [optional] 
**default_name_id_policy** | [**SAMLNameIDPolicyEnum**](SAMLNameIDPolicyEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.saml_provider_request import SAMLProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLProviderRequest from a JSON string
saml_provider_request_instance = SAMLProviderRequest.from_json(json)
# print the JSON string representation of the object
print(SAMLProviderRequest.to_json())

# convert the object into a dict
saml_provider_request_dict = saml_provider_request_instance.to_dict()
# create an instance of SAMLProviderRequest from a dict
saml_provider_request_from_dict = SAMLProviderRequest.from_dict(saml_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


