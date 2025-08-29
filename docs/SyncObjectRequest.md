# SyncObjectRequest

Sync object serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_object_model** | [**SyncObjectModelEnum**](SyncObjectModelEnum.md) |  | 
**sync_object_id** | **str** |  | 

## Example

```python
from authentik_client.models.sync_object_request import SyncObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncObjectRequest from a JSON string
sync_object_request_instance = SyncObjectRequest.from_json(json)
# print the JSON string representation of the object
print(SyncObjectRequest.to_json())

# convert the object into a dict
sync_object_request_dict = sync_object_request_instance.to_dict()
# create an instance of SyncObjectRequest from a dict
sync_object_request_from_dict = SyncObjectRequest.from_dict(sync_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


