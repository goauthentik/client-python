# UniquePasswordPolicy

Password Uniqueness Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**bound_to** | **int** | Return objects policy is bound to | [readonly] 
**password_field** | **str** | Field key to check, field keys defined in Prompt stages are available. | [optional] 
**num_historical_passwords** | **int** | Number of passwords to check against. | [optional] 

## Example

```python
from authentik_client.models.unique_password_policy import UniquePasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UniquePasswordPolicy from a JSON string
unique_password_policy_instance = UniquePasswordPolicy.from_json(json)
# print the JSON string representation of the object
print(UniquePasswordPolicy.to_json())

# convert the object into a dict
unique_password_policy_dict = unique_password_policy_instance.to_dict()
# create an instance of UniquePasswordPolicy from a dict
unique_password_policy_from_dict = UniquePasswordPolicy.from_dict(unique_password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


