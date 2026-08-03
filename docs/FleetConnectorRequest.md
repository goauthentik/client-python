# FleetConnectorRequest

FleetConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**url** | **str** |  | 
**token** | **str** |  | 
**headers_mapping** | **UUID** | Configure additional headers to be sent. Mapping should return a dictionary of key-value pairs | [optional] 
**map_users** | **bool** |  | [optional] 
**map_teams_access_group** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.fleet_connector_request import FleetConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConnectorRequest from a JSON string
fleet_connector_request_instance = FleetConnectorRequest.from_json(json)
# print the JSON string representation of the object
print(FleetConnectorRequest.to_json())

# convert the object into a dict
fleet_connector_request_dict = fleet_connector_request_instance.to_dict()
# create an instance of FleetConnectorRequest from a dict
fleet_connector_request_from_dict = FleetConnectorRequest.from_dict(fleet_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


