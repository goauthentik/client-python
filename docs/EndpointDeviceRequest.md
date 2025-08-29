# EndpointDeviceRequest

Serializer for Endpoint authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**name** | **str** | The human-readable name of this device. | 

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


