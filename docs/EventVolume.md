# EventVolume

Count of events of action created on day

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**EventActions**](EventActions.md) |  | 
**time** | **datetime** |  | 
**count** | **int** |  | 

## Example

```python
from authentik_client.models.event_volume import EventVolume

# TODO update the JSON string below
json = "{}"
# create an instance of EventVolume from a JSON string
event_volume_instance = EventVolume.from_json(json)
# print the JSON string representation of the object
print(EventVolume.to_json())

# convert the object into a dict
event_volume_dict = event_volume_instance.to_dict()
# create an instance of EventVolume from a dict
event_volume_from_dict = EventVolume.from_dict(event_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


