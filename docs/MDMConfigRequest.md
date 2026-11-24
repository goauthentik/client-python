# MDMConfigRequest

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | [**DeviceFactsOSFamily**](DeviceFactsOSFamily.md) |  | 
**enrollment_token** | **UUID** |  | 

## Example

```python
from authentik_client.models.mdm_config_request import MDMConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MDMConfigRequest from a JSON string
mdm_config_request_instance = MDMConfigRequest.from_json(json)
# print the JSON string representation of the object
print(MDMConfigRequest.to_json())

# convert the object into a dict
mdm_config_request_dict = mdm_config_request_instance.to_dict()
# create an instance of MDMConfigRequest from a dict
mdm_config_request_from_dict = MDMConfigRequest.from_dict(mdm_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


