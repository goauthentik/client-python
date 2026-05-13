# BulkDeleteSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **int** |  | 

## Example

```python
from authentik_client.models.bulk_delete_session_response import BulkDeleteSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteSessionResponse from a JSON string
bulk_delete_session_response_instance = BulkDeleteSessionResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteSessionResponse.to_json())

# convert the object into a dict
bulk_delete_session_response_dict = bulk_delete_session_response_instance.to_dict()
# create an instance of BulkDeleteSessionResponse from a dict
bulk_delete_session_response_from_dict = BulkDeleteSessionResponse.from_dict(bulk_delete_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


