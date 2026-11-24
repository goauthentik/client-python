# FlowMessage

Serializer for a django.contrib.messages message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**FlowMessageLevelEnum**](FlowMessageLevelEnum.md) |  | 
**message** | **str** |  | 

## Example

```python
from authentik_client.models.flow_message import FlowMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FlowMessage from a JSON string
flow_message_instance = FlowMessage.from_json(json)
# print the JSON string representation of the object
print(FlowMessage.to_json())

# convert the object into a dict
flow_message_dict = flow_message_instance.to_dict()
# create an instance of FlowMessage from a dict
flow_message_from_dict = FlowMessage.from_dict(flow_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


