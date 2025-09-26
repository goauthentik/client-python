# PartialGroup

Partial Group Serializer, does not include child relations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**num_pk** | **int** | Get a numerical, int32 ID for the group | [readonly] 
**name** | **str** |  | 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**parent** | **str** |  | [optional] 
**parent_name** | **str** |  | [readonly] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.partial_group import PartialGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PartialGroup from a JSON string
partial_group_instance = PartialGroup.from_json(json)
# print the JSON string representation of the object
print(PartialGroup.to_json())

# convert the object into a dict
partial_group_dict = partial_group_instance.to_dict()
# create an instance of PartialGroup from a dict
partial_group_from_dict = PartialGroup.from_dict(partial_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


