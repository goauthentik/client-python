# TelegramSourcePropertyMapping

TelegramSourcePropertyMapping Serializer

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
from authentik_client.models.telegram_source_property_mapping import TelegramSourcePropertyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramSourcePropertyMapping from a JSON string
telegram_source_property_mapping_instance = TelegramSourcePropertyMapping.from_json(json)
# print the JSON string representation of the object
print(TelegramSourcePropertyMapping.to_json())

# convert the object into a dict
telegram_source_property_mapping_dict = telegram_source_property_mapping_instance.to_dict()
# create an instance of TelegramSourcePropertyMapping from a dict
telegram_source_property_mapping_from_dict = TelegramSourcePropertyMapping.from_dict(telegram_source_property_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


