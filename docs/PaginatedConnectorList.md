# PaginatedConnectorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Connector]**](Connector.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_connector_list import PaginatedConnectorList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConnectorList from a JSON string
paginated_connector_list_instance = PaginatedConnectorList.from_json(json)
# print the JSON string representation of the object
print(PaginatedConnectorList.to_json())

# convert the object into a dict
paginated_connector_list_dict = paginated_connector_list_instance.to_dict()
# create an instance of PaginatedConnectorList from a dict
paginated_connector_list_from_dict = PaginatedConnectorList.from_dict(paginated_connector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


