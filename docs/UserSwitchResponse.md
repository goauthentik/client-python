# UserSwitchResponse

Redirect returned after planning a user switch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.user_switch_response import UserSwitchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchResponse from a JSON string
user_switch_response_instance = UserSwitchResponse.from_json(json)
# print the JSON string representation of the object
print(UserSwitchResponse.to_json())

# convert the object into a dict
user_switch_response_dict = user_switch_response_instance.to_dict()
# create an instance of UserSwitchResponse from a dict
user_switch_response_from_dict = UserSwitchResponse.from_dict(user_switch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


