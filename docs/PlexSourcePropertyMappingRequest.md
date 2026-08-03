# PlexSourcePropertyMappingRequest

PlexSourcePropertyMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 

## Example

```python
from authentik_client.models.plex_source_property_mapping_request import PlexSourcePropertyMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlexSourcePropertyMappingRequest from a JSON string
plex_source_property_mapping_request_instance = PlexSourcePropertyMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PlexSourcePropertyMappingRequest.to_json())

# convert the object into a dict
plex_source_property_mapping_request_dict = plex_source_property_mapping_request_instance.to_dict()
# create an instance of PlexSourcePropertyMappingRequest from a dict
plex_source_property_mapping_request_from_dict = PlexSourcePropertyMappingRequest.from_dict(plex_source_property_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


