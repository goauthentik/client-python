# TelegramAuthRequest


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

## Example

```python
from authentik_client.models.telegram_auth_request import TelegramAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramAuthRequest from a JSON string
telegram_auth_request_instance = TelegramAuthRequest.from_json(json)
# print the JSON string representation of the object
print(TelegramAuthRequest.to_json())

# convert the object into a dict
telegram_auth_request_dict = telegram_auth_request_instance.to_dict()
# create an instance of TelegramAuthRequest from a dict
telegram_auth_request_from_dict = TelegramAuthRequest.from_dict(telegram_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


