# TransactionPolicyBindingRequest

PolicyBindingSerializer which does not require target as target is set implicitly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**user** | **int** |  | [optional] 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 

## Example

```python
from authentik_client.models.transaction_policy_binding_request import TransactionPolicyBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPolicyBindingRequest from a JSON string
transaction_policy_binding_request_instance = TransactionPolicyBindingRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionPolicyBindingRequest.to_json())

# convert the object into a dict
transaction_policy_binding_request_dict = transaction_policy_binding_request_instance.to_dict()
# create an instance of TransactionPolicyBindingRequest from a dict
transaction_policy_binding_request_from_dict = TransactionPolicyBindingRequest.from_dict(transaction_policy_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


