# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KMeans.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cKMeans.proto\"I\n\nMapRequest\x12\x15\n\rcentroid_list\x18\x01 \x01(\t\x12\x19\n\x11\x64\x61ta_chunks_index\x18\x02 \x01(\t\x12\t\n\x01R\x18\x03 \x01(\x05\"\x1e\n\x0bMapResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"7\n\rReduceRequest\x12\x13\n\x0bmapper_port\x18\x01 \x03(\t\x12\x11\n\tpartition\x18\x02 \x01(\x05\"7\n\x0eReduceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x14\n\x0coutput_files\x18\x02 \x01(\t\"\'\n\x0bReadRequest\x12\x18\n\x10partition_number\x18\x01 \x01(\x05\"\x1c\n\x0cReadResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t2X\n\x06Mapper\x12$\n\x07MapTask\x12\x0b.MapRequest\x1a\x0c.MapResponse\x12(\n\tServeData\x12\x0c.ReadRequest\x1a\r.ReadResponse2:\n\x07Reducer\x12/\n\nReduceTask\x12\x0e.ReduceRequest\x1a\x0f.ReduceResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'KMeans_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MAPREQUEST']._serialized_start=16
  _globals['_MAPREQUEST']._serialized_end=89
  _globals['_MAPRESPONSE']._serialized_start=91
  _globals['_MAPRESPONSE']._serialized_end=121
  _globals['_REDUCEREQUEST']._serialized_start=123
  _globals['_REDUCEREQUEST']._serialized_end=178
  _globals['_REDUCERESPONSE']._serialized_start=180
  _globals['_REDUCERESPONSE']._serialized_end=235
  _globals['_READREQUEST']._serialized_start=237
  _globals['_READREQUEST']._serialized_end=276
  _globals['_READRESPONSE']._serialized_start=278
  _globals['_READRESPONSE']._serialized_end=306
  _globals['_MAPPER']._serialized_start=308
  _globals['_MAPPER']._serialized_end=396
  _globals['_REDUCER']._serialized_start=398
  _globals['_REDUCER']._serialized_end=456
# @@protoc_insertion_point(module_scope)
