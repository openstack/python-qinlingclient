# Copyright 2017 Catalyst IT Limited
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from qinlingclient.common import http
from qinlingclient.v1 import function
from qinlingclient.v1 import runtime


class Client(object):
    """Client for the Qinling v1 API.

    :param string endpoint: A user-supplied endpoint URL for the service.
    :param string token: Token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the Qinling v1 API."""
        self.http_client = http._construct_http_client(*args, **kwargs)

        self.runtimes = runtime.RuntimeManager(self.http_client)
        self.functions = function.FunctionManager(self.http_client)
        # self.function_executions = function_executions.ExecutionManager(
        #     self.http_client)
