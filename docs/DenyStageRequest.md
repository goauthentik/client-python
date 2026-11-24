# DenyStageRequest

DenyStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**deny_message** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.deny_stage_request import DenyStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DenyStageRequest from a JSON string
deny_stage_request_instance = DenyStageRequest.from_json(json)
# print the JSON string representation of the object
print(DenyStageRequest.to_json())

# convert the object into a dict
deny_stage_request_dict = deny_stage_request_instance.to_dict()
# create an instance of DenyStageRequest from a dict
deny_stage_request_from_dict = DenyStageRequest.from_dict(deny_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


