# PatchedAppleIndependentSecureEnclaveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**user** | **int** | The user that this device belongs to. | [optional] 
**apple_secure_enclave_key** | **str** |  | [optional] 
**apple_enclave_key_id** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.patched_apple_independent_secure_enclave_request import PatchedAppleIndependentSecureEnclaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAppleIndependentSecureEnclaveRequest from a JSON string
patched_apple_independent_secure_enclave_request_instance = PatchedAppleIndependentSecureEnclaveRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAppleIndependentSecureEnclaveRequest.to_json())

# convert the object into a dict
patched_apple_independent_secure_enclave_request_dict = patched_apple_independent_secure_enclave_request_instance.to_dict()
# create an instance of PatchedAppleIndependentSecureEnclaveRequest from a dict
patched_apple_independent_secure_enclave_request_from_dict = PatchedAppleIndependentSecureEnclaveRequest.from_dict(patched_apple_independent_secure_enclave_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


