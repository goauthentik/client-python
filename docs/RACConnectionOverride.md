# RACConnectionOverride

RACConnectionOverride Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname/IP to connect to. Optionally specify the port. | 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | 

## Example

```python
from authentik_client.models.rac_connection_override import RACConnectionOverride

# TODO update the JSON string below
json = "{}"
# create an instance of RACConnectionOverride from a JSON string
rac_connection_override_instance = RACConnectionOverride.from_json(json)
# print the JSON string representation of the object
print(RACConnectionOverride.to_json())

# convert the object into a dict
rac_connection_override_dict = rac_connection_override_instance.to_dict()
# create an instance of RACConnectionOverride from a dict
rac_connection_override_from_dict = RACConnectionOverride.from_dict(rac_connection_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


