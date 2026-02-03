# PatchedGoogleEndpointDeviceRequest

Serializer for Endpoint authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [optional] 
**name** | **str** | The human-readable name of this device. | [optional] 

## Example

```python
from authentik_client.models.patched_google_endpoint_device_request import PatchedGoogleEndpointDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGoogleEndpointDeviceRequest from a JSON string
patched_google_endpoint_device_request_instance = PatchedGoogleEndpointDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGoogleEndpointDeviceRequest.to_json())

# convert the object into a dict
patched_google_endpoint_device_request_dict = patched_google_endpoint_device_request_instance.to_dict()
# create an instance of PatchedGoogleEndpointDeviceRequest from a dict
patched_google_endpoint_device_request_from_dict = PatchedGoogleEndpointDeviceRequest.from_dict(patched_google_endpoint_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


