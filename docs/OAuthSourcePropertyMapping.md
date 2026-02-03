# OAuthSourcePropertyMapping

OAuthSourcePropertyMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 
**component** | **str** | Get object&#39;s component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 

## Example

```python
from authentik_client.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthSourcePropertyMapping from a JSON string
o_auth_source_property_mapping_instance = OAuthSourcePropertyMapping.from_json(json)
# print the JSON string representation of the object
print(OAuthSourcePropertyMapping.to_json())

# convert the object into a dict
o_auth_source_property_mapping_dict = o_auth_source_property_mapping_instance.to_dict()
# create an instance of OAuthSourcePropertyMapping from a dict
o_auth_source_property_mapping_from_dict = OAuthSourcePropertyMapping.from_dict(o_auth_source_property_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


