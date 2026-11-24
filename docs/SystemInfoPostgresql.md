# SystemInfoPostgresql

PostgreSQL information for this request's database connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**jit** | **str** |  | 
**jit_source** | **str** |  | 
**ssl** | **bool** |  | 
**ssl_version** | **str** |  | 
**ssl_cipher** | **str** |  | 

## Example

```python
from authentik_client.models.system_info_postgresql import SystemInfoPostgresql

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfoPostgresql from a JSON string
system_info_postgresql_instance = SystemInfoPostgresql.from_json(json)
# print the JSON string representation of the object
print(SystemInfoPostgresql.to_json())

# convert the object into a dict
system_info_postgresql_dict = system_info_postgresql_instance.to_dict()
# create an instance of SystemInfoPostgresql from a dict
system_info_postgresql_from_dict = SystemInfoPostgresql.from_dict(system_info_postgresql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


