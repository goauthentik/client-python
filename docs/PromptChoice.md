# PromptChoice

Serializer for a single Choice field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**label** | **str** |  | 

## Example

```python
from authentik_client.models.prompt_choice import PromptChoice

# TODO update the JSON string below
json = "{}"
# create an instance of PromptChoice from a JSON string
prompt_choice_instance = PromptChoice.from_json(json)
# print the JSON string representation of the object
print(PromptChoice.to_json())

# convert the object into a dict
prompt_choice_dict = prompt_choice_instance.to_dict()
# create an instance of PromptChoice from a dict
prompt_choice_from_dict = PromptChoice.from_dict(prompt_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


