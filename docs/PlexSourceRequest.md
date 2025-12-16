# PlexSourceRequest

Plex Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**promoted** | **bool** | When enabled, this source will be displayed as a prominent button on the login page, instead of a small icon. | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**group_matching_mode** | [**GroupMatchingModeEnum**](GroupMatchingModeEnum.md) | How the source determines if an existing group should be used or a new group created. | [optional] 
**client_id** | **str** | Client identifier used to talk to Plex. | [optional] 
**allowed_servers** | **List[str]** | Which servers a user has to be a member of to be granted access. Empty list allows every server. | [optional] 
**allow_friends** | **bool** | Allow friends to authenticate, even if you don&#39;t share a server. | [optional] 
**plex_token** | **str** | Plex token used to check friends | 

## Example

```python
from authentik_client.models.plex_source_request import PlexSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlexSourceRequest from a JSON string
plex_source_request_instance = PlexSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PlexSourceRequest.to_json())

# convert the object into a dict
plex_source_request_dict = plex_source_request_instance.to_dict()
# create an instance of PlexSourceRequest from a dict
plex_source_request_from_dict = PlexSourceRequest.from_dict(plex_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


