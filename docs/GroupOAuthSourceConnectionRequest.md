# GroupOAuthSourceConnectionRequest

OAuth Group-Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**source** | **str** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_o_auth_source_connection_request import GroupOAuthSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupOAuthSourceConnectionRequest from a JSON string
group_o_auth_source_connection_request_instance = GroupOAuthSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupOAuthSourceConnectionRequest.to_json())

# convert the object into a dict
group_o_auth_source_connection_request_dict = group_o_auth_source_connection_request_instance.to_dict()
# create an instance of GroupOAuthSourceConnectionRequest from a dict
group_o_auth_source_connection_request_from_dict = GroupOAuthSourceConnectionRequest.from_dict(group_o_auth_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


