# UserSourceConnectionRequest

User source connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**source** | **str** |  | 

## Example

```python
from authentik_client.models.user_source_connection_request import UserSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSourceConnectionRequest from a JSON string
user_source_connection_request_instance = UserSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserSourceConnectionRequest.to_json())

# convert the object into a dict
user_source_connection_request_dict = user_source_connection_request_instance.to_dict()
# create an instance of UserSourceConnectionRequest from a dict
user_source_connection_request_from_dict = UserSourceConnectionRequest.from_dict(user_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


