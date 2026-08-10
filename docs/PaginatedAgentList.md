# PaginatedAgentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Agent]**](Agent.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_agent_list import PaginatedAgentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentList from a JSON string
paginated_agent_list_instance = PaginatedAgentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAgentList.to_json())

# convert the object into a dict
paginated_agent_list_dict = paginated_agent_list_instance.to_dict()
# create an instance of PaginatedAgentList from a dict
paginated_agent_list_from_dict = PaginatedAgentList.from_dict(paginated_agent_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


