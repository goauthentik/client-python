# SyncObjectResult

Result of a single object sync

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[LogEvent]**](LogEvent.md) |  | [readonly] 

## Example

```python
from authentik_client.models.sync_object_result import SyncObjectResult

# TODO update the JSON string below
json = "{}"
# create an instance of SyncObjectResult from a JSON string
sync_object_result_instance = SyncObjectResult.from_json(json)
# print the JSON string representation of the object
print(SyncObjectResult.to_json())

# convert the object into a dict
sync_object_result_dict = sync_object_result_instance.to_dict()
# create an instance of SyncObjectResult from a dict
sync_object_result_from_dict = SyncObjectResult.from_dict(sync_object_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


