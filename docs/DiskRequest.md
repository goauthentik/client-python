# DiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mountpoint** | **str** |  | 
**label** | **str** |  | [optional] 
**capacity_total_bytes** | **int** |  | [optional] 
**capacity_used_bytes** | **int** |  | [optional] 
**encryption_enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from authentik_client.models.disk_request import DiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiskRequest from a JSON string
disk_request_instance = DiskRequest.from_json(json)
# print the JSON string representation of the object
print(DiskRequest.to_json())

# convert the object into a dict
disk_request_dict = disk_request_instance.to_dict()
# create an instance of DiskRequest from a dict
disk_request_from_dict = DiskRequest.from_dict(disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


