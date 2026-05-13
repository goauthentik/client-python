# Tenant

Tenant Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_uuid** | **UUID** |  | [readonly] 
**schema_name** | **str** |  | 
**name** | **str** |  | 
**ready** | **bool** |  | [optional] 

## Example

```python
from authentik_client.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print(Tenant.to_json())

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_from_dict = Tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


