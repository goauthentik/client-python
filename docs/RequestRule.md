# RequestRule

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**pbm_uuid** | **UUID** |  | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**name** | **str** |  | 
**targets** | **List[UUID]** |  | [readonly] 
**notification_transports** | **List[UUID]** |  | [optional] 
**notification_mode** | [**NotificationModeEnum**](NotificationModeEnum.md) |  | [optional] 
**min_reviewers** | **int** |  | [optional] 
**min_reviewers_is_per_group** | **bool** |  | [optional] 
**request_flow** | **UUID** |  | [optional] 

## Example

```python
from authentik_client.models.request_rule import RequestRule

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRule from a JSON string
request_rule_instance = RequestRule.from_json(json)
# print the JSON string representation of the object
print(RequestRule.to_json())

# convert the object into a dict
request_rule_dict = request_rule_instance.to_dict()
# create an instance of RequestRule from a dict
request_rule_from_dict = RequestRule.from_dict(request_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


