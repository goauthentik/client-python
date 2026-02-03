# SSFStream

SSFStream Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**provider** | **int** |  | 
**provider_obj** | [**SSFProvider**](SSFProvider.md) |  | [readonly] 
**delivery_method** | [**DeliveryMethodEnum**](DeliveryMethodEnum.md) |  | 
**endpoint_url** | **str** |  | [optional] 
**events_requested** | [**List[EventsRequestedEnum]**](EventsRequestedEnum.md) |  | [optional] 
**format** | **str** |  | 
**aud** | **List[str]** |  | [optional] 
**iss** | **str** |  | 

## Example

```python
from authentik_client.models.ssf_stream import SSFStream

# TODO update the JSON string below
json = "{}"
# create an instance of SSFStream from a JSON string
ssf_stream_instance = SSFStream.from_json(json)
# print the JSON string representation of the object
print(SSFStream.to_json())

# convert the object into a dict
ssf_stream_dict = ssf_stream_instance.to_dict()
# create an instance of SSFStream from a dict
ssf_stream_from_dict = SSFStream.from_dict(ssf_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


