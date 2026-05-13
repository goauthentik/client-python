# EventStats

Count of unique users in events and aggregated counts per specified deltas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_users** | **int** |  | 
**count_step** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.event_stats import EventStats

# TODO update the JSON string below
json = "{}"
# create an instance of EventStats from a JSON string
event_stats_instance = EventStats.from_json(json)
# print the JSON string representation of the object
print(EventStats.to_json())

# convert the object into a dict
event_stats_dict = event_stats_instance.to_dict()
# create an instance of EventStats from a dict
event_stats_from_dict = EventStats.from_dict(event_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


