# Submission


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
from openapi_client.models.submission import Submission

# TODO update the JSON string below
json = "{}"
# create an instance of Submission from a JSON string
submission_instance = Submission.from_json(json)
# print the JSON string representation of the object
print(Submission.to_json())

# convert the object into a dict
submission_dict = submission_instance.to_dict()
# create an instance of Submission from a dict
submission_from_dict = Submission.from_dict(submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


