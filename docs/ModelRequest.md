# ModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**property_mappings** | **List[UUID]** |  | [optional] 
**property_mappings_group** | **List[UUID]** | Property mappings used for group creation/updating. | [optional] 
**delegated_subject** | **str** |  | 
**credentials** | **Dict[str, object]** |  | 
**scopes** | **str** |  | [optional] 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **UUID** |  | [optional] 
**user_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**group_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**default_group_email_domain** | **str** |  | 
**sync_page_size** | **int** | Controls the number of objects synced in a single task | [optional] 
**sync_page_timeout** | **str** | Timeout for synchronization of a single page | [optional] 
**dry_run** | **bool** | When enabled, provider will not modify or create objects in the remote system. | [optional] 
**authentication_flow** | **UUID** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **UUID** | Flow used when authorizing this provider. | 
**invalidation_flow** | **UUID** | Flow used ending the session from a provider. | 
**base_dn** | **str** | DN under which objects are accessible. | [optional] 
**certificate** | **UUID** |  | [optional] 
**tls_server_name** | **str** |  | [optional] 
**uid_start_number** | **int** | The start for uidNumbers, this number is added to the user.pk to make sure that the numbers aren&#39;t too low for POSIX users. Default is 2000 to ensure that we don&#39;t collide with local users uidNumber | [optional] 
**gid_start_number** | **int** | The start for gidNumbers, this number is added to a number generated from the group.pk to make sure that the numbers aren&#39;t too low for POSIX groups. Default is 4000 to ensure that we don&#39;t collide with local groups or users primary groups gidNumber | [optional] 
**search_mode** | [**LDAPAPIAccessMode**](LDAPAPIAccessMode.md) |  | [optional] 
**bind_mode** | [**LDAPAPIAccessMode**](LDAPAPIAccessMode.md) |  | [optional] 
**mfa_support** | **bool** | When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon. | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**tenant_id** | **str** |  | 
**client_type** | [**ClientTypeEnum**](ClientTypeEnum.md) | Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable | [optional] 
**access_code_validity** | **str** | Access codes not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**access_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_threshold** | **str** | When refreshing a token, if the refresh token is valid for less than this duration, it will be renewed. When set to seconds&#x3D;0, token will always be renewed. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**include_claims_in_id_token** | **bool** | Include User claims from scopes in the id_token, for applications that don&#39;t access the userinfo endpoint. | [optional] 
**signing_key** | **UUID** | Key used to sign the SSF Events. | 
**encryption_key** | **UUID** | Key used to encrypt the tokens. When set, tokens will be encrypted and returned as JWEs. | [optional] 
**redirect_uris** | [**List[RedirectURIRequest]**](RedirectURIRequest.md) |  | 
**logout_uri** | **str** |  | [optional] 
**logout_method** | [**SAMLLogoutMethods**](SAMLLogoutMethods.md) | Method to use for logout. Front-channel iframe loads all logout URLs simultaneously in hidden iframes. Front-channel native uses your active browser tab to send post requests and redirect to providers. Back-channel sends logout requests directly from the server without user interaction (requires POST SLS binding). | [optional] 
**sub_mode** | [**SubModeEnum**](SubModeEnum.md) | Configure what data should be used as unique User Identifier. For most cases, the default should be fine. | [optional] 
**issuer_mode** | [**IssuerModeEnum**](IssuerModeEnum.md) | Configure how the issuer field of the ID Token should be filled. | [optional] 
**jwt_federation_sources** | **List[UUID]** |  | [optional] 
**jwt_federation_providers** | **List[int]** |  | [optional] 
**internal_host** | **str** |  | [optional] 
**external_host** | **str** |  | 
**internal_host_ssl_validation** | **bool** | Validate SSL Certificates of upstream servers | [optional] 
**skip_path_regex** | **str** | Regular expressions for which authentication is not required. Each new line is interpreted as a new Regular Expression. | [optional] 
**basic_auth_enabled** | **bool** | Set a custom HTTP-Basic Authentication header based on values from authentik. | [optional] 
**basic_auth_password_attribute** | **str** | User/Group Attribute used for the password part of the HTTP-Basic Header. | [optional] 
**basic_auth_user_attribute** | **str** | User/Group Attribute used for the user part of the HTTP-Basic Header. If not set, the user&#39;s Email address is used. | [optional] 
**mode** | [**ProxyMode**](ProxyMode.md) | Enable support for forwardAuth in traefik and nginx auth_request. Exclusive with internal_host. | [optional] 
**intercept_header_auth** | **bool** | When enabled, this provider will intercept the authorization header and authenticate requests based on its value. | [optional] 
**cookie_domain** | **str** |  | [optional] 
**settings** | **Dict[str, object]** |  | [optional] 
**connection_expiry** | **str** | Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 
**delete_token_on_disconnect** | **bool** | When set to true, connection tokens will be deleted upon disconnect. | [optional] 
**client_networks** | **str** | List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped. | [optional] 
**shared_secret** | **str** | Shared secret between clients and server to hash packets. | [optional] 
**acs_url** | **str** |  | 
**sls_url** | **str** | Single Logout Service URL where the logout response should be sent. | [optional] 
**audience** | **str** | Value of the audience restriction field of the assertion. When left empty, no audience restriction will be added. | [optional] 
**issuer** | **str** | Also known as EntityID | [optional] 
**assertion_valid_not_before** | **str** | Assertion valid not before current time + this value (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3). | [optional] 
**assertion_valid_not_on_or_after** | **str** | Assertion not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**session_valid_not_on_or_after** | **str** | Session not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**name_id_mapping** | **UUID** | Configure how the NameID value will be created. When left empty, the NameIDPolicy of the incoming request will be considered | [optional] 
**authn_context_class_ref_mapping** | **UUID** | Configure how the AuthnContextClassRef value will be created. When left empty, the AuthnContextClassRef will be set based on which authentication methods the user used to authenticate. | [optional] 
**digest_algorithm** | [**DigestAlgorithmEnum**](DigestAlgorithmEnum.md) |  | [optional] 
**signature_algorithm** | [**SignatureAlgorithmEnum**](SignatureAlgorithmEnum.md) |  | [optional] 
**signing_kp** | **UUID** | Keypair used to sign outgoing Responses going to the Service Provider. | [optional] 
**verification_kp** | **UUID** | When selected, incoming assertion&#39;s Signatures will be validated against this certificate. To allow unsigned Requests, leave on default. | [optional] 
**encryption_kp** | **UUID** | When selected, incoming assertions are encrypted by the IdP using the public key of the encryption keypair. The assertion is decrypted by the SP using the the private key. | [optional] 
**sign_assertion** | **bool** |  | [optional] 
**sign_response** | **bool** |  | [optional] 
**sign_logout_request** | **bool** |  | [optional] 
**sp_binding** | [**SAMLBindingsEnum**](SAMLBindingsEnum.md) | This determines how authentik sends the response back to the Service Provider. | [optional] 
**sls_binding** | [**SAMLBindingsEnum**](SAMLBindingsEnum.md) | This determines how authentik sends the logout response back to the Service Provider. | [optional] 
**default_relay_state** | **str** | Default relay_state value for IDP-initiated logins | [optional] 
**default_name_id_policy** | [**SAMLNameIDPolicyEnum**](SAMLNameIDPolicyEnum.md) |  | [optional] 
**url** | **str** | Base URL to SCIM requests, usually ends in /v2 | 
**verify_certificates** | **bool** |  | [optional] 
**token** | **str** | Authentication token | [optional] 
**auth_mode** | [**SCIMAuthenticationModeEnum**](SCIMAuthenticationModeEnum.md) |  | [optional] 
**auth_oauth** | **UUID** | OAuth Source used for authentication | [optional] 
**auth_oauth_params** | **Dict[str, object]** | Additional OAuth parameters, such as grant_type | [optional] 
**compatibility_mode** | [**CompatibilityModeEnum**](CompatibilityModeEnum.md) | Alter authentik behavior for vendor-specific SCIM implementations. | [optional] 
**service_provider_config_cache_timeout** | **str** | Cache duration for ServiceProviderConfig responses. Set minutes&#x3D;0 to disable. | [optional] 
**group_filters** | **List[UUID]** | Group filters used to define sync-scope for groups. | [optional] 
**oidc_auth_providers** | **List[int]** |  | [optional] 
**event_retention** | **str** |  | [optional] 
**reply_url** | **str** |  | 

## Example

```python
from authentik_client.models.model_request import ModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelRequest from a JSON string
model_request_instance = ModelRequest.from_json(json)
# print the JSON string representation of the object
print(ModelRequest.to_json())

# convert the object into a dict
model_request_dict = model_request_instance.to_dict()
# create an instance of ModelRequest from a dict
model_request_from_dict = ModelRequest.from_dict(model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


