# PaginatedEnrollmentTokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[EnrollmentToken]**](EnrollmentToken.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_enrollment_token_list import PaginatedEnrollmentTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEnrollmentTokenList from a JSON string
paginated_enrollment_token_list_instance = PaginatedEnrollmentTokenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEnrollmentTokenList.to_json())

# convert the object into a dict
paginated_enrollment_token_list_dict = paginated_enrollment_token_list_instance.to_dict()
# create an instance of PaginatedEnrollmentTokenList from a dict
paginated_enrollment_token_list_from_dict = PaginatedEnrollmentTokenList.from_dict(paginated_enrollment_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


