# -*- coding: utf-8 -*-
"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from models import *


class CompareApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient

    

    def compare(self, retina_name, body, ):
        """Compare 2 elements
        Args:
            body, ExpressionOperation: The JSON encoded comparison array to be evaluated (required)
            retina_name, str: The retina name (required)
            Returns: Metric
        """

        resourcePath = '/compare'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return apiMetric.Metric(**response.json())

    


