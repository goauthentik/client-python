# RACDevice

Device as it can be launched through a RAC provider. Deliberately does not include any connection settings, as this is also used by end-users launching a connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**protocols** | [**List[RACDeviceProtocol]**](RACDeviceProtocol.md) |  | [readonly] 
**override_pk** | **int** | Primary key of this device&#39;s connection override, if it has one | [readonly] 

## Example

```python
from authentik_client.models.rac_device import RACDevice

# TODO update the JSON string below
json = "{}"
# create an instance of RACDevice from a JSON string
rac_device_instance = RACDevice.from_json(json)
# print the JSON string representation of the object
print(RACDevice.to_json())

# convert the object into a dict
rac_device_dict = rac_device_instance.to_dict()
# create an instance of RACDevice from a dict
rac_device_from_dict = RACDevice.from_dict(rac_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


