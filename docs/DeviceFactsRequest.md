# DeviceFactsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os** | [**OperatingSystemRequest**](OperatingSystemRequest.md) |  | [optional] 
**disks** | [**List[DiskRequest]**](DiskRequest.md) |  | [optional] 
**network** | [**NetworkRequest**](NetworkRequest.md) |  | [optional] 
**hardware** | [**HardwareRequest**](HardwareRequest.md) |  | [optional] 
**software** | [**List[SoftwareRequest]**](SoftwareRequest.md) |  | [optional] 
**processes** | [**List[ProcessRequest]**](ProcessRequest.md) |  | [optional] 
**users** | [**List[DeviceUserRequest]**](DeviceUserRequest.md) |  | [optional] 
**groups** | [**List[DeviceGroupRequest]**](DeviceGroupRequest.md) |  | [optional] 
**vendor** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.device_facts_request import DeviceFactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFactsRequest from a JSON string
device_facts_request_instance = DeviceFactsRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceFactsRequest.to_json())

# convert the object into a dict
device_facts_request_dict = device_facts_request_instance.to_dict()
# create an instance of DeviceFactsRequest from a dict
device_facts_request_from_dict = DeviceFactsRequest.from_dict(device_facts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


