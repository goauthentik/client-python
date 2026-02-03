# PatchedKerberosSourceRequest

Kerberos Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | [optional] 
**slug** | **str** | Internal source name, used in URLs. | [optional] 
**enabled** | **bool** |  | [optional] 
**promoted** | **bool** | When enabled, this source will be displayed as a prominent button on the login page, instead of a small icon. | [optional] 
**authentication_flow** | **UUID** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **UUID** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[UUID]** |  | [optional] 
**group_property_mappings** | **List[UUID]** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**group_matching_mode** | [**GroupMatchingModeEnum**](GroupMatchingModeEnum.md) | How the source determines if an existing group should be used or a new group created. | [optional] 
**realm** | **str** | Kerberos realm | [optional] 
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
**sync_outgoing_trigger_mode** | [**SyncOutgoingTriggerModeEnum**](SyncOutgoingTriggerModeEnum.md) | When to trigger sync for outgoing providers | [optional] 

## Example

```python
from authentik_client.models.patched_kerberos_source_request import PatchedKerberosSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedKerberosSourceRequest from a JSON string
patched_kerberos_source_request_instance = PatchedKerberosSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedKerberosSourceRequest.to_json())

# convert the object into a dict
patched_kerberos_source_request_dict = patched_kerberos_source_request_instance.to_dict()
# create an instance of PatchedKerberosSourceRequest from a dict
patched_kerberos_source_request_from_dict = PatchedKerberosSourceRequest.from_dict(patched_kerberos_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


