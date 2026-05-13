# PaginatedMutualTLSStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[MutualTLSStage]**](MutualTLSStage.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_mutual_tls_stage_list import PaginatedMutualTLSStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMutualTLSStageList from a JSON string
paginated_mutual_tls_stage_list_instance = PaginatedMutualTLSStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMutualTLSStageList.to_json())

# convert the object into a dict
paginated_mutual_tls_stage_list_dict = paginated_mutual_tls_stage_list_instance.to_dict()
# create an instance of PaginatedMutualTLSStageList from a dict
paginated_mutual_tls_stage_list_from_dict = PaginatedMutualTLSStageList.from_dict(paginated_mutual_tls_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


