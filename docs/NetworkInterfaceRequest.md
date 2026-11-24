# NetworkInterfaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**hardware_address** | **str** |  | 
**ip_addresses** | **List[str]** |  | [optional] 
**dns_servers** | **List[str]** |  | [optional] 

## Example

```python
from authentik_client.models.network_interface_request import NetworkInterfaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceRequest from a JSON string
network_interface_request_instance = NetworkInterfaceRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkInterfaceRequest.to_json())

# convert the object into a dict
network_interface_request_dict = network_interface_request_instance.to_dict()
# create an instance of NetworkInterfaceRequest from a dict
network_interface_request_from_dict = NetworkInterfaceRequest.from_dict(network_interface_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


