# TelegramSourceRequest

Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**promoted** | **bool** | When enabled, this source will be displayed as a prominent button on the login page, instead of a small icon. | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**bot_username** | **str** | Telegram bot username | 
**bot_token** | **str** | Telegram bot token | 
**request_message_access** | **bool** | Request access to send messages from your bot. | [optional] 
**pre_authentication_flow** | **str** | Flow used before authentication. | 

## Example

```python
from authentik_client.models.telegram_source_request import TelegramSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramSourceRequest from a JSON string
telegram_source_request_instance = TelegramSourceRequest.from_json(json)
# print the JSON string representation of the object
print(TelegramSourceRequest.to_json())

# convert the object into a dict
telegram_source_request_dict = telegram_source_request_instance.to_dict()
# create an instance of TelegramSourceRequest from a dict
telegram_source_request_from_dict = TelegramSourceRequest.from_dict(telegram_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


