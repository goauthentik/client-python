# TelegramSource

Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**promoted** | **bool** | When enabled, this source will be displayed as a prominent button on the login page, instead of a small icon. | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [readonly] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_url** | **str** |  | [readonly] 
**icon_themed_urls** | [**ThemedUrls**](ThemedUrls.md) |  | [readonly] 
**bot_username** | **str** | Telegram bot username | 
**request_message_access** | **bool** | Request access to send messages from your bot. | [optional] 
**pre_authentication_flow** | **str** | Flow used before authentication. | 

## Example

```python
from authentik_client.models.telegram_source import TelegramSource

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramSource from a JSON string
telegram_source_instance = TelegramSource.from_json(json)
# print the JSON string representation of the object
print(TelegramSource.to_json())

# convert the object into a dict
telegram_source_dict = telegram_source_instance.to_dict()
# create an instance of TelegramSource from a dict
telegram_source_from_dict = TelegramSource.from_dict(telegram_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


