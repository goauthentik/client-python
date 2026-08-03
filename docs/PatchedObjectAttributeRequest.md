# PatchedObjectAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to True]
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**regex** | **str** |  | [optional] 
**type** | [**ObjectAttributeTypeEnum**](ObjectAttributeTypeEnum.md) |  | [optional] 
**group** | **str** |  | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**is_unique** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.patched_object_attribute_request import PatchedObjectAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedObjectAttributeRequest from a JSON string
patched_object_attribute_request_instance = PatchedObjectAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedObjectAttributeRequest.to_json())

# convert the object into a dict
patched_object_attribute_request_dict = patched_object_attribute_request_instance.to_dict()
# create an instance of PatchedObjectAttributeRequest from a dict
patched_object_attribute_request_from_dict = PatchedObjectAttributeRequest.from_dict(patched_object_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


