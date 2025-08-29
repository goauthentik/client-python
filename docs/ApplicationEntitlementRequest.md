# ApplicationEntitlementRequest

ApplicationEntitlement Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**app** | **str** |  | 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_client.models.application_entitlement_request import ApplicationEntitlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEntitlementRequest from a JSON string
application_entitlement_request_instance = ApplicationEntitlementRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationEntitlementRequest.to_json())

# convert the object into a dict
application_entitlement_request_dict = application_entitlement_request_instance.to_dict()
# create an instance of ApplicationEntitlementRequest from a dict
application_entitlement_request_from_dict = ApplicationEntitlementRequest.from_dict(application_entitlement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


