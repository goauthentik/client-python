# PaginatedMicrosoftIntuneConnectorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[MicrosoftIntuneConnector]**](MicrosoftIntuneConnector.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_microsoft_intune_connector_list import PaginatedMicrosoftIntuneConnectorList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMicrosoftIntuneConnectorList from a JSON string
paginated_microsoft_intune_connector_list_instance = PaginatedMicrosoftIntuneConnectorList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMicrosoftIntuneConnectorList.to_json())

# convert the object into a dict
paginated_microsoft_intune_connector_list_dict = paginated_microsoft_intune_connector_list_instance.to_dict()
# create an instance of PaginatedMicrosoftIntuneConnectorList from a dict
paginated_microsoft_intune_connector_list_from_dict = PaginatedMicrosoftIntuneConnectorList.from_dict(paginated_microsoft_intune_connector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


