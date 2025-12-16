# EndpointDeviceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** |  | [optional] 
**pbm_uuid** | **str** |  | [readonly] 
**name** | **str** |  | 
**access_group** | **str** |  | [optional] 
**access_group_obj** | [**DeviceAccessGroup**](DeviceAccessGroup.md) |  | [optional] 
**expiring** | **bool** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**facts** | [**DeviceFactSnapshot**](DeviceFactSnapshot.md) |  | [readonly] 
**attributes** | **Dict[str, object]** |  | [optional] 
**connections_obj** | [**List[DeviceConnection]**](DeviceConnection.md) |  | 
**policies** | **List[str]** |  | [readonly] 
**connections** | **List[str]** |  | [readonly] 

## Example

```python
from authentik_client.models.endpoint_device_details import EndpointDeviceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDeviceDetails from a JSON string
endpoint_device_details_instance = EndpointDeviceDetails.from_json(json)
# print the JSON string representation of the object
print(EndpointDeviceDetails.to_json())

# convert the object into a dict
endpoint_device_details_dict = endpoint_device_details_instance.to_dict()
# create an instance of EndpointDeviceDetails from a dict
endpoint_device_details_from_dict = EndpointDeviceDetails.from_dict(endpoint_device_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


