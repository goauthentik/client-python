# PatchedSettingsRequestFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies_buffered_access_view** | **bool** |  | 

## Example

```python
from authentik_client.models.patched_settings_request_flags import PatchedSettingsRequestFlags

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSettingsRequestFlags from a JSON string
patched_settings_request_flags_instance = PatchedSettingsRequestFlags.from_json(json)
# print the JSON string representation of the object
print(PatchedSettingsRequestFlags.to_json())

# convert the object into a dict
patched_settings_request_flags_dict = patched_settings_request_flags_instance.to_dict()
# create an instance of PatchedSettingsRequestFlags from a dict
patched_settings_request_flags_from_dict = PatchedSettingsRequestFlags.from_dict(patched_settings_request_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


