# PatchedApplicationEntitlementRequest

ApplicationEntitlement Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**app** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_client.models.patched_application_entitlement_request import PatchedApplicationEntitlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedApplicationEntitlementRequest from a JSON string
patched_application_entitlement_request_instance = PatchedApplicationEntitlementRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedApplicationEntitlementRequest.to_json())

# convert the object into a dict
patched_application_entitlement_request_dict = patched_application_entitlement_request_instance.to_dict()
# create an instance of PatchedApplicationEntitlementRequest from a dict
patched_application_entitlement_request_from_dict = PatchedApplicationEntitlementRequest.from_dict(patched_application_entitlement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


