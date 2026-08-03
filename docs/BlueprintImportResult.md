# BlueprintImportResult

Logs of an attempted blueprint import

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[LogEvent]**](LogEvent.md) |  | [readonly] 
**success** | **bool** |  | [readonly] 

## Example

```python
from authentik_client.models.blueprint_import_result import BlueprintImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintImportResult from a JSON string
blueprint_import_result_instance = BlueprintImportResult.from_json(json)
# print the JSON string representation of the object
print(BlueprintImportResult.to_json())

# convert the object into a dict
blueprint_import_result_dict = blueprint_import_result_instance.to_dict()
# create an instance of BlueprintImportResult from a dict
blueprint_import_result_from_dict = BlueprintImportResult.from_dict(blueprint_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


