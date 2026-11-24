# DiagramEdge

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** |  | [readonly] 
**target** | **str** |  | [readonly] 
**type** | [**DiagramEdgeTypeEnum**](DiagramEdgeTypeEnum.md) |  | [readonly] 

## Example

```python
from authentik_client.models.diagram_edge import DiagramEdge

# TODO update the JSON string below
json = "{}"
# create an instance of DiagramEdge from a JSON string
diagram_edge_instance = DiagramEdge.from_json(json)
# print the JSON string representation of the object
print(DiagramEdge.to_json())

# convert the object into a dict
diagram_edge_dict = diagram_edge_instance.to_dict()
# create an instance of DiagramEdge from a dict
diagram_edge_from_dict = DiagramEdge.from_dict(diagram_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


