# PaginatedRedirectStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RedirectStage]**](RedirectStage.md) |  | 

## Example

```python
from authentik_client.models.paginated_redirect_stage_list import PaginatedRedirectStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRedirectStageList from a JSON string
paginated_redirect_stage_list_instance = PaginatedRedirectStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRedirectStageList.to_json())

# convert the object into a dict
paginated_redirect_stage_list_dict = paginated_redirect_stage_list_instance.to_dict()
# create an instance of PaginatedRedirectStageList from a dict
paginated_redirect_stage_list_from_dict = PaginatedRedirectStageList.from_dict(paginated_redirect_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


