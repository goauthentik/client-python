# PaginatedRequestRuleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RequestRule]**](RequestRule.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_request_rule_list import PaginatedRequestRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRequestRuleList from a JSON string
paginated_request_rule_list_instance = PaginatedRequestRuleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRequestRuleList.to_json())

# convert the object into a dict
paginated_request_rule_list_dict = paginated_request_rule_list_instance.to_dict()
# create an instance of PaginatedRequestRuleList from a dict
paginated_request_rule_list_from_dict = PaginatedRequestRuleList.from_dict(paginated_request_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


