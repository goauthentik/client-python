# UniquePasswordPolicyRequest

Password Uniqueness Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**password_field** | **str** | Field key to check, field keys defined in Prompt stages are available. | [optional] 
**num_historical_passwords** | **int** | Number of passwords to check against. | [optional] 

## Example

```python
from authentik_client.models.unique_password_policy_request import UniquePasswordPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UniquePasswordPolicyRequest from a JSON string
unique_password_policy_request_instance = UniquePasswordPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(UniquePasswordPolicyRequest.to_json())

# convert the object into a dict
unique_password_policy_request_dict = unique_password_policy_request_instance.to_dict()
# create an instance of UniquePasswordPolicyRequest from a dict
unique_password_policy_request_from_dict = UniquePasswordPolicyRequest.from_dict(unique_password_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


