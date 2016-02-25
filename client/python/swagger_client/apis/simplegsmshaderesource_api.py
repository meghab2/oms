# coding: utf-8

"""
SimplegsmshaderesourceApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SimplegsmshaderesourceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_all_simple_gsm_shades_using_get(self, **kwargs):
        """
        getAllSimpleGsmShades
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_simple_gsm_shades_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[SimpleGsmShade]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_simple_gsm_shades_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/simpleGsmShades'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='list[SimpleGsmShade]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_simple_gsm_shade_using_put(self, simple_gsm_shade, **kwargs):
        """
        updateSimpleGsmShade
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_simple_gsm_shade_using_put(simple_gsm_shade, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SimpleGsmShade simple_gsm_shade: simpleGsmShade (required)
        :return: SimpleGsmShade
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['simple_gsm_shade']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_simple_gsm_shade_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'simple_gsm_shade' is set
        if ('simple_gsm_shade' not in params) or (params['simple_gsm_shade'] is None):
            raise ValueError("Missing the required parameter `simple_gsm_shade` when calling `update_simple_gsm_shade_using_put`")

        resource_path = '/api/simpleGsmShades'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        files = {}

        body_params = None
        if 'simple_gsm_shade' in params:
            body_params = params['simple_gsm_shade']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='SimpleGsmShade',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_simple_gsm_shade_using_post(self, simple_gsm_shade, **kwargs):
        """
        createSimpleGsmShade
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_simple_gsm_shade_using_post(simple_gsm_shade, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SimpleGsmShade simple_gsm_shade: simpleGsmShade (required)
        :return: SimpleGsmShade
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['simple_gsm_shade']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_simple_gsm_shade_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'simple_gsm_shade' is set
        if ('simple_gsm_shade' not in params) or (params['simple_gsm_shade'] is None):
            raise ValueError("Missing the required parameter `simple_gsm_shade` when calling `create_simple_gsm_shade_using_post`")

        resource_path = '/api/simpleGsmShades'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        files = {}

        body_params = None
        if 'simple_gsm_shade' in params:
            body_params = params['simple_gsm_shade']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='SimpleGsmShade',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_simple_gsm_shade_using_get(self, id, **kwargs):
        """
        getSimpleGsmShade
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_simple_gsm_shade_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: SimpleGsmShade
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_simple_gsm_shade_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_simple_gsm_shade_using_get`")

        resource_path = '/api/simpleGsmShades/{id}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='SimpleGsmShade',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_simple_gsm_shade_using_delete(self, id, **kwargs):
        """
        deleteSimpleGsmShade
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_simple_gsm_shade_using_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_simple_gsm_shade_using_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_simple_gsm_shade_using_delete`")

        resource_path = '/api/simpleGsmShades/{id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response