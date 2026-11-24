# NotificationRule

NotificationRule Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **UUID** |  | [readonly] 
**name** | **str** |  | 
**transports** | **List[UUID]** | Select which transports should be used to notify the user. If none are selected, the notification will only be shown in the authentik UI. | [optional] 
**severity** | [**SeverityEnum**](SeverityEnum.md) | Controls which severity level the created notifications will have. | [optional] 
**destination_group** | **UUID** | Define which group of users this notification should be sent and shown to. If left empty, Notification won&#39;t ben sent. | [optional] 
**destination_group_obj** | [**Group**](Group.md) |  | [readonly] 
**destination_event_user** | **bool** | When enabled, notification will be sent to user the user that triggered the event.When destination_group is configured, notification is sent to both. | [optional] 

## Example

```python
from authentik_client.models.notification_rule import NotificationRule

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRule from a JSON string
notification_rule_instance = NotificationRule.from_json(json)
# print the JSON string representation of the object
print(NotificationRule.to_json())

# convert the object into a dict
notification_rule_dict = notification_rule_instance.to_dict()
# create an instance of NotificationRule from a dict
notification_rule_from_dict = NotificationRule.from_dict(notification_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


