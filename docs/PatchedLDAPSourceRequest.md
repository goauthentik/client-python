# PatchedLDAPSourceRequest

LDAP Source Serializer

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
**server_uri** | **str** |  | [optional] 
**peer_certificate** | **UUID** | Optionally verify the LDAP Server&#39;s Certificate against the CA Chain in this keypair. | [optional] 
**client_certificate** | **UUID** | Client certificate to authenticate against the LDAP Server&#39;s Certificate. | [optional] 
**bind_cn** | **str** |  | [optional] 
**bind_password** | **str** |  | [optional] 
**start_tls** | **bool** |  | [optional] 
**sni** | **bool** |  | [optional] 
**base_dn** | **str** |  | [optional] 
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
**sync_parent_group** | **UUID** |  | [optional] 
**lookup_groups_from_user** | **bool** | Lookup group membership based on a user attribute instead of a group attribute. This allows nested group resolution on systems like FreeIPA and Active Directory | [optional] 
**delete_not_found_objects** | **bool** | Delete authentik users and groups which were previously supplied by this source, but are now missing from it. | [optional] 
**sync_outgoing_trigger_mode** | [**SyncOutgoingTriggerModeEnum**](SyncOutgoingTriggerModeEnum.md) | When to trigger sync for outgoing providers | [optional] 

## Example

```python
from authentik_client.models.patched_ldap_source_request import PatchedLDAPSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLDAPSourceRequest from a JSON string
patched_ldap_source_request_instance = PatchedLDAPSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLDAPSourceRequest.to_json())

# convert the object into a dict
patched_ldap_source_request_dict = patched_ldap_source_request_instance.to_dict()
# create an instance of PatchedLDAPSourceRequest from a dict
patched_ldap_source_request_from_dict = PatchedLDAPSourceRequest.from_dict(patched_ldap_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


