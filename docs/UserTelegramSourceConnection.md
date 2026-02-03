# UserTelegramSourceConnection

User source connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | 
**source** | **UUID** |  | 
**source_obj** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 
**created** | **datetime** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.user_telegram_source_connection import UserTelegramSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserTelegramSourceConnection from a JSON string
user_telegram_source_connection_instance = UserTelegramSourceConnection.from_json(json)
# print the JSON string representation of the object
print(UserTelegramSourceConnection.to_json())

# convert the object into a dict
user_telegram_source_connection_dict = user_telegram_source_connection_instance.to_dict()
# create an instance of UserTelegramSourceConnection from a dict
user_telegram_source_connection_from_dict = UserTelegramSourceConnection.from_dict(user_telegram_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


