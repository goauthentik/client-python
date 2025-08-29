# UserKerberosSourceConnectionRequest

Kerberos Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**source** | **str** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.user_kerberos_source_connection_request import UserKerberosSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserKerberosSourceConnectionRequest from a JSON string
user_kerberos_source_connection_request_instance = UserKerberosSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserKerberosSourceConnectionRequest.to_json())

# convert the object into a dict
user_kerberos_source_connection_request_dict = user_kerberos_source_connection_request_instance.to_dict()
# create an instance of UserKerberosSourceConnectionRequest from a dict
user_kerberos_source_connection_request_from_dict = UserKerberosSourceConnectionRequest.from_dict(user_kerberos_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


