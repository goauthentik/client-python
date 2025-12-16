# LDAPSource

LDAP Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**promoted** | **bool** | When enabled, this source will be displayed as a prominent button on the login page, instead of a small icon. | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**user_property_mappings** | **List[str]** |  | [optional] 
**group_property_mappings** | **List[str]** |  | [optional] 
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
**server_uri** | **str** |  | 
**peer_certificate** | **str** | Optionally verify the LDAP Server&#39;s Certificate against the CA Chain in this keypair. | [optional] 
**client_certificate** | **str** | Client certificate to authenticate against the LDAP Server&#39;s Certificate. | [optional] 
**bind_cn** | **str** |  | [optional] 
**start_tls** | **bool** |  | [optional] 
**sni** | **bool** |  | [optional] 
**base_dn** | **str** |  | 
**additional_user_dn** | **str** | Prepended to Base DN for User-queries. | [optional] 
**additional_group_dn** | **str** | Prepended to Base DN for Group-queries. | [optional] 
**user_object_filter** | **str** | Consider Objects matching this filter to be Users. | [optional] 
**group_object_filter** | **str** | Consider Objects matching this filter to be Groups. | [optional] 
**group_membership_field** | **str** | Field which contains members of a group. | [optional] 
**user_membership_attribute** | **str** | Attribute which matches the value of &#x60;group_membership_field&#x60;. | [optional] 
**object_uniqueness_field** | **str** | Field which contains a unique Identifier. | [optional] 
**password_login_update_internal_password** | **bool** | Update internal authentik password when login succeeds with LDAP | [optional] 
**sync_users** | **bool** |  | [optional] 
**sync_users_password** | **bool** | When a user changes their password, sync it back to LDAP. This can only be enabled on a single LDAP source. | [optional] 
**sync_groups** | **bool** |  | [optional] 
**sync_parent_group** | **str** |  | [optional] 
**connectivity** | **Dict[str, Dict[str, str]]** | Get cached source connectivity | [readonly] 
**lookup_groups_from_user** | **bool** | Lookup group membership based on a user attribute instead of a group attribute. This allows nested group resolution on systems like FreeIPA and Active Directory | [optional] 
**delete_not_found_objects** | **bool** | Delete authentik users and groups which were previously supplied by this source, but are now missing from it. | [optional] 
**sync_outgoing_trigger_mode** | [**SyncOutgoingTriggerModeEnum**](SyncOutgoingTriggerModeEnum.md) | When to trigger sync for outgoing providers | [optional] 

## Example

```python
from authentik_client.models.ldap_source import LDAPSource

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPSource from a JSON string
ldap_source_instance = LDAPSource.from_json(json)
# print the JSON string representation of the object
print(LDAPSource.to_json())

# convert the object into a dict
ldap_source_dict = ldap_source_instance.to_dict()
# create an instance of LDAPSource from a dict
ldap_source_from_dict = LDAPSource.from_dict(ldap_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


