# OAuthSourceRequest

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**group_matching_mode** | [**GroupMatchingModeEnum**](GroupMatchingModeEnum.md) | How the source determines if an existing group should be used or a new group created. | [optional] 
**provider_type** | [**ProviderTypeEnum**](ProviderTypeEnum.md) |  | 
**request_token_url** | **str** | URL used to request the initial token. This URL is only required for OAuth 1. | [optional] 
**authorization_url** | **str** | URL the user is redirect to to conest the flow. | [optional] 
**access_token_url** | **str** | URL used by authentik to retrieve tokens. | [optional] 
**profile_url** | **str** | URL used by authentik to get user information. | [optional] 
**pkce** | [**PKCEMethodEnum**](PKCEMethodEnum.md) |  | [optional] 
**consumer_key** | **str** |  | 
**consumer_secret** | **str** |  | 
**additional_scopes** | **str** |  | [optional] 
**oidc_well_known_url** | **str** |  | [optional] 
**oidc_jwks_url** | **str** |  | [optional] 
**oidc_jwks** | **Dict[str, object]** |  | [optional] 
**authorization_code_auth_method** | [**AuthorizationCodeAuthMethodEnum**](AuthorizationCodeAuthMethodEnum.md) | How to perform authentication during an authorization_code token request flow | [optional] 

## Example

```python
from authentik_client.models.o_auth_source_request import OAuthSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthSourceRequest from a JSON string
o_auth_source_request_instance = OAuthSourceRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthSourceRequest.to_json())

# convert the object into a dict
o_auth_source_request_dict = o_auth_source_request_instance.to_dict()
# create an instance of OAuthSourceRequest from a dict
o_auth_source_request_from_dict = OAuthSourceRequest.from_dict(o_auth_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


