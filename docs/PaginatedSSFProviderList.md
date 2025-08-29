# PaginatedSSFProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SSFProvider]**](SSFProvider.md) |  | 

## Example

```python
from authentik_client.models.paginated_ssf_provider_list import PaginatedSSFProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSSFProviderList from a JSON string
paginated_ssf_provider_list_instance = PaginatedSSFProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSSFProviderList.to_json())

# convert the object into a dict
paginated_ssf_provider_list_dict = paginated_ssf_provider_list_instance.to_dict()
# create an instance of PaginatedSSFProviderList from a dict
paginated_ssf_provider_list_from_dict = PaginatedSSFProviderList.from_dict(paginated_ssf_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


