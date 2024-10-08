# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.9.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Build with docker
```sh
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i https://subsetter-api-jbzfw6l52q-uc.a.run.app/openapi.json \
    -g python \
    -o /local
```

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/CUAHSI/subsetter-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subsetter-api-jbzfw6l52q-uc.a.run.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subsetter-api-jbzfw6l52q-uc.a.run.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ArgoApi(api_client)
    workflow_id = 'workflow_id_example' # str | The id of the workflow

    try:
        # Argo Metadata
        api_response = api_instance.argo_metadata_argo_workflow_id_get(workflow_id)
        print("The response of ArgoApi->argo_metadata_argo_workflow_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArgoApi->argo_metadata_argo_workflow_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://subsetter-api-jbzfw6l52q-uc.a.run.app*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArgoApi* | [**argo_metadata_argo_workflow_id_get**](docs/ArgoApi.md#argo_metadata_argo_workflow_id_get) | **GET** /argo/{workflow_id} | Argo Metadata
*ArgoApi* | [**extract_metadata_extract_metadata_post**](docs/ArgoApi.md#extract_metadata_extract_metadata_post) | **POST** /extract/metadata | Extract Metadata
*ArgoApi* | [**logs_logs_workflow_id_get**](docs/ArgoApi.md#logs_logs_workflow_id_get) | **GET** /logs/{workflow_id} | Logs
*ArgoApi* | [**refresh_workflow_refresh_get**](docs/ArgoApi.md#refresh_workflow_refresh_get) | **GET** /refresh | Refresh Workflow
*ArgoApi* | [**refresh_workflow_refresh_workflow_id_get**](docs/ArgoApi.md#refresh_workflow_refresh_workflow_id_get) | **GET** /refresh/{workflow_id} | Refresh Workflow
*ArgoApi* | [**submissions_submissions_get**](docs/ArgoApi.md#submissions_submissions_get) | **GET** /submissions | Submissions
*ArgoApi* | [**submit_nwm_submit_nwm_post**](docs/ArgoApi.md#submit_nwm_submit_nwm_post) | **POST** /submit/nwm | Submit Nwm
*ArgoApi* | [**submit_parflow_submit_parflow_post**](docs/ArgoApi.md#submit_parflow_submit_parflow_post) | **POST** /submit/parflow | Submit Parflow
*AuthApi* | [**oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get**](docs/AuthApi.md#oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get) | **GET** /auth/cuahsi/authorize | Oauth:Oauth2.Jwt.Authorize
*AuthApi* | [**oauth_oauth2_jwt_authorize_auth_front_authorize_get**](docs/AuthApi.md#oauth_oauth2_jwt_authorize_auth_front_authorize_get) | **GET** /auth/front/authorize | Oauth:Oauth2.Jwt.Authorize
*AuthApi* | [**oauth_oauth2_jwt_callback_auth_cuahsi_callback_get**](docs/AuthApi.md#oauth_oauth2_jwt_callback_auth_cuahsi_callback_get) | **GET** /auth/cuahsi/callback | Oauth:Oauth2.Jwt.Callback
*AuthApi* | [**oauth_oauth2_jwt_callback_auth_front_callback_get**](docs/AuthApi.md#oauth_oauth2_jwt_callback_auth_front_callback_get) | **GET** /auth/front/callback | Oauth:Oauth2.Jwt.Callback
*HydroshareApi* | [**create_metadata_dataset_metadata_post**](docs/HydroshareApi.md#create_metadata_dataset_metadata_post) | **POST** /dataset/metadata | Create Metadata
*HydroshareApi* | [**update_metadata_dataset_metadata_put**](docs/HydroshareApi.md#update_metadata_dataset_metadata_put) | **PUT** /dataset/metadata | Update Metadata
*MinioApi* | [**generate_and_save_user_policy_policy_minio_cuahsi_get**](docs/MinioApi.md#generate_and_save_user_policy_policy_minio_cuahsi_get) | **GET** /policy/minio/cuahsi | Generate And Save User Policy
*MinioApi* | [**generate_user_policy_policy_get**](docs/MinioApi.md#generate_user_policy_policy_get) | **GET** /policy | Generate User Policy
*MinioApi* | [**presigned_get_minio_presigned_get_workflow_id_get**](docs/MinioApi.md#presigned_get_minio_presigned_get_workflow_id_get) | **GET** /presigned/get/{workflow_id} | Presigned Get Minio
*MinioApi* | [**presigned_get_url_url_workflow_id_get**](docs/MinioApi.md#presigned_get_url_url_workflow_id_get) | **GET** /url/{workflow_id} | Presigned Get Url
*MinioApi* | [**presigned_put_minio_presigned_put_bucket_get**](docs/MinioApi.md#presigned_put_minio_presigned_put_bucket_get) | **GET** /presigned/put/{bucket} | Presigned Put Minio
*MinioApi* | [**refresh_profile_profile_get**](docs/MinioApi.md#refresh_profile_profile_get) | **GET** /profile | Refresh Profile
*UsersApi* | [**users_current_user_users_me_get**](docs/UsersApi.md#users_current_user_users_me_get) | **GET** /users/me | Users:Current User
*UsersApi* | [**users_delete_user_users_id_delete**](docs/UsersApi.md#users_delete_user_users_id_delete) | **DELETE** /users/{id} | Users:Delete User
*UsersApi* | [**users_patch_current_user_users_me_patch**](docs/UsersApi.md#users_patch_current_user_users_me_patch) | **PATCH** /users/me | Users:Patch Current User
*UsersApi* | [**users_patch_user_users_id_patch**](docs/UsersApi.md#users_patch_user_users_id_patch) | **PATCH** /users/{id} | Users:Patch User
*UsersApi* | [**users_user_users_id_get**](docs/UsersApi.md#users_user_users_id_get) | **GET** /users/{id} | Users:User
*UtilitiesApi* | [**compute_nwm_bbox_nwm_compute_bbox_post**](docs/UtilitiesApi.md#compute_nwm_bbox_nwm_compute_bbox_post) | **POST** /nwm/compute_bbox | Compute Nwm Bbox


## Documentation For Models

 - [DatasetMetadataRequestModel](docs/DatasetMetadataRequestModel.md)
 - [Detail](docs/Detail.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [ExtractMetadataRequestBody](docs/ExtractMetadataRequestBody.md)
 - [GeoJsonFeature](docs/GeoJsonFeature.md)
 - [GeoJsonFeatureCollection](docs/GeoJsonFeatureCollection.md)
 - [GeoJsonGeometry](docs/GeoJsonGeometry.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HydroShareMetadata](docs/HydroShareMetadata.md)
 - [LogsResponseModel](docs/LogsResponseModel.md)
 - [NWMVersionEnum](docs/NWMVersionEnum.md)
 - [OAuth2AuthorizeResponse](docs/OAuth2AuthorizeResponse.md)
 - [PhaseEnum](docs/PhaseEnum.md)
 - [Submission](docs/Submission.md)
 - [SubmissionResponseModel](docs/SubmissionResponseModel.md)
 - [UserRead](docs/UserRead.md)
 - [UserSubmissionsResponseModel](docs/UserSubmissionsResponseModel.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="OAuth2PasswordBearer"></a>
### OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




