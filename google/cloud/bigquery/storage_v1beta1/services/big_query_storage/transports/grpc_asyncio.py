# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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
#

import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.bigquery.storage_v1beta1.types import storage
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import BigQueryStorageTransport, DEFAULT_CLIENT_INFO
from .grpc import BigQueryStorageGrpcTransport


class BigQueryStorageGrpcAsyncIOTransport(BigQueryStorageTransport):
    """gRPC AsyncIO backend transport for BigQueryStorage.

    BigQuery storage API.
    The BigQuery storage API can be used to read data stored in
    BigQuery.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "bigquerystorage.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "bigquerystorage.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        self._stubs = {}

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_read_session(
        self,
    ) -> Callable[[storage.CreateReadSessionRequest], Awaitable[storage.ReadSession]]:
        r"""Return a callable for the create read session method over gRPC.

        Creates a new read session. A read session divides
        the contents of a BigQuery table into one or more
        streams, which can then be used to read data from the
        table. The read session also specifies properties of the
        data to be read, such as a list of columns or a push-
        down filter describing the rows to be returned.

        A particular row can be read by at most one stream. When
        the caller has reached the end of each stream in the
        session, then all the data in the table has been read.

        Read sessions automatically expire 24 hours after they
        are created and do not require manual clean-up by the
        caller.

        Returns:
            Callable[[~.CreateReadSessionRequest],
                    Awaitable[~.ReadSession]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_read_session" not in self._stubs:
            self._stubs["create_read_session"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1beta1.BigQueryStorage/CreateReadSession",
                request_serializer=storage.CreateReadSessionRequest.serialize,
                response_deserializer=storage.ReadSession.deserialize,
            )
        return self._stubs["create_read_session"]

    @property
    def read_rows(
        self,
    ) -> Callable[[storage.ReadRowsRequest], Awaitable[storage.ReadRowsResponse]]:
        r"""Return a callable for the read rows method over gRPC.

        Reads rows from the table in the format prescribed by
        the read session. Each response contains one or more
        table rows, up to a maximum of 10 MiB per response; read
        requests which attempt to read individual rows larger
        than this will fail.

        Each request also returns a set of stream statistics
        reflecting the estimated total number of rows in the
        read stream. This number is computed based on the total
        table size and the number of active streams in the read
        session, and may change as other streams continue to
        read data.

        Returns:
            Callable[[~.ReadRowsRequest],
                    Awaitable[~.ReadRowsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "read_rows" not in self._stubs:
            self._stubs["read_rows"] = self.grpc_channel.unary_stream(
                "/google.cloud.bigquery.storage.v1beta1.BigQueryStorage/ReadRows",
                request_serializer=storage.ReadRowsRequest.serialize,
                response_deserializer=storage.ReadRowsResponse.deserialize,
            )
        return self._stubs["read_rows"]

    @property
    def batch_create_read_session_streams(
        self,
    ) -> Callable[
        [storage.BatchCreateReadSessionStreamsRequest],
        Awaitable[storage.BatchCreateReadSessionStreamsResponse],
    ]:
        r"""Return a callable for the batch create read session
        streams method over gRPC.

        Creates additional streams for a ReadSession. This
        API can be used to dynamically adjust the parallelism of
        a batch processing task upwards by adding additional
        workers.

        Returns:
            Callable[[~.BatchCreateReadSessionStreamsRequest],
                    Awaitable[~.BatchCreateReadSessionStreamsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_read_session_streams" not in self._stubs:
            self._stubs[
                "batch_create_read_session_streams"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1beta1.BigQueryStorage/BatchCreateReadSessionStreams",
                request_serializer=storage.BatchCreateReadSessionStreamsRequest.serialize,
                response_deserializer=storage.BatchCreateReadSessionStreamsResponse.deserialize,
            )
        return self._stubs["batch_create_read_session_streams"]

    @property
    def finalize_stream(
        self,
    ) -> Callable[[storage.FinalizeStreamRequest], Awaitable[empty.Empty]]:
        r"""Return a callable for the finalize stream method over gRPC.

        Triggers the graceful termination of a single stream
        in a ReadSession. This API can be used to dynamically
        adjust the parallelism of a batch processing task
        downwards without losing data.

        This API does not delete the stream -- it remains
        visible in the ReadSession, and any data processed by
        the stream is not released to other streams. However, no
        additional data will be assigned to the stream once this
        call completes. Callers must continue reading data on
        the stream until the end of the stream is reached so
        that data which has already been assigned to the stream
        will be processed.

        This method will return an error if there are no other
        live streams in the Session, or if SplitReadStream() has
        been called on the given Stream.

        Returns:
            Callable[[~.FinalizeStreamRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "finalize_stream" not in self._stubs:
            self._stubs["finalize_stream"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1beta1.BigQueryStorage/FinalizeStream",
                request_serializer=storage.FinalizeStreamRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["finalize_stream"]

    @property
    def split_read_stream(
        self,
    ) -> Callable[
        [storage.SplitReadStreamRequest], Awaitable[storage.SplitReadStreamResponse]
    ]:
        r"""Return a callable for the split read stream method over gRPC.

        Splits a given read stream into two Streams. These streams are
        referred to as the primary and the residual of the split. The
        original stream can still be read from in the same manner as
        before. Both of the returned streams can also be read from, and
        the total rows return by both child streams will be the same as
        the rows read from the original stream.

        Moreover, the two child streams will be allocated back to back
        in the original Stream. Concretely, it is guaranteed that for
        streams Original, Primary, and Residual, that Original[0-j] =
        Primary[0-j] and Original[j-n] = Residual[0-m] once the streams
        have been read to completion.

        This method is guaranteed to be idempotent.

        Returns:
            Callable[[~.SplitReadStreamRequest],
                    Awaitable[~.SplitReadStreamResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "split_read_stream" not in self._stubs:
            self._stubs["split_read_stream"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1beta1.BigQueryStorage/SplitReadStream",
                request_serializer=storage.SplitReadStreamRequest.serialize,
                response_deserializer=storage.SplitReadStreamResponse.deserialize,
            )
        return self._stubs["split_read_stream"]


__all__ = ("BigQueryStorageGrpcAsyncIOTransport",)
