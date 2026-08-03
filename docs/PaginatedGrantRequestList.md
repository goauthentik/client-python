# PaginatedGrantRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GrantRequest]**](GrantRequest.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_grant_request_list import PaginatedGrantRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGrantRequestList from a JSON string
paginated_grant_request_list_instance = PaginatedGrantRequestList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGrantRequestList.to_json())

# convert the object into a dict
paginated_grant_request_list_dict = paginated_grant_request_list_instance.to_dict()
# create an instance of PaginatedGrantRequestList from a dict
paginated_grant_request_list_from_dict = PaginatedGrantRequestList.from_dict(paginated_grant_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


