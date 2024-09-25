# LogsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | **str** | The logs for a workflow submission | 

## Example

```python
from openapi_client.models.logs_response_model import LogsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of LogsResponseModel from a JSON string
logs_response_model_instance = LogsResponseModel.from_json(json)
# print the JSON string representation of the object
print(LogsResponseModel.to_json())

# convert the object into a dict
logs_response_model_dict = logs_response_model_instance.to_dict()
# create an instance of LogsResponseModel from a dict
logs_response_model_from_dict = LogsResponseModel.from_dict(logs_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


