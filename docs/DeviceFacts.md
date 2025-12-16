# DeviceFacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**disks** | [**List[Disk]**](Disk.md) |  | [optional] 
**network** | [**Network**](Network.md) |  | [optional] 
**hardware** | [**Hardware**](Hardware.md) |  | [optional] 
**software** | [**List[Software]**](Software.md) |  | [optional] 
**processes** | [**List[Process]**](Process.md) |  | [optional] 
**users** | [**List[DeviceUser]**](DeviceUser.md) |  | [optional] 
**groups** | [**List[DeviceGroup]**](DeviceGroup.md) |  | [optional] 
**vendor** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.device_facts import DeviceFacts

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFacts from a JSON string
device_facts_instance = DeviceFacts.from_json(json)
# print the JSON string representation of the object
print(DeviceFacts.to_json())

# convert the object into a dict
device_facts_dict = device_facts_instance.to_dict()
# create an instance of DeviceFacts from a dict
device_facts_from_dict = DeviceFacts.from_dict(device_facts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


