# GroupSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**source** | **str** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_source_connection_request import GroupSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSourceConnectionRequest from a JSON string
group_source_connection_request_instance = GroupSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupSourceConnectionRequest.to_json())

# convert the object into a dict
group_source_connection_request_dict = group_source_connection_request_instance.to_dict()
# create an instance of GroupSourceConnectionRequest from a dict
group_source_connection_request_from_dict = GroupSourceConnectionRequest.from_dict(group_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


