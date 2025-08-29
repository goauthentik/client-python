# PatchedUserSourceConnectionRequest

User source connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_user_source_connection_request import PatchedUserSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserSourceConnectionRequest from a JSON string
patched_user_source_connection_request_instance = PatchedUserSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserSourceConnectionRequest.to_json())

# convert the object into a dict
patched_user_source_connection_request_dict = patched_user_source_connection_request_instance.to_dict()
# create an instance of PatchedUserSourceConnectionRequest from a dict
patched_user_source_connection_request_from_dict = PatchedUserSourceConnectionRequest.from_dict(patched_user_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


