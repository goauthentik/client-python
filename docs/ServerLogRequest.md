# ServerLogRequest

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from authentik_client.models.server_log_request import ServerLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerLogRequest from a JSON string
server_log_request_instance = ServerLogRequest.from_json(json)
# print the JSON string representation of the object
print(ServerLogRequest.to_json())

# convert the object into a dict
server_log_request_dict = server_log_request_instance.to_dict()
# create an instance of ServerLogRequest from a dict
server_log_request_from_dict = ServerLogRequest.from_dict(server_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


