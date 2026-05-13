# EventRequest

Event Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **Dict[str, object]** |  | [optional] 
**action** | [**EventActions**](EventActions.md) |  | 
**app** | **str** |  | 
**context** | **Dict[str, object]** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**brand** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.event_request import EventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventRequest from a JSON string
event_request_instance = EventRequest.from_json(json)
# print the JSON string representation of the object
print(EventRequest.to_json())

# convert the object into a dict
event_request_dict = event_request_instance.to_dict()
# create an instance of EventRequest from a dict
event_request_from_dict = EventRequest.from_dict(event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


