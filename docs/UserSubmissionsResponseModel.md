# UserSubmissionsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submissions** | [**List[Submission]**](Submission.md) |  | 

## Example

```python
from openapi_client.models.user_submissions_response_model import UserSubmissionsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubmissionsResponseModel from a JSON string
user_submissions_response_model_instance = UserSubmissionsResponseModel.from_json(json)
# print the JSON string representation of the object
print(UserSubmissionsResponseModel.to_json())

# convert the object into a dict
user_submissions_response_model_dict = user_submissions_response_model_instance.to_dict()
# create an instance of UserSubmissionsResponseModel from a dict
user_submissions_response_model_from_dict = UserSubmissionsResponseModel.from_dict(user_submissions_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


