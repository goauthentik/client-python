# MutualTLSStageRequest

MutualTLSStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mode** | [**StageModeEnum**](StageModeEnum.md) |  | 
**certificate_authorities** | **List[str]** | Configure certificate authorities to validate the certificate against. This option has a higher priority than the &#x60;client_certificate&#x60; option on &#x60;Brand&#x60;. | [optional] 
**cert_attribute** | [**CertAttributeEnum**](CertAttributeEnum.md) |  | 
**user_attribute** | [**UserAttributeEnum**](UserAttributeEnum.md) |  | 

## Example

```python
from authentik_client.models.mutual_tls_stage_request import MutualTLSStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutualTLSStageRequest from a JSON string
mutual_tls_stage_request_instance = MutualTLSStageRequest.from_json(json)
# print the JSON string representation of the object
print(MutualTLSStageRequest.to_json())

# convert the object into a dict
mutual_tls_stage_request_dict = mutual_tls_stage_request_instance.to_dict()
# create an instance of MutualTLSStageRequest from a dict
mutual_tls_stage_request_from_dict = MutualTLSStageRequest.from_dict(mutual_tls_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


