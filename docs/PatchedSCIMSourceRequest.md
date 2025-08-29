# PatchedSCIMSourceRequest

SCIMSource Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | [optional] 
**slug** | **str** | Internal source name, used in URLs. | [optional] 
**enabled** | **bool** |  | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
**user_path_template** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_scim_source_request import PatchedSCIMSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMSourceRequest from a JSON string
patched_scim_source_request_instance = PatchedSCIMSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMSourceRequest.to_json())

# convert the object into a dict
patched_scim_source_request_dict = patched_scim_source_request_instance.to_dict()
# create an instance of PatchedSCIMSourceRequest from a dict
patched_scim_source_request_from_dict = PatchedSCIMSourceRequest.from_dict(patched_scim_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


