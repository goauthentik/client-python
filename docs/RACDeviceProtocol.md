# RACDeviceProtocol

A protocol a device can be connected to with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** |  | 
**launch_url** | **str** |  | 

## Example

```python
from authentik_client.models.rac_device_protocol import RACDeviceProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of RACDeviceProtocol from a JSON string
rac_device_protocol_instance = RACDeviceProtocol.from_json(json)
# print the JSON string representation of the object
print(RACDeviceProtocol.to_json())

# convert the object into a dict
rac_device_protocol_dict = rac_device_protocol_instance.to_dict()
# create an instance of RACDeviceProtocol from a dict
rac_device_protocol_from_dict = RACDeviceProtocol.from_dict(rac_device_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


