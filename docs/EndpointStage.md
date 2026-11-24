# EndpointStage

EndpointStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [readonly] 
**connector** | **UUID** |  | 
**connector_obj** | [**Connector**](Connector.md) |  | [readonly] 
**mode** | [**StageModeEnum**](StageModeEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.endpoint_stage import EndpointStage

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStage from a JSON string
endpoint_stage_instance = EndpointStage.from_json(json)
# print the JSON string representation of the object
print(EndpointStage.to_json())

# convert the object into a dict
endpoint_stage_dict = endpoint_stage_instance.to_dict()
# create an instance of EndpointStage from a dict
endpoint_stage_from_dict = EndpointStage.from_dict(endpoint_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


