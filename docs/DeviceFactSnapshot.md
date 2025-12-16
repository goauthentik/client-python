# DeviceFactSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeviceFacts**](DeviceFacts.md) |  | 
**connection** | **str** |  | 
**created** | **datetime** |  | [readonly] 
**expires** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.device_fact_snapshot import DeviceFactSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFactSnapshot from a JSON string
device_fact_snapshot_instance = DeviceFactSnapshot.from_json(json)
# print the JSON string representation of the object
print(DeviceFactSnapshot.to_json())

# convert the object into a dict
device_fact_snapshot_dict = device_fact_snapshot_instance.to_dict()
# create an instance of DeviceFactSnapshot from a dict
device_fact_snapshot_from_dict = DeviceFactSnapshot.from_dict(device_fact_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


