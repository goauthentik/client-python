# RadiusProviderRequest

RadiusProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**authentication_flow** | **UUID** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **UUID** | Flow used when authorizing this provider. | 
**invalidation_flow** | **UUID** | Flow used ending the session from a provider. | 
**property_mappings** | **List[UUID]** |  | [optional] 
**client_networks** | **str** | List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped. | [optional] 
**shared_secret** | **str** | Shared secret between clients and server to hash packets. | [optional] 
**mfa_support** | **bool** | When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon. | [optional] 
**certificate** | **UUID** |  | [optional] 

## Example

```python
from authentik_client.models.radius_provider_request import RadiusProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusProviderRequest from a JSON string
radius_provider_request_instance = RadiusProviderRequest.from_json(json)
# print the JSON string representation of the object
print(RadiusProviderRequest.to_json())

# convert the object into a dict
radius_provider_request_dict = radius_provider_request_instance.to_dict()
# create an instance of RadiusProviderRequest from a dict
radius_provider_request_from_dict = RadiusProviderRequest.from_dict(radius_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


