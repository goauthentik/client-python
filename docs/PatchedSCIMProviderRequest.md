# PatchedSCIMProviderRequest

SCIMProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**url** | **str** | Base URL to SCIM requests, usually ends in /v2 | [optional] 
**verify_certificates** | **bool** |  | [optional] 
**token** | **str** | Authentication token | [optional] 
**auth_mode** | [**SCIMAuthenticationModeEnum**](SCIMAuthenticationModeEnum.md) |  | [optional] 
**auth_oauth** | **str** | OAuth Source used for authentication | [optional] 
**auth_oauth_params** | **Dict[str, object]** | Additional OAuth parameters, such as grant_type | [optional] 
**compatibility_mode** | [**CompatibilityModeEnum**](CompatibilityModeEnum.md) | Alter authentik behavior for vendor-specific SCIM implementations. | [optional] 
**service_provider_config_cache_timeout** | **str** | Cache duration for ServiceProviderConfig responses. Set minutes&#x3D;0 to disable. | [optional] 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 
**sync_page_size** | **int** | Controls the number of objects synced in a single task | [optional] 
**sync_page_timeout** | **str** | Timeout for synchronization of a single page | [optional] 
**dry_run** | **bool** | When enabled, provider will not modify or create objects in the remote system. | [optional] 

## Example

```python
from authentik_client.models.patched_scim_provider_request import PatchedSCIMProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMProviderRequest from a JSON string
patched_scim_provider_request_instance = PatchedSCIMProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMProviderRequest.to_json())

# convert the object into a dict
patched_scim_provider_request_dict = patched_scim_provider_request_instance.to_dict()
# create an instance of PatchedSCIMProviderRequest from a dict
patched_scim_provider_request_from_dict = PatchedSCIMProviderRequest.from_dict(patched_scim_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


