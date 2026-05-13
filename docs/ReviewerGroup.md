# ReviewerGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 

## Example

```python
from authentik_client.models.reviewer_group import ReviewerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewerGroup from a JSON string
reviewer_group_instance = ReviewerGroup.from_json(json)
# print the JSON string representation of the object
print(ReviewerGroup.to_json())

# convert the object into a dict
reviewer_group_dict = reviewer_group_instance.to_dict()
# create an instance of ReviewerGroup from a dict
reviewer_group_from_dict = ReviewerGroup.from_dict(reviewer_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


