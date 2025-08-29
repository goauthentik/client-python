# MutualTLSStage

MutualTLSStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**mode** | [**MutualTLSStageModeEnum**](MutualTLSStageModeEnum.md) |  | 
**certificate_authorities** | **List[str]** | Configure certificate authorities to validate the certificate against. This option has a higher priority than the &#x60;client_certificate&#x60; option on &#x60;Brand&#x60;. | [optional] 
**cert_attribute** | [**CertAttributeEnum**](CertAttributeEnum.md) |  | 
**user_attribute** | [**UserAttributeEnum**](UserAttributeEnum.md) |  | 

## Example

```python
from authentik_client.models.mutual_tls_stage import MutualTLSStage

# TODO update the JSON string below
json = "{}"
# create an instance of MutualTLSStage from a JSON string
mutual_tls_stage_instance = MutualTLSStage.from_json(json)
# print the JSON string representation of the object
print(MutualTLSStage.to_json())

# convert the object into a dict
mutual_tls_stage_dict = mutual_tls_stage_instance.to_dict()
# create an instance of MutualTLSStage from a dict
mutual_tls_stage_from_dict = MutualTLSStage.from_dict(mutual_tls_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


