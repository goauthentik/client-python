# GroupSAMLSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**source** | **str** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_saml_source_connection_request import GroupSAMLSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSAMLSourceConnectionRequest from a JSON string
group_saml_source_connection_request_instance = GroupSAMLSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupSAMLSourceConnectionRequest.to_json())

# convert the object into a dict
group_saml_source_connection_request_dict = group_saml_source_connection_request_instance.to_dict()
# create an instance of GroupSAMLSourceConnectionRequest from a dict
group_saml_source_connection_request_from_dict = GroupSAMLSourceConnectionRequest.from_dict(group_saml_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


