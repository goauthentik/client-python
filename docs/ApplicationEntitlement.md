# ApplicationEntitlement

ApplicationEntitlement Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pbm_uuid** | **str** |  | [readonly] 
**name** | **str** |  | 
**app** | **str** |  | 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_client.models.application_entitlement import ApplicationEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEntitlement from a JSON string
application_entitlement_instance = ApplicationEntitlement.from_json(json)
# print the JSON string representation of the object
print(ApplicationEntitlement.to_json())

# convert the object into a dict
application_entitlement_dict = application_entitlement_instance.to_dict()
# create an instance of ApplicationEntitlement from a dict
application_entitlement_from_dict = ApplicationEntitlement.from_dict(application_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


