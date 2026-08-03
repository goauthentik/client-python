# ObjectAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**object_type** | **str** |  | 
**object_type_obj** | [**ContentType**](ContentType.md) |  | [readonly] 
**enabled** | **bool** |  | [optional] [default to True]
**created** | **datetime** |  | [readonly] 
**key** | **str** |  | 
**label** | **str** |  | 
**last_updated** | **datetime** |  | [readonly] 
**regex** | **str** |  | [optional] 
**type** | [**ObjectAttributeTypeEnum**](ObjectAttributeTypeEnum.md) |  | 
**group** | **str** |  | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**is_unique** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.object_attribute import ObjectAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAttribute from a JSON string
object_attribute_instance = ObjectAttribute.from_json(json)
# print the JSON string representation of the object
print(ObjectAttribute.to_json())

# convert the object into a dict
object_attribute_dict = object_attribute_instance.to_dict()
# create an instance of ObjectAttribute from a dict
object_attribute_from_dict = ObjectAttribute.from_dict(object_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


