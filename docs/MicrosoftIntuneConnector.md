# MicrosoftIntuneConnector

MicrosoftIntuneConnector Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **UUID** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**client_id** | **str** |  | 
**tenant_id** | **str** |  | 
**certificate_authorities** | **List[UUID]** | Certificate authorities which issue device certificates via Intune (Cloud PKI, SCEP or PKCS profiles), used by the endpoint stage to validate certificates. This option has a higher priority than the &#x60;client_certificate&#x60; option on &#x60;Brand&#x60;. | [optional] 

## Example

```python
from authentik_client.models.microsoft_intune_connector import MicrosoftIntuneConnector

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftIntuneConnector from a JSON string
microsoft_intune_connector_instance = MicrosoftIntuneConnector.from_json(json)
# print the JSON string representation of the object
print(MicrosoftIntuneConnector.to_json())

# convert the object into a dict
microsoft_intune_connector_dict = microsoft_intune_connector_instance.to_dict()
# create an instance of MicrosoftIntuneConnector from a dict
microsoft_intune_connector_from_dict = MicrosoftIntuneConnector.from_dict(microsoft_intune_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


