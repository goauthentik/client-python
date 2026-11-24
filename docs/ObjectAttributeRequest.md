# ObjectAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**key** | **str** |  | 
**label** | **str** |  | 
**regex** | **str** |  | [optional] 
**type** | [**ObjectAttributeTypeEnum**](ObjectAttributeTypeEnum.md) |  | 
**group** | **str** |  | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**is_unique** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.object_attribute_request import ObjectAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAttributeRequest from a JSON string
object_attribute_request_instance = ObjectAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectAttributeRequest.to_json())

# convert the object into a dict
object_attribute_request_dict = object_attribute_request_instance.to_dict()
# create an instance of ObjectAttributeRequest from a dict
object_attribute_request_from_dict = ObjectAttributeRequest.from_dict(object_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


