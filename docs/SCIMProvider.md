# SCIMProvider

SCIMProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**assigned_backchannel_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_backchannel_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**url** | **str** | Base URL to SCIM requests, usually ends in /v2 | 
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
from authentik_client.models.scim_provider import SCIMProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMProvider from a JSON string
scim_provider_instance = SCIMProvider.from_json(json)
# print the JSON string representation of the object
print(SCIMProvider.to_json())

# convert the object into a dict
scim_provider_dict = scim_provider_instance.to_dict()
# create an instance of SCIMProvider from a dict
scim_provider_from_dict = SCIMProvider.from_dict(scim_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


