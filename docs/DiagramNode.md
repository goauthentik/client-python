# DiagramNode

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [readonly] 
**type** | [**DiagramNodeTypeEnum**](DiagramNodeTypeEnum.md) |  | [readonly] 
**name** | **str** |  | [readonly] 
**verbose_name** | **str** |  | [readonly] 
**model** | **str** |  | [readonly] 
**pk** | **str** |  | [readonly] 
**component** | **str** |  | [readonly] 
**binding_model** | **str** |  | [readonly] 
**binding_pk** | **str** |  | [readonly] 
**binding_order** | **int** |  | [readonly] 

## Example

```python
from authentik_client.models.diagram_node import DiagramNode

# TODO update the JSON string below
json = "{}"
# create an instance of DiagramNode from a JSON string
diagram_node_instance = DiagramNode.from_json(json)
# print the JSON string representation of the object
print(DiagramNode.to_json())

# convert the object into a dict
diagram_node_dict = diagram_node_instance.to_dict()
# create an instance of DiagramNode from a dict
diagram_node_from_dict = DiagramNode.from_dict(diagram_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


