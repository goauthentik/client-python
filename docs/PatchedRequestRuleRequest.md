# PatchedRequestRuleRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**name** | **str** |  | [optional] 
**notification_transports** | **List[UUID]** |  | [optional] 
**notification_mode** | [**NotificationModeEnum**](NotificationModeEnum.md) |  | [optional] 
**min_reviewers** | **int** |  | [optional] 
**min_reviewers_is_per_group** | **bool** |  | [optional] 
**request_flow** | **UUID** |  | [optional] 

## Example

```python
from authentik_client.models.patched_request_rule_request import PatchedRequestRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRequestRuleRequest from a JSON string
patched_request_rule_request_instance = PatchedRequestRuleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedRequestRuleRequest.to_json())

# convert the object into a dict
patched_request_rule_request_dict = patched_request_rule_request_instance.to_dict()
# create an instance of PatchedRequestRuleRequest from a dict
patched_request_rule_request_from_dict = PatchedRequestRuleRequest.from_dict(patched_request_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


