# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: school_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14school_service.proto\x12\x0eschool_service\"6\n\x10GetSchoolRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xab\x01\n\x11GetSchoolResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x15\n\rsession_state\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x16\n\x0eschool_user_id\x18\x05 \x01(\t\x12\x11\n\tcoalition\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\"$\n\x0cGetRpRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"}\n\rGetRpResponse\x12\x0b\n\x03\x63rp\x18\x01 \x01(\x05\x12\r\n\x05\x63oins\x18\x02 \x01(\x05\x12\x0b\n\x03prp\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x12\n\nfirst_name\x18\x05 \x01(\t\x12\x11\n\tlast_name\x18\x06 \x01(\t\x12\r\n\x05login\x18\x07 \x01(\t\"W\n GetAllMembersFromPlatformRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\"/\n\x06Member\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\x12\r\n\x05login\x18\x02 \x01(\t\"q\n!GetAllMembersFromPlatformResponse\x12\'\n\x07members\x18\x01 \x03(\x0b\x32\x16.school_service.Member\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t2\xc0\x02\n\rSchoolService\x12X\n\x0fget_school_info\x12 .school_service.GetSchoolRequest\x1a!.school_service.GetSchoolResponse\"\x00\x12L\n\x0bget_rp_info\x12\x1c.school_service.GetRpRequest\x1a\x1d.school_service.GetRpResponse\"\x00\x12\x86\x01\n\x1dget_all_members_from_platform\x12\x30.school_service.GetAllMembersFromPlatformRequest\x1a\x31.school_service.GetAllMembersFromPlatformResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'school_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETSCHOOLREQUEST']._serialized_start=40
  _globals['_GETSCHOOLREQUEST']._serialized_end=94
  _globals['_GETSCHOOLRESPONSE']._serialized_start=97
  _globals['_GETSCHOOLRESPONSE']._serialized_end=268
  _globals['_GETRPREQUEST']._serialized_start=270
  _globals['_GETRPREQUEST']._serialized_end=306
  _globals['_GETRPRESPONSE']._serialized_start=308
  _globals['_GETRPRESPONSE']._serialized_end=433
  _globals['_GETALLMEMBERSFROMPLATFORMREQUEST']._serialized_start=435
  _globals['_GETALLMEMBERSFROMPLATFORMREQUEST']._serialized_end=522
  _globals['_MEMBER']._serialized_start=524
  _globals['_MEMBER']._serialized_end=571
  _globals['_GETALLMEMBERSFROMPLATFORMRESPONSE']._serialized_start=573
  _globals['_GETALLMEMBERSFROMPLATFORMRESPONSE']._serialized_end=686
  _globals['_SCHOOLSERVICE']._serialized_start=689
  _globals['_SCHOOLSERVICE']._serialized_end=1009
# @@protoc_insertion_point(module_scope)
