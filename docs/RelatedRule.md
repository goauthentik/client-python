# RelatedRule

Mixin to validate that a valid enterprise license exists before allowing to save the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | 
**reviewer_groups** | [**List[ReviewerGroup]**](ReviewerGroup.md) |  | [readonly] 
**min_reviewers** | **int** |  | [readonly] 
**reviewers** | [**List[ReviewerUser]**](ReviewerUser.md) |  | [readonly] 

## Example

```python
from authentik_client.models.related_rule import RelatedRule

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedRule from a JSON string
related_rule_instance = RelatedRule.from_json(json)
# print the JSON string representation of the object
print(RelatedRule.to_json())

# convert the object into a dict
related_rule_dict = related_rule_instance.to_dict()
# create an instance of RelatedRule from a dict
related_rule_from_dict = RelatedRule.from_dict(related_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


