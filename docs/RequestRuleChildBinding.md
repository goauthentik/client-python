# RequestRuleChildBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**binding** | **UUID** |  | 
**target** | **UUID** |  | 

## Example

```python
from authentik_client.models.request_rule_child_binding import RequestRuleChildBinding

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRuleChildBinding from a JSON string
request_rule_child_binding_instance = RequestRuleChildBinding.from_json(json)
# print the JSON string representation of the object
print(RequestRuleChildBinding.to_json())

# convert the object into a dict
request_rule_child_binding_dict = request_rule_child_binding_instance.to_dict()
# create an instance of RequestRuleChildBinding from a dict
request_rule_child_binding_from_dict = RequestRuleChildBinding.from_dict(request_rule_child_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


