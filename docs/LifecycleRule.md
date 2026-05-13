# LifecycleRule

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**content_type** | [**ContentTypeEnum**](ContentTypeEnum.md) |  | 
**object_id** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**grace_period** | **str** |  | [optional] 
**reviewer_groups** | **List[UUID]** |  | [optional] 
**reviewer_groups_obj** | [**List[ReviewerGroup]**](ReviewerGroup.md) |  | [readonly] 
**min_reviewers** | **int** |  | [optional] 
**min_reviewers_is_per_group** | **bool** |  | [optional] 
**reviewers** | **List[UUID]** |  | 
**reviewers_obj** | [**List[ReviewerUser]**](ReviewerUser.md) |  | [readonly] 
**notification_transports** | **List[UUID]** | Select which transports should be used to notify the reviewers. If none are selected, the notification will only be shown in the authentik UI. | [optional] 
**target_verbose** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.lifecycle_rule import LifecycleRule

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleRule from a JSON string
lifecycle_rule_instance = LifecycleRule.from_json(json)
# print the JSON string representation of the object
print(LifecycleRule.to_json())

# convert the object into a dict
lifecycle_rule_dict = lifecycle_rule_instance.to_dict()
# create an instance of LifecycleRule from a dict
lifecycle_rule_from_dict = LifecycleRule.from_dict(lifecycle_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


