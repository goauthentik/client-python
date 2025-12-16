# DeviceUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**home** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.device_user import DeviceUser

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUser from a JSON string
device_user_instance = DeviceUser.from_json(json)
# print the JSON string representation of the object
print(DeviceUser.to_json())

# convert the object into a dict
device_user_dict = device_user_instance.to_dict()
# create an instance of DeviceUser from a dict
device_user_from_dict = DeviceUser.from_dict(device_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


