# KerberosSyncStatus

Kerberos Source sync status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_running** | **bool** |  | [readonly] 
**tasks** | [**List[SystemTask]**](SystemTask.md) |  | [readonly] 

## Example

```python
from authentik_client.models.kerberos_sync_status import KerberosSyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosSyncStatus from a JSON string
kerberos_sync_status_instance = KerberosSyncStatus.from_json(json)
# print the JSON string representation of the object
print(KerberosSyncStatus.to_json())

# convert the object into a dict
kerberos_sync_status_dict = kerberos_sync_status_instance.to_dict()
# create an instance of KerberosSyncStatus from a dict
kerberos_sync_status_from_dict = KerberosSyncStatus.from_dict(kerberos_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


