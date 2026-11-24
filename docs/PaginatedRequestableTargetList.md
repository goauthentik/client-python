# PaginatedRequestableTargetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RequestableTarget]**](RequestableTarget.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_requestable_target_list import PaginatedRequestableTargetList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRequestableTargetList from a JSON string
paginated_requestable_target_list_instance = PaginatedRequestableTargetList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRequestableTargetList.to_json())

# convert the object into a dict
paginated_requestable_target_list_dict = paginated_requestable_target_list_instance.to_dict()
# create an instance of PaginatedRequestableTargetList from a dict
paginated_requestable_target_list_from_dict = PaginatedRequestableTargetList.from_dict(paginated_requestable_target_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


