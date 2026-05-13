# GroupSourceConnection

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**group** | **UUID** |  | 
**source** | **UUID** |  | 
**source_obj** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 
**created** | **datetime** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.group_source_connection import GroupSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSourceConnection from a JSON string
group_source_connection_instance = GroupSourceConnection.from_json(json)
# print the JSON string representation of the object
print(GroupSourceConnection.to_json())

# convert the object into a dict
group_source_connection_dict = group_source_connection_instance.to_dict()
# create an instance of GroupSourceConnection from a dict
group_source_connection_from_dict = GroupSourceConnection.from_dict(group_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


