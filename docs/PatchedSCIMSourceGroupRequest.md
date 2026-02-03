# PatchedSCIMSourceGroupRequest

SCIMSourceGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**group** | **UUID** |  | [optional] 
**source** | **UUID** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.patched_scim_source_group_request import PatchedSCIMSourceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMSourceGroupRequest from a JSON string
patched_scim_source_group_request_instance = PatchedSCIMSourceGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMSourceGroupRequest.to_json())

# convert the object into a dict
patched_scim_source_group_request_dict = patched_scim_source_group_request_instance.to_dict()
# create an instance of PatchedSCIMSourceGroupRequest from a dict
patched_scim_source_group_request_from_dict = PatchedSCIMSourceGroupRequest.from_dict(patched_scim_source_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


