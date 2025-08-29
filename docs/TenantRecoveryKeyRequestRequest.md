# TenantRecoveryKeyRequestRequest

Tenant recovery key creation request serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**duration_days** | **int** |  | 

## Example

```python
from authentik_client.models.tenant_recovery_key_request_request import TenantRecoveryKeyRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRecoveryKeyRequestRequest from a JSON string
tenant_recovery_key_request_request_instance = TenantRecoveryKeyRequestRequest.from_json(json)
# print the JSON string representation of the object
print(TenantRecoveryKeyRequestRequest.to_json())

# convert the object into a dict
tenant_recovery_key_request_request_dict = tenant_recovery_key_request_request_instance.to_dict()
# create an instance of TenantRecoveryKeyRequestRequest from a dict
tenant_recovery_key_request_request_from_dict = TenantRecoveryKeyRequestRequest.from_dict(tenant_recovery_key_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


