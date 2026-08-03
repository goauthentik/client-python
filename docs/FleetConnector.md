# FleetConnector

FleetConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**url** | **str** |  | 
**headers_mapping** | **UUID** | Configure additional headers to be sent. Mapping should return a dictionary of key-value pairs | [optional] 
**map_users** | **bool** |  | [optional] 
**map_teams_access_group** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.fleet_connector import FleetConnector

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConnector from a JSON string
fleet_connector_instance = FleetConnector.from_json(json)
# print the JSON string representation of the object
print(FleetConnector.to_json())

# convert the object into a dict
fleet_connector_dict = fleet_connector_instance.to_dict()
# create an instance of FleetConnector from a dict
fleet_connector_from_dict = FleetConnector.from_dict(fleet_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


