# PaginatedScheduleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Schedule]**](Schedule.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_schedule_list import PaginatedScheduleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedScheduleList from a JSON string
paginated_schedule_list_instance = PaginatedScheduleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedScheduleList.to_json())

# convert the object into a dict
paginated_schedule_list_dict = paginated_schedule_list_instance.to_dict()
# create an instance of PaginatedScheduleList from a dict
paginated_schedule_list_from_dict = PaginatedScheduleList.from_dict(paginated_schedule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


