# IframeLogoutChallenge

Challenge for iframe logout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-provider-iframe-logout']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**logout_urls** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from authentik_client.models.iframe_logout_challenge import IframeLogoutChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of IframeLogoutChallenge from a JSON string
iframe_logout_challenge_instance = IframeLogoutChallenge.from_json(json)
# print the JSON string representation of the object
print(IframeLogoutChallenge.to_json())

# convert the object into a dict
iframe_logout_challenge_dict = iframe_logout_challenge_instance.to_dict()
# create an instance of IframeLogoutChallenge from a dict
iframe_logout_challenge_from_dict = IframeLogoutChallenge.from_dict(iframe_logout_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


