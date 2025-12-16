# OperatingSystemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | [**DeviceFactsOSFamily**](DeviceFactsOSFamily.md) |  | 
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**arch** | **str** |  | 

## Example

```python
from authentik_client.models.operating_system_request import OperatingSystemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystemRequest from a JSON string
operating_system_request_instance = OperatingSystemRequest.from_json(json)
# print the JSON string representation of the object
print(OperatingSystemRequest.to_json())

# convert the object into a dict
operating_system_request_dict = operating_system_request_instance.to_dict()
# create an instance of OperatingSystemRequest from a dict
operating_system_request_from_dict = OperatingSystemRequest.from_dict(operating_system_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


