# UserPlexSourceConnectionRequest

User source connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**source** | **UUID** |  | 
**identifier** | **str** |  | 
**plex_token** | **str** |  | 

## Example

```python
from authentik_client.models.user_plex_source_connection_request import UserPlexSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlexSourceConnectionRequest from a JSON string
user_plex_source_connection_request_instance = UserPlexSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserPlexSourceConnectionRequest.to_json())

# convert the object into a dict
user_plex_source_connection_request_dict = user_plex_source_connection_request_instance.to_dict()
# create an instance of UserPlexSourceConnectionRequest from a dict
user_plex_source_connection_request_from_dict = UserPlexSourceConnectionRequest.from_dict(user_plex_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


