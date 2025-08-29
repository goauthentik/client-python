# Schedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**identifier** | **str** | Unique schedule identifier | [readonly] 
**uid** | **str** |  | [readonly] 
**actor_name** | **str** | Dramatiq actor to call | [readonly] 
**rel_obj_app_label** | **str** |  | [readonly] 
**rel_obj_model** | **str** |  | [readonly] 
**rel_obj_id** | **str** |  | [optional] 
**crontab** | **str** | When to schedule tasks | 
**paused** | **bool** | Pause this schedule | [optional] 
**next_run** | **datetime** |  | [readonly] 
**description** | **str** |  | [readonly] 
**last_task_status** | [**LastTaskStatusEnum**](LastTaskStatusEnum.md) |  | [readonly] 

## Example

```python
from authentik_client.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


