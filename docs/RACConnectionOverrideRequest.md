# RACConnectionOverrideRequest

RACConnectionOverride Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname/IP to connect to. Optionally specify the port. | 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | 

## Example

```python
from authentik_client.models.rac_connection_override_request import RACConnectionOverrideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RACConnectionOverrideRequest from a JSON string
rac_connection_override_request_instance = RACConnectionOverrideRequest.from_json(json)
# print the JSON string representation of the object
print(RACConnectionOverrideRequest.to_json())

# convert the object into a dict
rac_connection_override_request_dict = rac_connection_override_request_instance.to_dict()
# create an instance of RACConnectionOverrideRequest from a dict
rac_connection_override_request_from_dict = RACConnectionOverrideRequest.from_dict(rac_connection_override_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


