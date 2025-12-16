# PatchedTelegramSourceRequest

Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | [optional] 
**slug** | **str** | Internal source name, used in URLs. | [optional] 
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
**bot_username** | **str** | Telegram bot username | [optional] 
**bot_token** | **str** | Telegram bot token | [optional] 
**request_message_access** | **bool** | Request access to send messages from your bot. | [optional] 
**pre_authentication_flow** | **str** | Flow used before authentication. | [optional] 

## Example

```python
from authentik_client.models.patched_telegram_source_request import PatchedTelegramSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTelegramSourceRequest from a JSON string
patched_telegram_source_request_instance = PatchedTelegramSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTelegramSourceRequest.to_json())

# convert the object into a dict
patched_telegram_source_request_dict = patched_telegram_source_request_instance.to_dict()
# create an instance of PatchedTelegramSourceRequest from a dict
patched_telegram_source_request_from_dict = PatchedTelegramSourceRequest.from_dict(patched_telegram_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


