# GlobalTaskStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queued** | **int** |  | [readonly] 
**consumed** | **int** |  | [readonly] 
**preprocess** | **int** |  | [readonly] 
**running** | **int** |  | [readonly] 
**postprocess** | **int** |  | [readonly] 
**rejected** | **int** |  | [readonly] 
**done** | **int** |  | [readonly] 
**info** | **int** |  | [readonly] 
**warning** | **int** |  | [readonly] 
**error** | **int** |  | [readonly] 

## Example

```python
from authentik_client.models.global_task_status import GlobalTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalTaskStatus from a JSON string
global_task_status_instance = GlobalTaskStatus.from_json(json)
# print the JSON string representation of the object
print(GlobalTaskStatus.to_json())

# convert the object into a dict
global_task_status_dict = global_task_status_instance.to_dict()
# create an instance of GlobalTaskStatus from a dict
global_task_status_from_dict = GlobalTaskStatus.from_dict(global_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


