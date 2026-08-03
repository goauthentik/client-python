# MDMConfigResponse

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** |  | 
**mime_type** | **str** |  | 
**filename** | **str** |  | 

## Example

```python
from authentik_client.models.mdm_config_response import MDMConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MDMConfigResponse from a JSON string
mdm_config_response_instance = MDMConfigResponse.from_json(json)
# print the JSON string representation of the object
print(MDMConfigResponse.to_json())

# convert the object into a dict
mdm_config_response_dict = mdm_config_response_instance.to_dict()
# create an instance of MDMConfigResponse from a dict
mdm_config_response_from_dict = MDMConfigResponse.from_dict(mdm_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


