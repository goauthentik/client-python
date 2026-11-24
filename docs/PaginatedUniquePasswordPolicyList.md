# PaginatedUniquePasswordPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UniquePasswordPolicy]**](UniquePasswordPolicy.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_unique_password_policy_list import PaginatedUniquePasswordPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUniquePasswordPolicyList from a JSON string
paginated_unique_password_policy_list_instance = PaginatedUniquePasswordPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUniquePasswordPolicyList.to_json())

# convert the object into a dict
paginated_unique_password_policy_list_dict = paginated_unique_password_policy_list_instance.to_dict()
# create an instance of PaginatedUniquePasswordPolicyList from a dict
paginated_unique_password_policy_list_from_dict = PaginatedUniquePasswordPolicyList.from_dict(paginated_unique_password_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


