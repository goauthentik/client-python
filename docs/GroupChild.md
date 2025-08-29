# GroupChild

Stripped down group serializer to show relevant children for groups

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
from authentik_client.models.group_child import GroupChild

# TODO update the JSON string below
json = "{}"
# create an instance of GroupChild from a JSON string
group_child_instance = GroupChild.from_json(json)
# print the JSON string representation of the object
print(GroupChild.to_json())

# convert the object into a dict
group_child_dict = group_child_instance.to_dict()
# create an instance of GroupChild from a dict
group_child_from_dict = GroupChild.from_dict(group_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


