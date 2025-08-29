# PaginatedSSFStreamList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SSFStream]**](SSFStream.md) |  | 

## Example

```python
from authentik_client.models.paginated_ssf_stream_list import PaginatedSSFStreamList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSSFStreamList from a JSON string
paginated_ssf_stream_list_instance = PaginatedSSFStreamList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSSFStreamList.to_json())

# convert the object into a dict
paginated_ssf_stream_list_dict = paginated_ssf_stream_list_instance.to_dict()
# create an instance of PaginatedSSFStreamList from a dict
paginated_ssf_stream_list_from_dict = PaginatedSSFStreamList.from_dict(paginated_ssf_stream_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


