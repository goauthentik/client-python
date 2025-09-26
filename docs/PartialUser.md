# PartialUser

Partial User Serializer, does not include child relations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**uid** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.partial_user import PartialUser

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUser from a JSON string
partial_user_instance = PartialUser.from_json(json)
# print the JSON string representation of the object
print(PartialUser.to_json())

# convert the object into a dict
partial_user_dict = partial_user_instance.to_dict()
# create an instance of PartialUser from a dict
partial_user_from_dict = PartialUser.from_dict(partial_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


