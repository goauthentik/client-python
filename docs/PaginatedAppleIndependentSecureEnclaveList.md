# PaginatedAppleIndependentSecureEnclaveList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AppleIndependentSecureEnclave]**](AppleIndependentSecureEnclave.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_apple_independent_secure_enclave_list import PaginatedAppleIndependentSecureEnclaveList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAppleIndependentSecureEnclaveList from a JSON string
paginated_apple_independent_secure_enclave_list_instance = PaginatedAppleIndependentSecureEnclaveList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAppleIndependentSecureEnclaveList.to_json())

# convert the object into a dict
paginated_apple_independent_secure_enclave_list_dict = paginated_apple_independent_secure_enclave_list_instance.to_dict()
# create an instance of PaginatedAppleIndependentSecureEnclaveList from a dict
paginated_apple_independent_secure_enclave_list_from_dict = PaginatedAppleIndependentSecureEnclaveList.from_dict(paginated_apple_independent_secure_enclave_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


