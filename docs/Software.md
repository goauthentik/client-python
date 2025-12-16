# Software


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** |  | [optional] 
**source** | **str** |  | 
**path** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.software import Software

# TODO update the JSON string below
json = "{}"
# create an instance of Software from a JSON string
software_instance = Software.from_json(json)
# print the JSON string representation of the object
print(Software.to_json())

# convert the object into a dict
software_dict = software_instance.to_dict()
# create an instance of Software from a dict
software_from_dict = Software.from_dict(software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


