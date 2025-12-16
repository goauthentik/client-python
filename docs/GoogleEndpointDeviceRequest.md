# GoogleEndpointDeviceRequest

Serializer for Endpoint authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_client.models.google_endpoint_device_request import GoogleEndpointDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleEndpointDeviceRequest from a JSON string
google_endpoint_device_request_instance = GoogleEndpointDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleEndpointDeviceRequest.to_json())

# convert the object into a dict
google_endpoint_device_request_dict = google_endpoint_device_request_instance.to_dict()
# create an instance of GoogleEndpointDeviceRequest from a dict
google_endpoint_device_request_from_dict = GoogleEndpointDeviceRequest.from_dict(google_endpoint_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


