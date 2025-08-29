# PaginatedAuthenticatorEndpointGDTCStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorEndpointGDTCStage]**](AuthenticatorEndpointGDTCStage.md) |  | 

## Example

```python
from authentik_client.models.paginated_authenticator_endpoint_gdtc_stage_list import PaginatedAuthenticatorEndpointGDTCStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorEndpointGDTCStageList from a JSON string
paginated_authenticator_endpoint_gdtc_stage_list_instance = PaginatedAuthenticatorEndpointGDTCStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorEndpointGDTCStageList.to_json())

# convert the object into a dict
paginated_authenticator_endpoint_gdtc_stage_list_dict = paginated_authenticator_endpoint_gdtc_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorEndpointGDTCStageList from a dict
paginated_authenticator_endpoint_gdtc_stage_list_from_dict = PaginatedAuthenticatorEndpointGDTCStageList.from_dict(paginated_authenticator_endpoint_gdtc_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


