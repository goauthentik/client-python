# PatchedRequestRuleChildBindingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**binding** | **UUID** |  | [optional] 
**target** | **UUID** |  | [optional] 

## Example

```python
from authentik_client.models.patched_request_rule_child_binding_request import PatchedRequestRuleChildBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRequestRuleChildBindingRequest from a JSON string
patched_request_rule_child_binding_request_instance = PatchedRequestRuleChildBindingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedRequestRuleChildBindingRequest.to_json())

# convert the object into a dict
patched_request_rule_child_binding_request_dict = patched_request_rule_child_binding_request_instance.to_dict()
# create an instance of PatchedRequestRuleChildBindingRequest from a dict
patched_request_rule_child_binding_request_from_dict = PatchedRequestRuleChildBindingRequest.from_dict(patched_request_rule_child_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


