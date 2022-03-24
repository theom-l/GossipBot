# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEvaluation
# Creates a new Evaluation of an MLModel.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateEvaluation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateEvaluation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateEvaluation, self).__init__(temboo_session, '/Library/Amazon/MachineLearning/CreateEvaluation')


    def new_input_set(self):
        return CreateEvaluationInputSet()

    def _make_result_set(self, result, path):
        return CreateEvaluationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEvaluationChoreographyExecution(session, exec_id, path)

class CreateEvaluationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateEvaluation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateEvaluationInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateEvaluationInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_EvaluationDataSourceId(self, value):
        """
        Set the value of the EvaluationDataSourceId input for this Choreo. ((required, string) The DataSource that points to the training data.)
        """
        super(CreateEvaluationInputSet, self)._set_input('EvaluationDataSourceId', value)
    def set_EvaluationId(self, value):
        """
        Set the value of the EvaluationId input for this Choreo. ((required, string) A user-supplied identifier that uniquely identifies the MLModel.)
        """
        super(CreateEvaluationInputSet, self)._set_input('EvaluationId', value)
    def set_EvaluationName(self, value):
        """
        Set the value of the EvaluationName input for this Choreo. ((optional, string) A user-supplied name or description of the MLModel.)
        """
        super(CreateEvaluationInputSet, self)._set_input('EvaluationName', value)
    def set_MLModelId(self, value):
        """
        Set the value of the MLModelId input for this Choreo. ((required, string) The ID of the MLModel to evaluate.)
        """
        super(CreateEvaluationInputSet, self)._set_input('MLModelId', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(CreateEvaluationInputSet, self)._set_input('UserRegion', value)

class CreateEvaluationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateEvaluation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateEvaluationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateEvaluationResultSet(response, path)
