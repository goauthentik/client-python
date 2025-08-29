# PatchedUserPlexSourceConnectionRequest

Plex Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**source** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**plex_token** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_user_plex_source_connection_request import PatchedUserPlexSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserPlexSourceConnectionRequest from a JSON string
patched_user_plex_source_connection_request_instance = PatchedUserPlexSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserPlexSourceConnectionRequest.to_json())

# convert the object into a dict
patched_user_plex_source_connection_request_dict = patched_user_plex_source_connection_request_instance.to_dict()
# create an instance of PatchedUserPlexSourceConnectionRequest from a dict
patched_user_plex_source_connection_request_from_dict = PatchedUserPlexSourceConnectionRequest.from_dict(patched_user_plex_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


