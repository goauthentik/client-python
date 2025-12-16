# GoogleEndpointDevice

Serializer for Endpoint authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_client.models.google_endpoint_device import GoogleEndpointDevice

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleEndpointDevice from a JSON string
google_endpoint_device_instance = GoogleEndpointDevice.from_json(json)
# print the JSON string representation of the object
print(GoogleEndpointDevice.to_json())

# convert the object into a dict
google_endpoint_device_dict = google_endpoint_device_instance.to_dict()
# create an instance of GoogleEndpointDevice from a dict
google_endpoint_device_from_dict = GoogleEndpointDevice.from_dict(google_endpoint_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


