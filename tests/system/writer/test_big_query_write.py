# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from google.cloud.bigquery_storage_v1beta2.services import big_query_write
from . import messages_pb2


@pytest.fixture(scope="session")
def write_client():
    return big_query_write.BigQueryWriteClient()


def test_bare_metal_streaming(write_client):
    # TODO create table with name:string, value:int64
    test_data = [
        messages_pb2.SimpleMessage(name="one", value=1),
        messages_pb2.SimpleMessage(name="two", value=2),
        messages_pb2.SimpleMessage(name="three", value=3),
    ]

