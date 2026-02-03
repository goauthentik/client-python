# OperatingSystem

For example: {\"family\":\"linux\",\"name\":\"Ubuntu\",\"version\":\"24.04.3 LTS (Noble Numbat)\",\"arch\":\"amd64\"} {\"family\": \"windows\",\"name\":\"Server 2022 Datacenter\",\"version\":\"10.0.20348.4405\",\"arch\":\"amd64\"} {\"family\": \"windows\",\"name\":\"Server 2022 Datacenter\",\"version\":\"10.0.20348.4405\",\"arch\":\"amd64\"} {\"family\": \"mac_os\", \"name\": \"\", \"version\": \"26.2\", \"arch\": \"arm64\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | [**DeviceFactsOSFamily**](DeviceFactsOSFamily.md) |  | 
**name** | **str** | Operating System name, such as &#39;Server 2022&#39; or &#39;Ubuntu&#39; | [optional] 
**version** | **str** | Operating System version, must always be the version number but may contain build name | [optional] 
**arch** | **str** |  | 

## Example

```python
from authentik_client.models.operating_system import OperatingSystem

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystem from a JSON string
operating_system_instance = OperatingSystem.from_json(json)
# print the JSON string representation of the object
print(OperatingSystem.to_json())

# convert the object into a dict
operating_system_dict = operating_system_instance.to_dict()
# create an instance of OperatingSystem from a dict
operating_system_from_dict = OperatingSystem.from_dict(operating_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


