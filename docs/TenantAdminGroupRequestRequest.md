# TenantAdminGroupRequestRequest

Tenant admin group creation request serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 

## Example

```python
from authentik_client.models.tenant_admin_group_request_request import TenantAdminGroupRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAdminGroupRequestRequest from a JSON string
tenant_admin_group_request_request_instance = TenantAdminGroupRequestRequest.from_json(json)
# print the JSON string representation of the object
print(TenantAdminGroupRequestRequest.to_json())

# convert the object into a dict
tenant_admin_group_request_request_dict = tenant_admin_group_request_request_instance.to_dict()
# create an instance of TenantAdminGroupRequestRequest from a dict
tenant_admin_group_request_request_from_dict = TenantAdminGroupRequestRequest.from_dict(tenant_admin_group_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


