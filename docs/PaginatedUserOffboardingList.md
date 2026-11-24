# PaginatedUserOffboardingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserOffboarding]**](UserOffboarding.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_user_offboarding_list import PaginatedUserOffboardingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserOffboardingList from a JSON string
paginated_user_offboarding_list_instance = PaginatedUserOffboardingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserOffboardingList.to_json())

# convert the object into a dict
paginated_user_offboarding_list_dict = paginated_user_offboarding_list_instance.to_dict()
# create an instance of PaginatedUserOffboardingList from a dict
paginated_user_offboarding_list_from_dict = PaginatedUserOffboardingList.from_dict(paginated_user_offboarding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


