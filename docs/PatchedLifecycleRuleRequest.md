# PatchedLifecycleRuleRequest

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**content_type** | [**ContentTypeEnum**](ContentTypeEnum.md) |  | [optional] 
**object_id** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**grace_period** | **str** |  | [optional] 
**reviewer_groups** | **List[UUID]** |  | [optional] 
**min_reviewers** | **int** |  | [optional] 
**min_reviewers_is_per_group** | **bool** |  | [optional] 
**reviewers** | **List[UUID]** |  | [optional] 
**notification_transports** | **List[UUID]** | Select which transports should be used to notify the reviewers. If none are selected, the notification will only be shown in the authentik UI. | [optional] 

## Example

```python
from authentik_client.models.patched_lifecycle_rule_request import PatchedLifecycleRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLifecycleRuleRequest from a JSON string
patched_lifecycle_rule_request_instance = PatchedLifecycleRuleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLifecycleRuleRequest.to_json())

# convert the object into a dict
patched_lifecycle_rule_request_dict = patched_lifecycle_rule_request_instance.to_dict()
# create an instance of PatchedLifecycleRuleRequest from a dict
patched_lifecycle_rule_request_from_dict = PatchedLifecycleRuleRequest.from_dict(patched_lifecycle_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


