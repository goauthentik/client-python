# EndpointDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **UUID** |  | [optional] 
**pbm_uuid** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**access_group** | **UUID** |  | [optional] 
**access_group_obj** | [**DeviceAccessGroup**](DeviceAccessGroup.md) |  | [optional] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**facts** | [**DeviceFactSnapshot**](DeviceFactSnapshot.md) |  | [readonly] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.endpoint_device import EndpointDevice

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDevice from a JSON string
endpoint_device_instance = EndpointDevice.from_json(json)
# print the JSON string representation of the object
print(EndpointDevice.to_json())

# convert the object into a dict
endpoint_device_dict = endpoint_device_instance.to_dict()
# create an instance of EndpointDevice from a dict
endpoint_device_from_dict = EndpointDevice.from_dict(endpoint_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


