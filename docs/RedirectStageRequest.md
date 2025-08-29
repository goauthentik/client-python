# RedirectStageRequest

RedirectStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**keep_context** | **bool** |  | [optional] 
**mode** | [**RedirectStageModeEnum**](RedirectStageModeEnum.md) |  | 
**target_static** | **str** |  | [optional] 
**target_flow** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.redirect_stage_request import RedirectStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectStageRequest from a JSON string
redirect_stage_request_instance = RedirectStageRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectStageRequest.to_json())

# convert the object into a dict
redirect_stage_request_dict = redirect_stage_request_instance.to_dict()
# create an instance of RedirectStageRequest from a dict
redirect_stage_request_from_dict = RedirectStageRequest.from_dict(redirect_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


