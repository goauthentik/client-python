# TenantRequest

Tenant Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_name** | **str** |  | 
**name** | **str** |  | 
**ready** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.tenant_request import TenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRequest from a JSON string
tenant_request_instance = TenantRequest.from_json(json)
# print the JSON string representation of the object
print(TenantRequest.to_json())

# convert the object into a dict
tenant_request_dict = tenant_request_instance.to_dict()
# create an instance of TenantRequest from a dict
tenant_request_from_dict = TenantRequest.from_dict(tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


