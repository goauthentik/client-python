# LifecycleRuleRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**content_type** | [**ContentTypeEnum**](ContentTypeEnum.md) |  | 
**object_id** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**grace_period** | **str** |  | [optional] 
**reviewer_groups** | **List[UUID]** |  | [optional] 
**min_reviewers** | **int** |  | [optional] 
**min_reviewers_is_per_group** | **bool** |  | [optional] 
**reviewers** | **List[UUID]** |  | 
**notification_transports** | **List[UUID]** | Select which transports should be used to notify the reviewers. If none are selected, the notification will only be shown in the authentik UI. | [optional] 

## Example

```python
from authentik_client.models.lifecycle_rule_request import LifecycleRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleRuleRequest from a JSON string
lifecycle_rule_request_instance = LifecycleRuleRequest.from_json(json)
# print the JSON string representation of the object
print(LifecycleRuleRequest.to_json())

# convert the object into a dict
lifecycle_rule_request_dict = lifecycle_rule_request_instance.to_dict()
# create an instance of LifecycleRuleRequest from a dict
lifecycle_rule_request_from_dict = LifecycleRuleRequest.from_dict(lifecycle_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


