# PatchedGroupOAuthSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **UUID** |  | [optional] 
**source** | **UUID** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_group_o_auth_source_connection_request import PatchedGroupOAuthSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGroupOAuthSourceConnectionRequest from a JSON string
patched_group_o_auth_source_connection_request_instance = PatchedGroupOAuthSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGroupOAuthSourceConnectionRequest.to_json())

# convert the object into a dict
patched_group_o_auth_source_connection_request_dict = patched_group_o_auth_source_connection_request_instance.to_dict()
# create an instance of PatchedGroupOAuthSourceConnectionRequest from a dict
patched_group_o_auth_source_connection_request_from_dict = PatchedGroupOAuthSourceConnectionRequest.from_dict(patched_group_o_auth_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


