# UpdateVersionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**changelog** | **str** |  | 
**changelog_url** | **str** |  | 
**reason** | [**UpdateVersionReason**](UpdateVersionReason.md) |  | 
**valid** | **bool** |  | [optional] [default to True]

## Example

```python
from authentik_client.models.update_version_info import UpdateVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVersionInfo from a JSON string
update_version_info_instance = UpdateVersionInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateVersionInfo.to_json())

# convert the object into a dict
update_version_info_dict = update_version_info_instance.to_dict()
# create an instance of UpdateVersionInfo from a dict
update_version_info_from_dict = UpdateVersionInfo.from_dict(update_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


