# PaginatedDomainList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Domain]**](Domain.md) |  | 

## Example

```python
from authentik_client.models.paginated_domain_list import PaginatedDomainList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDomainList from a JSON string
paginated_domain_list_instance = PaginatedDomainList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDomainList.to_json())

# convert the object into a dict
paginated_domain_list_dict = paginated_domain_list_instance.to_dict()
# create an instance of PaginatedDomainList from a dict
paginated_domain_list_from_dict = PaginatedDomainList.from_dict(paginated_domain_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


