# GroupPlexSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **UUID** |  | 
**source** | **UUID** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_plex_source_connection_request import GroupPlexSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPlexSourceConnectionRequest from a JSON string
group_plex_source_connection_request_instance = GroupPlexSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupPlexSourceConnectionRequest.to_json())

# convert the object into a dict
group_plex_source_connection_request_dict = group_plex_source_connection_request_instance.to_dict()
# create an instance of GroupPlexSourceConnectionRequest from a dict
group_plex_source_connection_request_from_dict = GroupPlexSourceConnectionRequest.from_dict(group_plex_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


