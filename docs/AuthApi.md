# openapi_client.AuthApi

All URIs are relative to *https://subsetter-api-jbzfw6l52q-uc.a.run.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get**](AuthApi.md#oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get) | **GET** /auth/cuahsi/authorize | Oauth:Oauth2.Jwt.Authorize
[**oauth_oauth2_jwt_authorize_auth_front_authorize_get**](AuthApi.md#oauth_oauth2_jwt_authorize_auth_front_authorize_get) | **GET** /auth/front/authorize | Oauth:Oauth2.Jwt.Authorize
[**oauth_oauth2_jwt_callback_auth_cuahsi_callback_get**](AuthApi.md#oauth_oauth2_jwt_callback_auth_cuahsi_callback_get) | **GET** /auth/cuahsi/callback | Oauth:Oauth2.Jwt.Callback
[**oauth_oauth2_jwt_callback_auth_front_callback_get**](AuthApi.md#oauth_oauth2_jwt_callback_auth_front_callback_get) | **GET** /auth/front/callback | Oauth:Oauth2.Jwt.Callback


# **oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get**
> OAuth2AuthorizeResponse oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get(scopes=scopes)

Oauth:Oauth2.Jwt.Authorize

### Example


```python
import openapi_client
from openapi_client.models.o_auth2_authorize_response import OAuth2AuthorizeResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    scopes = ['scopes_example'] # List[Optional[str]] |  (optional)

    try:
        # Oauth:Oauth2.Jwt.Authorize
        api_response = api_instance.oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get(scopes=scopes)
        print("The response of AuthApi->oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_oauth2_jwt_authorize_auth_cuahsi_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scopes** | [**List[Optional[str]]**](str.md)|  | [optional] 

### Return type

[**OAuth2AuthorizeResponse**](OAuth2AuthorizeResponse.md)

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

# **oauth_oauth2_jwt_authorize_auth_front_authorize_get**
> OAuth2AuthorizeResponse oauth_oauth2_jwt_authorize_auth_front_authorize_get(scopes=scopes)

Oauth:Oauth2.Jwt.Authorize

### Example


```python
import openapi_client
from openapi_client.models.o_auth2_authorize_response import OAuth2AuthorizeResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    scopes = ['scopes_example'] # List[str] |  (optional)

    try:
        # Oauth:Oauth2.Jwt.Authorize
        api_response = api_instance.oauth_oauth2_jwt_authorize_auth_front_authorize_get(scopes=scopes)
        print("The response of AuthApi->oauth_oauth2_jwt_authorize_auth_front_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_oauth2_jwt_authorize_auth_front_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scopes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**OAuth2AuthorizeResponse**](OAuth2AuthorizeResponse.md)

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

# **oauth_oauth2_jwt_callback_auth_cuahsi_callback_get**
> object oauth_oauth2_jwt_callback_auth_cuahsi_callback_get(code=code, code_verifier=code_verifier, state=state, error=error)

Oauth:Oauth2.Jwt.Callback

The response varies based on the authentication backend used.

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
    api_instance = openapi_client.AuthApi(api_client)
    code = 'code_example' # str |  (optional)
    code_verifier = 'code_verifier_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    error = 'error_example' # str |  (optional)

    try:
        # Oauth:Oauth2.Jwt.Callback
        api_response = api_instance.oauth_oauth2_jwt_callback_auth_cuahsi_callback_get(code=code, code_verifier=code_verifier, state=state, error=error)
        print("The response of AuthApi->oauth_oauth2_jwt_callback_auth_cuahsi_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_oauth2_jwt_callback_auth_cuahsi_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code_verifier** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **error** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_oauth2_jwt_callback_auth_front_callback_get**
> object oauth_oauth2_jwt_callback_auth_front_callback_get(code=code, code_verifier=code_verifier, state=state, error=error)

Oauth:Oauth2.Jwt.Callback

The response varies based on the authentication backend used.

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
    api_instance = openapi_client.AuthApi(api_client)
    code = 'code_example' # str |  (optional)
    code_verifier = 'code_verifier_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    error = 'error_example' # str |  (optional)

    try:
        # Oauth:Oauth2.Jwt.Callback
        api_response = api_instance.oauth_oauth2_jwt_callback_auth_front_callback_get(code=code, code_verifier=code_verifier, state=state, error=error)
        print("The response of AuthApi->oauth_oauth2_jwt_callback_auth_front_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_oauth2_jwt_callback_auth_front_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **code_verifier** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **error** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

