# GroupPlexSourceConnection

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**group** | **str** |  | 
**source** | **str** |  | 
**source_obj** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 
**created** | **datetime** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.group_plex_source_connection import GroupPlexSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPlexSourceConnection from a JSON string
group_plex_source_connection_instance = GroupPlexSourceConnection.from_json(json)
# print the JSON string representation of the object
print(GroupPlexSourceConnection.to_json())

# convert the object into a dict
group_plex_source_connection_dict = group_plex_source_connection_instance.to_dict()
# create an instance of GroupPlexSourceConnection from a dict
group_plex_source_connection_from_dict = GroupPlexSourceConnection.from_dict(group_plex_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


