# PatchedSettingsRequestFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_default_app_access** | **bool** | Configure if applications without any policy/group/user bindings should be accessible to any user. | 
**enterprise_audit_include_expanded_diff** | **bool** | Include additional information in audit logs, may incur a performance penalty. | 
**flows_continuous_login** | **bool** | Upon successful authentication, re-start authentication in other open tabs. | 
**flows_refresh_others** | **bool** | Refresh other tabs after successful authentication. | 

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


