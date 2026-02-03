# BrandRequest

Brand Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain that activates this brand. Can be a superset, i.e. &#x60;a.b&#x60; for &#x60;aa.b&#x60; and &#x60;ba.b&#x60; | 
**default** | **bool** |  | [optional] 
**branding_title** | **str** |  | [optional] 
**branding_logo** | **str** |  | [optional] 
**branding_favicon** | **str** |  | [optional] 
**branding_custom_css** | **str** |  | [optional] 
**branding_default_flow_background** | **str** |  | [optional] 
**flow_authentication** | **UUID** |  | [optional] 
**flow_invalidation** | **UUID** |  | [optional] 
**flow_recovery** | **UUID** |  | [optional] 
**flow_unenrollment** | **UUID** |  | [optional] 
**flow_user_settings** | **UUID** |  | [optional] 
**flow_device_code** | **UUID** |  | [optional] 
**default_application** | **UUID** | When set, external users will be redirected to this application after authenticating. | [optional] 
**web_certificate** | **UUID** | Web Certificate used by the authentik Core webserver. | [optional] 
**client_certificates** | **List[UUID]** | Certificates used for client authentication. | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_client.models.brand_request import BrandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrandRequest from a JSON string
brand_request_instance = BrandRequest.from_json(json)
# print the JSON string representation of the object
print(BrandRequest.to_json())

# convert the object into a dict
brand_request_dict = brand_request_instance.to_dict()
# create an instance of BrandRequest from a dict
brand_request_from_dict = BrandRequest.from_dict(brand_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


