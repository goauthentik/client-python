# PatchedMutualTLSStageRequest

MutualTLSStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**mode** | [**MutualTLSStageModeEnum**](MutualTLSStageModeEnum.md) |  | [optional] 
**certificate_authorities** | **List[str]** | Configure certificate authorities to validate the certificate against. This option has a higher priority than the &#x60;client_certificate&#x60; option on &#x60;Brand&#x60;. | [optional] 
**cert_attribute** | [**CertAttributeEnum**](CertAttributeEnum.md) |  | [optional] 
**user_attribute** | [**UserAttributeEnum**](UserAttributeEnum.md) |  | [optional] 

## Example

```python
from authentik_client.models.patched_mutual_tls_stage_request import PatchedMutualTLSStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMutualTLSStageRequest from a JSON string
patched_mutual_tls_stage_request_instance = PatchedMutualTLSStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedMutualTLSStageRequest.to_json())

# convert the object into a dict
patched_mutual_tls_stage_request_dict = patched_mutual_tls_stage_request_instance.to_dict()
# create an instance of PatchedMutualTLSStageRequest from a dict
patched_mutual_tls_stage_request_from_dict = PatchedMutualTLSStageRequest.from_dict(patched_mutual_tls_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


