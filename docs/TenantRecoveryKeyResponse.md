# TenantRecoveryKeyResponse

Tenant recovery key creation response serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from authentik_client.models.tenant_recovery_key_response import TenantRecoveryKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRecoveryKeyResponse from a JSON string
tenant_recovery_key_response_instance = TenantRecoveryKeyResponse.from_json(json)
# print the JSON string representation of the object
print(TenantRecoveryKeyResponse.to_json())

# convert the object into a dict
tenant_recovery_key_response_dict = tenant_recovery_key_response_instance.to_dict()
# create an instance of TenantRecoveryKeyResponse from a dict
tenant_recovery_key_response_from_dict = TenantRecoveryKeyResponse.from_dict(tenant_recovery_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


