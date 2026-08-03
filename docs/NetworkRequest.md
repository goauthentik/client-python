# NetworkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | 
**firewall_enabled** | **bool** |  | [optional] 
**interfaces** | [**List[NetworkInterfaceRequest]**](NetworkInterfaceRequest.md) |  | 
**gateway** | **str** |  | [optional] 

## Example

```python
from authentik_client.models.network_request import NetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRequest from a JSON string
network_request_instance = NetworkRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkRequest.to_json())

# convert the object into a dict
network_request_dict = network_request_instance.to_dict()
# create an instance of NetworkRequest from a dict
network_request_from_dict = NetworkRequest.from_dict(network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


