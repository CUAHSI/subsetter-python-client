# openapi_client.ArgoApi

All URIs are relative to *https://subsetter-api-jbzfw6l52q-uc.a.run.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**argo_metadata_argo_workflow_id_get**](ArgoApi.md#argo_metadata_argo_workflow_id_get) | **GET** /argo/{workflow_id} | Argo Metadata
[**extract_metadata_extract_metadata_post**](ArgoApi.md#extract_metadata_extract_metadata_post) | **POST** /extract/metadata | Extract Metadata
[**logs_logs_workflow_id_get**](ArgoApi.md#logs_logs_workflow_id_get) | **GET** /logs/{workflow_id} | Logs
[**refresh_workflow_refresh_get**](ArgoApi.md#refresh_workflow_refresh_get) | **GET** /refresh | Refresh Workflow
[**refresh_workflow_refresh_workflow_id_get**](ArgoApi.md#refresh_workflow_refresh_workflow_id_get) | **GET** /refresh/{workflow_id} | Refresh Workflow
[**submissions_submissions_get**](ArgoApi.md#submissions_submissions_get) | **GET** /submissions | Submissions
[**submit_nwm_submit_nwm_post**](ArgoApi.md#submit_nwm_submit_nwm_post) | **POST** /submit/nwm | Submit Nwm
[**submit_parflow_submit_parflow_post**](ArgoApi.md#submit_parflow_submit_parflow_post) | **POST** /submit/parflow | Submit Parflow


# **argo_metadata_argo_workflow_id_get**
> object argo_metadata_argo_workflow_id_get(workflow_id)

Argo Metadata

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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
    except Exception as e:
        print("Exception when calling ArgoApi->argo_metadata_argo_workflow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| The id of the workflow | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_metadata_extract_metadata_post**
> object extract_metadata_extract_metadata_post(extract_metadata_request_body)

Extract Metadata

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.extract_metadata_request_body import ExtractMetadataRequestBody
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
    extract_metadata_request_body = openapi_client.ExtractMetadataRequestBody() # ExtractMetadataRequestBody | 

    try:
        # Extract Metadata
        api_response = api_instance.extract_metadata_extract_metadata_post(extract_metadata_request_body)
        print("The response of ArgoApi->extract_metadata_extract_metadata_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->extract_metadata_extract_metadata_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_metadata_request_body** | [**ExtractMetadataRequestBody**](ExtractMetadataRequestBody.md)|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logs_logs_workflow_id_get**
> LogsResponseModel logs_logs_workflow_id_get(workflow_id)

Logs

logs for a workflow

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.logs_response_model import LogsResponseModel
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
        # Logs
        api_response = api_instance.logs_logs_workflow_id_get(workflow_id)
        print("The response of ArgoApi->logs_logs_workflow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->logs_logs_workflow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| The id of the workflow | 

### Return type

[**LogsResponseModel**](LogsResponseModel.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_workflow_refresh_get**
> object refresh_workflow_refresh_get()

Refresh Workflow

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

    try:
        # Refresh Workflow
        api_response = api_instance.refresh_workflow_refresh_get()
        print("The response of ArgoApi->refresh_workflow_refresh_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->refresh_workflow_refresh_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_workflow_refresh_workflow_id_get**
> object refresh_workflow_refresh_workflow_id_get(workflow_id)

Refresh Workflow

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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
        # Refresh Workflow
        api_response = api_instance.refresh_workflow_refresh_workflow_id_get(workflow_id)
        print("The response of ArgoApi->refresh_workflow_refresh_workflow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->refresh_workflow_refresh_workflow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| The id of the workflow | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_submissions_get**
> UserSubmissionsResponseModel submissions_submissions_get()

Submissions

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.user_submissions_response_model import UserSubmissionsResponseModel
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

    try:
        # Submissions
        api_response = api_instance.submissions_submissions_get()
        print("The response of ArgoApi->submissions_submissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->submissions_submissions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserSubmissionsResponseModel**](UserSubmissionsResponseModel.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_nwm_submit_nwm_post**
> SubmissionResponseModel submit_nwm_submit_nwm_post(y_south, x_west, y_north, x_east, model_version)

Submit Nwm

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.nwm_version_enum import NWMVersionEnum
from openapi_client.models.submission_response_model import SubmissionResponseModel
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
    y_south = 3.4 # float | 
    x_west = 3.4 # float | 
    y_north = 3.4 # float | 
    x_east = 3.4 # float | 
    model_version = openapi_client.NWMVersionEnum() # NWMVersionEnum | 

    try:
        # Submit Nwm
        api_response = api_instance.submit_nwm_submit_nwm_post(y_south, x_west, y_north, x_east, model_version)
        print("The response of ArgoApi->submit_nwm_submit_nwm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->submit_nwm_submit_nwm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **y_south** | **float**|  | 
 **x_west** | **float**|  | 
 **y_north** | **float**|  | 
 **x_east** | **float**|  | 
 **model_version** | [**NWMVersionEnum**](.md)|  | 

### Return type

[**SubmissionResponseModel**](SubmissionResponseModel.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_parflow_submit_parflow_post**
> SubmissionResponseModel submit_parflow_submit_parflow_post(hucs)

Submit Parflow

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import openapi_client
from openapi_client.models.submission_response_model import SubmissionResponseModel
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
    hucs = ['hucs_example'] # List[str] | 

    try:
        # Submit Parflow
        api_response = api_instance.submit_parflow_submit_parflow_post(hucs)
        print("The response of ArgoApi->submit_parflow_submit_parflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArgoApi->submit_parflow_submit_parflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hucs** | [**List[str]**](str.md)|  | 

### Return type

[**SubmissionResponseModel**](SubmissionResponseModel.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

