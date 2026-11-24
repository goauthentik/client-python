# ThemedUrls

Themed URLs - maps theme names to URLs for light and dark themes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **str** |  | [optional] 
**dark** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.themed_urls import ThemedUrls

# TODO update the JSON string below
json = "{}"
# create an instance of ThemedUrls from a JSON string
themed_urls_instance = ThemedUrls.from_json(json)
# print the JSON string representation of the object
print(ThemedUrls.to_json())

# convert the object into a dict
themed_urls_dict = themed_urls_instance.to_dict()
# create an instance of ThemedUrls from a dict
themed_urls_from_dict = ThemedUrls.from_dict(themed_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


