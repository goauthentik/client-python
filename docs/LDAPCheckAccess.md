# LDAPCheckAccess

Base serializer class which doesn't implement create/update methods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_search_permission** | **bool** |  | [optional] 
**access** | [**PolicyTestResult**](PolicyTestResult.md) |  | 

## Example

```python
from authentik_client.models.ldap_check_access import LDAPCheckAccess

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPCheckAccess from a JSON string
ldap_check_access_instance = LDAPCheckAccess.from_json(json)
# print the JSON string representation of the object
print(LDAPCheckAccess.to_json())

# convert the object into a dict
ldap_check_access_dict = ldap_check_access_instance.to_dict()
# create an instance of LDAPCheckAccess from a dict
ldap_check_access_from_dict = LDAPCheckAccess.from_dict(ldap_check_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


