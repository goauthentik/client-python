# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**queue_name** | **str** | Queue name | [optional] 
**actor_name** | **str** | Dramatiq actor name | 
**state** | [**StateEnum**](StateEnum.md) | Task status | [optional] 
**mtime** | **datetime** | Task last modified time | [optional] 
**rel_obj_app_label** | **str** |  | [readonly] 
**rel_obj_model** | **str** |  | [readonly] 
**rel_obj_id** | **str** |  | [optional] 
**uid** | **str** |  | [readonly] 
**messages** | [**List[LogEvent]**](LogEvent.md) |  | 
**previous_messages** | [**List[LogEvent]**](LogEvent.md) |  | 
**aggregated_status** | [**TaskAggregatedStatusEnum**](TaskAggregatedStatusEnum.md) |  | 
**description** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


