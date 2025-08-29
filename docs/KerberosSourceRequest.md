# KerberosSourceRequest

Kerberos Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**group_matching_mode** | [**GroupMatchingModeEnum**](GroupMatchingModeEnum.md) | How the source determines if an existing group should be used or a new group created. | [optional] 
**realm** | **str** | Kerberos realm | 
**krb5_conf** | **str** | Custom krb5.conf to use. Uses the system one by default | [optional] 
**kadmin_type** | [**KadminTypeEnum**](KadminTypeEnum.md) | KAdmin server type | [optional] 
**sync_users** | **bool** | Sync users from Kerberos into authentik | [optional] 
**sync_users_password** | **bool** | When a user changes their password, sync it back to Kerberos | [optional] 
**sync_principal** | **str** | Principal to authenticate to kadmin for sync. | [optional] 
**sync_password** | **str** | Password to authenticate to kadmin for sync | [optional] 
**sync_keytab** | **str** | Keytab to authenticate to kadmin for sync. Must be base64-encoded or in the form TYPE:residual | [optional] 
**sync_ccache** | **str** | Credentials cache to authenticate to kadmin for sync. Must be in the form TYPE:residual | [optional] 
**spnego_server_name** | **str** | Force the use of a specific server name for SPNEGO. Must be in the form HTTP@hostname | [optional] 
**spnego_keytab** | **str** | SPNEGO keytab base64-encoded or path to keytab in the form FILE:path | [optional] 
**spnego_ccache** | **str** | Credential cache to use for SPNEGO in form type:residual | [optional] 
**password_login_update_internal_password** | **bool** | If enabled, the authentik-stored password will be updated upon login with the Kerberos password backend | [optional] 

## Example

```python
from authentik_client.models.kerberos_source_request import KerberosSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosSourceRequest from a JSON string
kerberos_source_request_instance = KerberosSourceRequest.from_json(json)
# print the JSON string representation of the object
print(KerberosSourceRequest.to_json())

# convert the object into a dict
kerberos_source_request_dict = kerberos_source_request_instance.to_dict()
# create an instance of KerberosSourceRequest from a dict
kerberos_source_request_from_dict = KerberosSourceRequest.from_dict(kerberos_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


