# DeviceUserBinding

PolicyBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**policy** | **UUID** |  | [optional] 
**group** | **UUID** |  | [optional] 
**user** | **int** |  | [optional] 
**policy_obj** | [**Policy**](Policy.md) |  | [readonly] 
**group_obj** | [**PartialGroup**](PartialGroup.md) |  | [readonly] 
**user_obj** | [**PartialUser**](PartialUser.md) |  | [readonly] 
**target** | **UUID** |  | 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 
**is_primary** | **bool** |  | [optional] 
**connector** | **UUID** |  | [readonly] 
**connector_obj** | [**Connector**](Connector.md) |  | [readonly] 

## Example

```python
from authentik_client.models.device_user_binding import DeviceUserBinding

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUserBinding from a JSON string
device_user_binding_instance = DeviceUserBinding.from_json(json)
# print the JSON string representation of the object
print(DeviceUserBinding.to_json())

# convert the object into a dict
device_user_binding_dict = device_user_binding_instance.to_dict()
# create an instance of DeviceUserBinding from a dict
device_user_binding_from_dict = DeviceUserBinding.from_dict(device_user_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


