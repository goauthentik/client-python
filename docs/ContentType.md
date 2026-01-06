# ContentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**app_label** | **str** |  | [readonly] 
**model** | **str** |  | [readonly] 
**verbose_name_plural** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.content_type import ContentType

# TODO update the JSON string below
json = "{}"
# create an instance of ContentType from a JSON string
content_type_instance = ContentType.from_json(json)
# print the JSON string representation of the object
print(ContentType.to_json())

# convert the object into a dict
content_type_dict = content_type_instance.to_dict()
# create an instance of ContentType from a dict
content_type_from_dict = ContentType.from_dict(content_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


