# EmailStage

EmailStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [readonly] 
**use_global_settings** | **bool** | When enabled, global Email connection settings will be used and connection settings below will be ignored. | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 
**use_ssl** | **bool** |  | [optional] 
**timeout** | **int** |  | [optional] 
**from_address** | **str** |  | [optional] 
**token_expiry** | **str** | Time the token sent is valid (Format: hours&#x3D;3,minutes&#x3D;17,seconds&#x3D;300). | [optional] 
**subject** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**activate_user_on_success** | **bool** | Activate users upon completion of stage. | [optional] 
**recovery_max_attempts** | **int** |  | [optional] 
**recovery_cache_timeout** | **str** | The time window used to count recent account recovery attempts. If the number of attempts exceed recovery_max_attempts within this period, further attempts will be rate-limited. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 

## Example

```python
from authentik_client.models.email_stage import EmailStage

# TODO update the JSON string below
json = "{}"
# create an instance of EmailStage from a JSON string
email_stage_instance = EmailStage.from_json(json)
# print the JSON string representation of the object
print(EmailStage.to_json())

# convert the object into a dict
email_stage_dict = email_stage_instance.to_dict()
# create an instance of EmailStage from a dict
email_stage_from_dict = EmailStage.from_dict(email_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


