# AppleIndependentSecureEnclave


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
from authentik_client.models.apple_independent_secure_enclave import AppleIndependentSecureEnclave

# TODO update the JSON string below
json = "{}"
# create an instance of AppleIndependentSecureEnclave from a JSON string
apple_independent_secure_enclave_instance = AppleIndependentSecureEnclave.from_json(json)
# print the JSON string representation of the object
print(AppleIndependentSecureEnclave.to_json())

# convert the object into a dict
apple_independent_secure_enclave_dict = apple_independent_secure_enclave_instance.to_dict()
# create an instance of AppleIndependentSecureEnclave from a dict
apple_independent_secure_enclave_from_dict = AppleIndependentSecureEnclave.from_dict(apple_independent_secure_enclave_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


