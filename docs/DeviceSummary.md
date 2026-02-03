# DeviceSummary

Summary of registered devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**unreachable_count** | **int** |  | 
**outdated_agent_count** | **int** |  | 

## Example

```python
from authentik_client.models.device_summary import DeviceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSummary from a JSON string
device_summary_instance = DeviceSummary.from_json(json)
# print the JSON string representation of the object
print(DeviceSummary.to_json())

# convert the object into a dict
device_summary_dict = device_summary_instance.to_dict()
# create an instance of DeviceSummary from a dict
device_summary_from_dict = DeviceSummary.from_dict(device_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


