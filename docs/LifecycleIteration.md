# LifecycleIteration

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly] 
**content_type** | [**ContentTypeEnum**](ContentTypeEnum.md) |  | 
**object_id** | **str** |  | [readonly] 
**object_verbose** | **str** |  | [readonly] 
**object_admin_url** | **str** |  | [readonly] 
**state** | [**LifecycleIterationStateEnum**](LifecycleIterationStateEnum.md) |  | [readonly] 
**opened_on** | **date** |  | [readonly] 
**grace_period_end** | **date** |  | [readonly] 
**next_review_date** | **date** |  | [readonly] 
**reviews** | [**List[Review]**](Review.md) |  | [readonly] 
**user_can_review** | **bool** |  | [readonly] 
**reviewer_groups** | [**List[ReviewerGroup]**](ReviewerGroup.md) |  | [readonly] 
**min_reviewers** | **int** |  | [readonly] 
**reviewers** | [**List[ReviewerUser]**](ReviewerUser.md) |  | [readonly] 

## Example

```python
from authentik_client.models.lifecycle_iteration import LifecycleIteration

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleIteration from a JSON string
lifecycle_iteration_instance = LifecycleIteration.from_json(json)
# print the JSON string representation of the object
print(LifecycleIteration.to_json())

# convert the object into a dict
lifecycle_iteration_dict = lifecycle_iteration_instance.to_dict()
# create an instance of LifecycleIteration from a dict
lifecycle_iteration_from_dict = LifecycleIteration.from_dict(lifecycle_iteration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


