# PatchedFleetConnectorRequest

FleetConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**headers_mapping** | **UUID** | Configure additional headers to be sent. Mapping should return a dictionary of key-value pairs | [optional] 
**map_users** | **bool** |  | [optional] 
**map_teams_access_group** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.patched_fleet_connector_request import PatchedFleetConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFleetConnectorRequest from a JSON string
patched_fleet_connector_request_instance = PatchedFleetConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedFleetConnectorRequest.to_json())

# convert the object into a dict
patched_fleet_connector_request_dict = patched_fleet_connector_request_instance.to_dict()
# create an instance of PatchedFleetConnectorRequest from a dict
patched_fleet_connector_request_from_dict = PatchedFleetConnectorRequest.from_dict(patched_fleet_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


