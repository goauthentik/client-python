# AppleIndependentSecureEnclaveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**user** | **int** | The user that this device belongs to. | 
**apple_secure_enclave_key** | **str** |  | 
**apple_enclave_key_id** | **str** |  | 
**device_type** | **str** |  | 

## Example

```python
from authentik_client.models.apple_independent_secure_enclave_request import AppleIndependentSecureEnclaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppleIndependentSecureEnclaveRequest from a JSON string
apple_independent_secure_enclave_request_instance = AppleIndependentSecureEnclaveRequest.from_json(json)
# print the JSON string representation of the object
print(AppleIndependentSecureEnclaveRequest.to_json())

# convert the object into a dict
apple_independent_secure_enclave_request_dict = apple_independent_secure_enclave_request_instance.to_dict()
# create an instance of AppleIndependentSecureEnclaveRequest from a dict
apple_independent_secure_enclave_request_from_dict = AppleIndependentSecureEnclaveRequest.from_dict(apple_independent_secure_enclave_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


