# UserSwitchRequest

Request to add or switch users in the current browser.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**UserSwitchActionEnum**](UserSwitchActionEnum.md) |  | [optional] 
**user_pk** | **int** |  | [optional] 

## Example

```python
from authentik_client.models.user_switch_request import UserSwitchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchRequest from a JSON string
user_switch_request_instance = UserSwitchRequest.from_json(json)
# print the JSON string representation of the object
print(UserSwitchRequest.to_json())

# convert the object into a dict
user_switch_request_dict = user_switch_request_instance.to_dict()
# create an instance of UserSwitchRequest from a dict
user_switch_request_from_dict = UserSwitchRequest.from_dict(user_switch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


