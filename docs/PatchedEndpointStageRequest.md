# PatchedEndpointStageRequest

EndpointStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**connector** | **str** |  | [optional] 
**mode** | [**StageModeEnum**](StageModeEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.patched_endpoint_stage_request import PatchedEndpointStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEndpointStageRequest from a JSON string
patched_endpoint_stage_request_instance = PatchedEndpointStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEndpointStageRequest.to_json())

# convert the object into a dict
patched_endpoint_stage_request_dict = patched_endpoint_stage_request_instance.to_dict()
# create an instance of PatchedEndpointStageRequest from a dict
patched_endpoint_stage_request_from_dict = PatchedEndpointStageRequest.from_dict(patched_endpoint_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


