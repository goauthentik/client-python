# SoftwareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** |  | [optional] 
**source** | **str** |  | 
**path** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.software_request import SoftwareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareRequest from a JSON string
software_request_instance = SoftwareRequest.from_json(json)
# print the JSON string representation of the object
print(SoftwareRequest.to_json())

# convert the object into a dict
software_request_dict = software_request_instance.to_dict()
# create an instance of SoftwareRequest from a dict
software_request_from_dict = SoftwareRequest.from_dict(software_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


