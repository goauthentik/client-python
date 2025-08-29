# VersionHistory

VersionHistory Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**timestamp** | **datetime** |  | 
**version** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from authentik_client.models.version_history import VersionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of VersionHistory from a JSON string
version_history_instance = VersionHistory.from_json(json)
# print the JSON string representation of the object
print(VersionHistory.to_json())

# convert the object into a dict
version_history_dict = version_history_instance.to_dict()
# create an instance of VersionHistory from a dict
version_history_from_dict = VersionHistory.from_dict(version_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


