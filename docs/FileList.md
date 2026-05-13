# FileList

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mime_type** | **str** |  | 
**url** | **str** |  | 
**themed_urls** | [**ThemedUrls**](ThemedUrls.md) |  | [optional] 

## Example

```python
from authentik_client.models.file_list import FileList

# TODO update the JSON string below
json = "{}"
# create an instance of FileList from a JSON string
file_list_instance = FileList.from_json(json)
# print the JSON string representation of the object
print(FileList.to_json())

# convert the object into a dict
file_list_dict = file_list_instance.to_dict()
# create an instance of FileList from a dict
file_list_from_dict = FileList.from_dict(file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


