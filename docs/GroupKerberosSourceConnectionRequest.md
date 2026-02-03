# GroupKerberosSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **UUID** |  | 
**source** | **UUID** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_kerberos_source_connection_request import GroupKerberosSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupKerberosSourceConnectionRequest from a JSON string
group_kerberos_source_connection_request_instance = GroupKerberosSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupKerberosSourceConnectionRequest.to_json())

# convert the object into a dict
group_kerberos_source_connection_request_dict = group_kerberos_source_connection_request_instance.to_dict()
# create an instance of GroupKerberosSourceConnectionRequest from a dict
group_kerberos_source_connection_request_from_dict = GroupKerberosSourceConnectionRequest.from_dict(group_kerberos_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


