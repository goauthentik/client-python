# PartialUserExpirationRule

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.partial_user_expiration_rule import PartialUserExpirationRule

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUserExpirationRule from a JSON string
partial_user_expiration_rule_instance = PartialUserExpirationRule.from_json(json)
# print the JSON string representation of the object
print(PartialUserExpirationRule.to_json())

# convert the object into a dict
partial_user_expiration_rule_dict = partial_user_expiration_rule_instance.to_dict()
# create an instance of PartialUserExpirationRule from a dict
partial_user_expiration_rule_from_dict = PartialUserExpirationRule.from_dict(partial_user_expiration_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


