# TelegramLoginChallenge

Base login challenge for Identification stage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-source-telegram']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**bot_username** | **str** | Telegram bot username | 
**request_message_access** | **bool** |  | 

## Example

```python
from authentik_client.models.telegram_login_challenge import TelegramLoginChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramLoginChallenge from a JSON string
telegram_login_challenge_instance = TelegramLoginChallenge.from_json(json)
# print the JSON string representation of the object
print(TelegramLoginChallenge.to_json())

# convert the object into a dict
telegram_login_challenge_dict = telegram_login_challenge_instance.to_dict()
# create an instance of TelegramLoginChallenge from a dict
telegram_login_challenge_from_dict = TelegramLoginChallenge.from_dict(telegram_login_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


