# RelatedTarget

Simplified related target object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**pbm_uuid** | **str** |  | [readonly] 
**label** | **str** |  | [readonly] 

## Example

```python
from authentik_client.models.related_target import RelatedTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTarget from a JSON string
related_target_instance = RelatedTarget.from_json(json)
# print the JSON string representation of the object
print(RelatedTarget.to_json())

# convert the object into a dict
related_target_dict = related_target_instance.to_dict()
# create an instance of RelatedTarget from a dict
related_target_from_dict = RelatedTarget.from_dict(related_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


