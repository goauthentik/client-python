# RelatedGroup

Stripped down group serializer to show relevant children/parents for groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**group_uuid** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.related_group import RelatedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedGroup from a JSON string
related_group_instance = RelatedGroup.from_json(json)
# print the JSON string representation of the object
print(RelatedGroup.to_json())

# convert the object into a dict
related_group_dict = related_group_instance.to_dict()
# create an instance of RelatedGroup from a dict
related_group_from_dict = RelatedGroup.from_dict(related_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


