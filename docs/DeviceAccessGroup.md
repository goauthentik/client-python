# DeviceAccessGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pbm_uuid** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.device_access_group import DeviceAccessGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAccessGroup from a JSON string
device_access_group_instance = DeviceAccessGroup.from_json(json)
# print the JSON string representation of the object
print(DeviceAccessGroup.to_json())

# convert the object into a dict
device_access_group_dict = device_access_group_instance.to_dict()
# create an instance of DeviceAccessGroup from a dict
device_access_group_from_dict = DeviceAccessGroup.from_dict(device_access_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


