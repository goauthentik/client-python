# PaginatedAccountLockdownStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AccountLockdownStage]**](AccountLockdownStage.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_account_lockdown_stage_list import PaginatedAccountLockdownStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAccountLockdownStageList from a JSON string
paginated_account_lockdown_stage_list_instance = PaginatedAccountLockdownStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAccountLockdownStageList.to_json())

# convert the object into a dict
paginated_account_lockdown_stage_list_dict = paginated_account_lockdown_stage_list_instance.to_dict()
# create an instance of PaginatedAccountLockdownStageList from a dict
paginated_account_lockdown_stage_list_from_dict = PaginatedAccountLockdownStageList.from_dict(paginated_account_lockdown_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


