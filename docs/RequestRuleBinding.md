# RequestRuleBinding

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**pbm_uuid** | **UUID** |  | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**rule** | **UUID** |  | 
**rule_obj** | [**RequestRule**](RequestRule.md) |  | [readonly] 
**target** | **UUID** |  | 
**related** | **List[UUID]** |  | [readonly] 
**related_obj** | [**List[RelatedTarget]**](RelatedTarget.md) |  | [readonly] 
**expiry_pending** | **str** | How long a request against this binding stays pending before it automatically lapses if not approved or denied. | [optional] 
**expiry_granted_max** | **str** | The maximum duration a grant approved against this binding can last. | [optional] 

## Example

```python
from authentik_client.models.request_rule_binding import RequestRuleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRuleBinding from a JSON string
request_rule_binding_instance = RequestRuleBinding.from_json(json)
# print the JSON string representation of the object
print(RequestRuleBinding.to_json())

# convert the object into a dict
request_rule_binding_dict = request_rule_binding_instance.to_dict()
# create an instance of RequestRuleBinding from a dict
request_rule_binding_from_dict = RequestRuleBinding.from_dict(request_rule_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


