# SubmissionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | 
**workflow_name** | **str** |  | 
**phase** | [**PhaseEnum**](PhaseEnum.md) |  | [optional] 
**started_at** | **str** |  | [optional] 
**finished_at** | **str** |  | [optional] 
**estimated_duration** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.submission_response_model import SubmissionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponseModel from a JSON string
submission_response_model_instance = SubmissionResponseModel.from_json(json)
# print the JSON string representation of the object
print(SubmissionResponseModel.to_json())

# convert the object into a dict
submission_response_model_dict = submission_response_model_instance.to_dict()
# create an instance of SubmissionResponseModel from a dict
submission_response_model_from_dict = SubmissionResponseModel.from_dict(submission_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


