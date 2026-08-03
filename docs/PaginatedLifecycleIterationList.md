# PaginatedLifecycleIterationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[LifecycleIteration]**](LifecycleIteration.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_lifecycle_iteration_list import PaginatedLifecycleIterationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLifecycleIterationList from a JSON string
paginated_lifecycle_iteration_list_instance = PaginatedLifecycleIterationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLifecycleIterationList.to_json())

# convert the object into a dict
paginated_lifecycle_iteration_list_dict = paginated_lifecycle_iteration_list_instance.to_dict()
# create an instance of PaginatedLifecycleIterationList from a dict
paginated_lifecycle_iteration_list_from_dict = PaginatedLifecycleIterationList.from_dict(paginated_lifecycle_iteration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


