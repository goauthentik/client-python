# RequestRuleChildBindingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**binding** | **UUID** |  | 
**target** | **UUID** |  | 

## Example

```python
from authentik_client.models.request_rule_child_binding_request import RequestRuleChildBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRuleChildBindingRequest from a JSON string
request_rule_child_binding_request_instance = RequestRuleChildBindingRequest.from_json(json)
# print the JSON string representation of the object
print(RequestRuleChildBindingRequest.to_json())

# convert the object into a dict
request_rule_child_binding_request_dict = request_rule_child_binding_request_instance.to_dict()
# create an instance of RequestRuleChildBindingRequest from a dict
request_rule_child_binding_request_from_dict = RequestRuleChildBindingRequest.from_dict(request_rule_child_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


