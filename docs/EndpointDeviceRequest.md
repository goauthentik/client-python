# EndpointDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**access_group** | **UUID** |  | [optional] 
**access_group_obj** | [**DeviceAccessGroupRequest**](DeviceAccessGroupRequest.md) |  | [optional] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.endpoint_device_request import EndpointDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDeviceRequest from a JSON string
endpoint_device_request_instance = EndpointDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointDeviceRequest.to_json())

# convert the object into a dict
endpoint_device_request_dict = endpoint_device_request_instance.to_dict()
# create an instance of EndpointDeviceRequest from a dict
endpoint_device_request_from_dict = EndpointDeviceRequest.from_dict(endpoint_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


