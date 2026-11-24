# PaginatedUserExpirationRuleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserExpirationRule]**](UserExpirationRule.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_user_expiration_rule_list import PaginatedUserExpirationRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserExpirationRuleList from a JSON string
paginated_user_expiration_rule_list_instance = PaginatedUserExpirationRuleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserExpirationRuleList.to_json())

# convert the object into a dict
paginated_user_expiration_rule_list_dict = paginated_user_expiration_rule_list_instance.to_dict()
# create an instance of PaginatedUserExpirationRuleList from a dict
paginated_user_expiration_rule_list_from_dict = PaginatedUserExpirationRuleList.from_dict(paginated_user_expiration_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


