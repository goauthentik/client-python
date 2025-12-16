# PaginatedAgentConnectorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AgentConnector]**](AgentConnector.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_agent_connector_list import PaginatedAgentConnectorList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentConnectorList from a JSON string
paginated_agent_connector_list_instance = PaginatedAgentConnectorList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAgentConnectorList.to_json())

# convert the object into a dict
paginated_agent_connector_list_dict = paginated_agent_connector_list_instance.to_dict()
# create an instance of PaginatedAgentConnectorList from a dict
paginated_agent_connector_list_from_dict = PaginatedAgentConnectorList.from_dict(paginated_agent_connector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


