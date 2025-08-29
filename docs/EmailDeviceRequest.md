# EmailDeviceRequest

Serializer for email authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_client.models.email_device_request import EmailDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDeviceRequest from a JSON string
email_device_request_instance = EmailDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(EmailDeviceRequest.to_json())

# convert the object into a dict
email_device_request_dict = email_device_request_instance.to_dict()
# create an instance of EmailDeviceRequest from a dict
email_device_request_from_dict = EmailDeviceRequest.from_dict(email_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


