# EmailDevice

Serializer for email authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 
**pk** | **int** |  | [readonly] 
**email** | **str** |  | [readonly] 
**user** | [**GroupMember**](GroupMember.md) |  | [readonly] 

## Example

```python
from authentik_client.models.email_device import EmailDevice

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDevice from a JSON string
email_device_instance = EmailDevice.from_json(json)
# print the JSON string representation of the object
print(EmailDevice.to_json())

# convert the object into a dict
email_device_dict = email_device_instance.to_dict()
# create an instance of EmailDevice from a dict
email_device_from_dict = EmailDevice.from_dict(email_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


