# GroupTelegramSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **UUID** |  | 
**source** | **UUID** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_telegram_source_connection_request import GroupTelegramSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTelegramSourceConnectionRequest from a JSON string
group_telegram_source_connection_request_instance = GroupTelegramSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupTelegramSourceConnectionRequest.to_json())

# convert the object into a dict
group_telegram_source_connection_request_dict = group_telegram_source_connection_request_instance.to_dict()
# create an instance of GroupTelegramSourceConnectionRequest from a dict
group_telegram_source_connection_request_from_dict = GroupTelegramSourceConnectionRequest.from_dict(group_telegram_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


