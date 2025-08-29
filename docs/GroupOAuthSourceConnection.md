# GroupOAuthSourceConnection

OAuth Group-Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**group** | **str** |  | 
**source** | **str** |  | 
**source_obj** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 
**created** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.group_o_auth_source_connection import GroupOAuthSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GroupOAuthSourceConnection from a JSON string
group_o_auth_source_connection_instance = GroupOAuthSourceConnection.from_json(json)
# print the JSON string representation of the object
print(GroupOAuthSourceConnection.to_json())

# convert the object into a dict
group_o_auth_source_connection_dict = group_o_auth_source_connection_instance.to_dict()
# create an instance of GroupOAuthSourceConnection from a dict
group_o_auth_source_connection_from_dict = GroupOAuthSourceConnection.from_dict(group_o_auth_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


