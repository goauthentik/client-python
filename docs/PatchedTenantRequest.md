# PatchedTenantRequest

Tenant Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ready** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.patched_tenant_request import PatchedTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTenantRequest from a JSON string
patched_tenant_request_instance = PatchedTenantRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTenantRequest.to_json())

# convert the object into a dict
patched_tenant_request_dict = patched_tenant_request_instance.to_dict()
# create an instance of PatchedTenantRequest from a dict
patched_tenant_request_from_dict = PatchedTenantRequest.from_dict(patched_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


