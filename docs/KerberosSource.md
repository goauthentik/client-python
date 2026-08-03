# KerberosSource

Kerberos Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**promoted** | **bool** | When enabled, this source will be displayed as a prominent button on the login page, instead of a small icon. | [optional] 
**authentication_flow** | **UUID** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **UUID** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[UUID]** |  | [optional] 
**group_property_mappings** | **List[UUID]** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [readonly] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_url** | **str** |  | [readonly] 
**icon_themed_urls** | [**ThemedUrls**](ThemedUrls.md) |  | [readonly] 
**group_matching_mode** | [**GroupMatchingModeEnum**](GroupMatchingModeEnum.md) | How the source determines if an existing group should be used or a new group created. | [optional] 
**realm** | **str** | Kerberos realm | 
**krb5_conf** | **str** | Custom krb5.conf to use. Uses the system one by default | [optional] 
**kadmin_type** | [**KadminTypeEnum**](KadminTypeEnum.md) | KAdmin server type | [optional] 
**sync_users** | **bool** | Sync users from Kerberos into authentik | [optional] 
**sync_users_password** | **bool** | When a user changes their password, sync it back to Kerberos | [optional] 
**sync_principal** | **str** | Principal to authenticate to kadmin for sync. | [optional] 
**sync_ccache** | **str** | Credentials cache to authenticate to kadmin for sync. Must be in the form TYPE:residual | [optional] 
**connectivity** | **Dict[str, str]** | Get cached source connectivity | [readonly] 
**spnego_server_name** | **str** | Force the use of a specific server name for SPNEGO. Must be in the form HTTP@hostname | [optional] 
**spnego_ccache** | **str** | Credential cache to use for SPNEGO in form type:residual | [optional] 
**password_login_update_internal_password** | **bool** | If enabled, the authentik-stored password will be updated upon login with the Kerberos password backend | [optional] 
**sync_outgoing_trigger_mode** | [**SyncOutgoingTriggerModeEnum**](SyncOutgoingTriggerModeEnum.md) | When to trigger sync for outgoing providers | [optional] 

## Example

```python
from authentik_client.models.kerberos_source import KerberosSource

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosSource from a JSON string
kerberos_source_instance = KerberosSource.from_json(json)
# print the JSON string representation of the object
print(KerberosSource.to_json())

# convert the object into a dict
kerberos_source_dict = kerberos_source_instance.to_dict()
# create an instance of KerberosSource from a dict
kerberos_source_from_dict = KerberosSource.from_dict(kerberos_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


