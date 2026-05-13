# NativeLogoutChallenge

Challenge for native browser logout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-provider-saml-native-logout']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**is_complete** | **bool** |  | [optional] [default to False]
**post_url** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**saml_binding** | [**SAMLBindingsEnum**](SAMLBindingsEnum.md) |  | [optional] 
**saml_request** | **str** |  | [optional] 
**saml_response** | **str** |  | [optional] 
**saml_relay_state** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.native_logout_challenge import NativeLogoutChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of NativeLogoutChallenge from a JSON string
native_logout_challenge_instance = NativeLogoutChallenge.from_json(json)
# print the JSON string representation of the object
print(NativeLogoutChallenge.to_json())

# convert the object into a dict
native_logout_challenge_dict = native_logout_challenge_instance.to_dict()
# create an instance of NativeLogoutChallenge from a dict
native_logout_challenge_from_dict = NativeLogoutChallenge.from_dict(native_logout_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


