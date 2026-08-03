# PaginatedDataExportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DataExport]**](DataExport.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_data_export_list import PaginatedDataExportList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDataExportList from a JSON string
paginated_data_export_list_instance = PaginatedDataExportList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDataExportList.to_json())

# convert the object into a dict
paginated_data_export_list_dict = paginated_data_export_list_instance.to_dict()
# create an instance of PaginatedDataExportList from a dict
paginated_data_export_list_from_dict = PaginatedDataExportList.from_dict(paginated_data_export_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


