# openapi_client.MinioApi

All URIs are relative to *https://subsetter-api-jbzfw6l52q-uc.a.run.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_and_save_user_policy_policy_minio_cuahsi_get**](MinioApi.md#generate_and_save_user_policy_policy_minio_cuahsi_get) | **GET** /policy/minio/cuahsi | Generate And Save User Policy
[**generate_user_policy_policy_get**](MinioApi.md#generate_user_policy_policy_get) | **GET** /policy | Generate User Policy
[**presigned_get_minio_presigned_get_workflow_id_get**](MinioApi.md#presigned_get_minio_presigned_get_workflow_id_get) | **GET** /presigned/get/{workflow_id} | Presigned Get Minio
[**presigned_get_url_url_workflow_id_get**](MinioApi.md#presigned_get_url_url_workflow_id_get) | **GET** /url/{workflow_id} | Presigned Get Url
[**presigned_put_minio_presigned_put_bucket_get**](MinioApi.md#presigned_put_minio_presigned_put_bucket_get) | **GET** /presigned/put/{bucket} | Presigned Put Minio
[**refresh_profile_profile_get**](MinioApi.md#refresh_profile_profile_get) | **GET** /profile | Refresh Profile


# **generate_and_save_user_policy_policy_minio_cuahsi_get**
> object generate_and_save_user_policy_policy_minio_cuahsi_get()

Generate And Save User Policy

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
    api_instance = openapi_client.MinioApi(api_client)

    try:
        # Generate And Save User Policy
        api_response = api_instance.generate_and_save_user_policy_policy_minio_cuahsi_get()
        print("The response of MinioApi->generate_and_save_user_policy_policy_minio_cuahsi_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinioApi->generate_and_save_user_policy_policy_minio_cuahsi_get: %s\n" % e)
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

# **generate_user_policy_policy_get**
> object generate_user_policy_policy_get()

Generate User Policy

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
    api_instance = openapi_client.MinioApi(api_client)

    try:
        # Generate User Policy
        api_response = api_instance.generate_user_policy_policy_get()
        print("The response of MinioApi->generate_user_policy_policy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinioApi->generate_user_policy_policy_get: %s\n" % e)
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

# **presigned_get_minio_presigned_get_workflow_id_get**
> object presigned_get_minio_presigned_get_workflow_id_get(workflow_id)

Presigned Get Minio

Create a download url

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
    api_instance = openapi_client.MinioApi(api_client)
    workflow_id = 'workflow_id_example' # str | The id of the workflow

    try:
        # Presigned Get Minio
        api_response = api_instance.presigned_get_minio_presigned_get_workflow_id_get(workflow_id)
        print("The response of MinioApi->presigned_get_minio_presigned_get_workflow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinioApi->presigned_get_minio_presigned_get_workflow_id_get: %s\n" % e)
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

# **presigned_get_url_url_workflow_id_get**
> object presigned_get_url_url_workflow_id_get(workflow_id)

Presigned Get Url

Create a download url

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
    api_instance = openapi_client.MinioApi(api_client)
    workflow_id = 'workflow_id_example' # str | The id of the workflow

    try:
        # Presigned Get Url
        api_response = api_instance.presigned_get_url_url_workflow_id_get(workflow_id)
        print("The response of MinioApi->presigned_get_url_url_workflow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinioApi->presigned_get_url_url_workflow_id_get: %s\n" % e)
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

# **presigned_put_minio_presigned_put_bucket_get**
> object presigned_put_minio_presigned_put_bucket_get(bucket, path)

Presigned Put Minio

Create a PUT file presigned url

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subsetter-api-jbzfw6l52q-uc.a.run.app
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subsetter-api-jbzfw6l52q-uc.a.run.app"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MinioApi(api_client)
    bucket = 'bucket_example' # str | 
    path = 'path_example' # str | 

    try:
        # Presigned Put Minio
        api_response = api_instance.presigned_put_minio_presigned_put_bucket_get(bucket, path)
        print("The response of MinioApi->presigned_put_minio_presigned_put_bucket_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinioApi->presigned_put_minio_presigned_put_bucket_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **path** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_profile_profile_get**
> object refresh_profile_profile_get()

Refresh Profile

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
    api_instance = openapi_client.MinioApi(api_client)

    try:
        # Refresh Profile
        api_response = api_instance.refresh_profile_profile_get()
        print("The response of MinioApi->refresh_profile_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinioApi->refresh_profile_profile_get: %s\n" % e)
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

