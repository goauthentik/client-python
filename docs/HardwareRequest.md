# HardwareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**serial** | **str** |  | 
**cpu_name** | **str** |  | [optional] 
**cpu_count** | **int** |  | [optional] 
**memory_bytes** | **int** |  | [optional] 

## Example

```python
from authentik_client.models.hardware_request import HardwareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareRequest from a JSON string
hardware_request_instance = HardwareRequest.from_json(json)
# print the JSON string representation of the object
print(HardwareRequest.to_json())

# convert the object into a dict
hardware_request_dict = hardware_request_instance.to_dict()
# create an instance of HardwareRequest from a dict
hardware_request_from_dict = HardwareRequest.from_dict(hardware_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


