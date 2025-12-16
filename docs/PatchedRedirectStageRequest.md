# PatchedRedirectStageRequest

RedirectStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**keep_context** | **bool** |  | [optional] 
**mode** | [**RedirectStageModeEnum**](RedirectStageModeEnum.md) |  | [optional] 
**target_static** | **str** |  | [optional] 
**target_flow** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_redirect_stage_request import PatchedRedirectStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRedirectStageRequest from a JSON string
patched_redirect_stage_request_instance = PatchedRedirectStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedRedirectStageRequest.to_json())

# convert the object into a dict
patched_redirect_stage_request_dict = patched_redirect_stage_request_instance.to_dict()
# create an instance of PatchedRedirectStageRequest from a dict
patched_redirect_stage_request_from_dict = PatchedRedirectStageRequest.from_dict(patched_redirect_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


