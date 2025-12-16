# EndpointStageRequest

EndpointStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**connector** | **str** |  | 
**mode** | [**StageModeEnum**](StageModeEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.endpoint_stage_request import EndpointStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStageRequest from a JSON string
endpoint_stage_request_instance = EndpointStageRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointStageRequest.to_json())

# convert the object into a dict
endpoint_stage_request_dict = endpoint_stage_request_instance.to_dict()
# create an instance of EndpointStageRequest from a dict
endpoint_stage_request_from_dict = EndpointStageRequest.from_dict(endpoint_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


