# Group

Group Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**num_pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**parents** | **List[str]** |  | [optional] 
**parents_obj** | [**List[RelatedGroup]**](RelatedGroup.md) |  | [readonly] 
**users** | **List[int]** |  | [optional] 
**users_obj** | [**List[PartialUser]**](PartialUser.md) |  | [readonly] 
**attributes** | **Dict[str, object]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**roles_obj** | [**List[Role]**](Role.md) |  | [readonly] 
**inherited_roles_obj** | [**List[Role]**](Role.md) |  | [readonly] 
**children** | **List[str]** |  | [readonly] 
**children_obj** | [**List[RelatedGroup]**](RelatedGroup.md) |  | [readonly] 

## Example

```python
from authentik_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


