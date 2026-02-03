# TelegramChallengeResponseRequest

Base class for all challenge responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**auth_date** | **int** |  | 
**hash** | **str** |  | 
**component** | **str** |  | [optional] [default to 'ak-source-telegram']

## Example

```python
from authentik_client.models.telegram_challenge_response_request import TelegramChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramChallengeResponseRequest from a JSON string
telegram_challenge_response_request_instance = TelegramChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(TelegramChallengeResponseRequest.to_json())

# convert the object into a dict
telegram_challenge_response_request_dict = telegram_challenge_response_request_instance.to_dict()
# create an instance of TelegramChallengeResponseRequest from a dict
telegram_challenge_response_request_from_dict = TelegramChallengeResponseRequest.from_dict(telegram_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


