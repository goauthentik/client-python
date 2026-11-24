# PatchedEmailDeviceRequest

Serializer for email authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | [optional] 

## Example

```python
from authentik_client.models.patched_email_device_request import PatchedEmailDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEmailDeviceRequest from a JSON string
patched_email_device_request_instance = PatchedEmailDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEmailDeviceRequest.to_json())

# convert the object into a dict
patched_email_device_request_dict = patched_email_device_request_instance.to_dict()
# create an instance of PatchedEmailDeviceRequest from a dict
patched_email_device_request_from_dict = PatchedEmailDeviceRequest.from_dict(patched_email_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


