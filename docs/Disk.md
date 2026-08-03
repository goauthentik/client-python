# Disk


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
from authentik_client.models.disk import Disk

# TODO update the JSON string below
json = "{}"
# create an instance of Disk from a JSON string
disk_instance = Disk.from_json(json)
# print the JSON string representation of the object
print(Disk.to_json())

# convert the object into a dict
disk_dict = disk_instance.to_dict()
# create an instance of Disk from a dict
disk_from_dict = Disk.from_dict(disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


