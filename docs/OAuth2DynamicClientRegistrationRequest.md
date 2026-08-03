# OAuth2DynamicClientRegistrationRequest

Serializer for OAuth2DynamicClientRegistration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **int** |  | 
**default_application_group** | **str** | Group to assign to automatically created applications. | [optional] 
**override_authorization_flow** | **UUID** | Authorization flow applied to dynamically registered clients. | [optional] 
**override_invalidation_flow** | **UUID** |  | [optional] 
**override_property_mappings** | **List[UUID]** | Scope mappings applied to dynamically registered clients. | [optional] 
**access_token_validity** | **str** | Maximum access token validity for registered clients (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_validity** | **str** | Maximum refresh token validity for registered clients (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**allowed_grant_types** | [**List[GrantTypeEnum]**](GrantTypeEnum.md) | If empty, all grant types are allowed. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 

## Example

```python
from authentik_client.models.o_auth2_dynamic_client_registration_request import OAuth2DynamicClientRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2DynamicClientRegistrationRequest from a JSON string
o_auth2_dynamic_client_registration_request_instance = OAuth2DynamicClientRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(OAuth2DynamicClientRegistrationRequest.to_json())

# convert the object into a dict
o_auth2_dynamic_client_registration_request_dict = o_auth2_dynamic_client_registration_request_instance.to_dict()
# create an instance of OAuth2DynamicClientRegistrationRequest from a dict
o_auth2_dynamic_client_registration_request_from_dict = OAuth2DynamicClientRegistrationRequest.from_dict(o_auth2_dynamic_client_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


