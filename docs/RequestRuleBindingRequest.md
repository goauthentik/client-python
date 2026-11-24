# RequestRuleBindingRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**rule** | **UUID** |  | 
**target** | **UUID** |  | 
**expiry_pending** | **str** | How long a request against this binding stays pending before it automatically lapses if not approved or denied. | [optional] 
**expiry_granted_max** | **str** | The maximum duration a grant approved against this binding can last. | [optional] 

## Example

```python
from authentik_client.models.request_rule_binding_request import RequestRuleBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRuleBindingRequest from a JSON string
request_rule_binding_request_instance = RequestRuleBindingRequest.from_json(json)
# print the JSON string representation of the object
print(RequestRuleBindingRequest.to_json())

# convert the object into a dict
request_rule_binding_request_dict = request_rule_binding_request_instance.to_dict()
# create an instance of RequestRuleBindingRequest from a dict
request_rule_binding_request_from_dict = RequestRuleBindingRequest.from_dict(request_rule_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


