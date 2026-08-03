# PaginatedRequestRuleChildBindingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RequestRuleChildBinding]**](RequestRuleChildBinding.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_request_rule_child_binding_list import PaginatedRequestRuleChildBindingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRequestRuleChildBindingList from a JSON string
paginated_request_rule_child_binding_list_instance = PaginatedRequestRuleChildBindingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRequestRuleChildBindingList.to_json())

# convert the object into a dict
paginated_request_rule_child_binding_list_dict = paginated_request_rule_child_binding_list_instance.to_dict()
# create an instance of PaginatedRequestRuleChildBindingList from a dict
paginated_request_rule_child_binding_list_from_dict = PaginatedRequestRuleChildBindingList.from_dict(paginated_request_rule_child_binding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


