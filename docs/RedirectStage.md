# RedirectStage

RedirectStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [readonly] 
**keep_context** | **bool** |  | [optional] 
**mode** | [**RedirectStageModeEnum**](RedirectStageModeEnum.md) |  | 
**target_static** | **str** |  | [optional] 
**target_flow** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.redirect_stage import RedirectStage

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectStage from a JSON string
redirect_stage_instance = RedirectStage.from_json(json)
# print the JSON string representation of the object
print(RedirectStage.to_json())

# convert the object into a dict
redirect_stage_dict = redirect_stage_instance.to_dict()
# create an instance of RedirectStage from a dict
redirect_stage_from_dict = RedirectStage.from_dict(redirect_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


