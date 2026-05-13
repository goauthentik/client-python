# ReviewerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**uuid** | **UUID** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 

## Example

```python
from authentik_client.models.reviewer_user import ReviewerUser

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewerUser from a JSON string
reviewer_user_instance = ReviewerUser.from_json(json)
# print the JSON string representation of the object
print(ReviewerUser.to_json())

# convert the object into a dict
reviewer_user_dict = reviewer_user_instance.to_dict()
# create an instance of ReviewerUser from a dict
reviewer_user_from_dict = ReviewerUser.from_dict(reviewer_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


