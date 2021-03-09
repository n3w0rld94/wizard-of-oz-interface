# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animus_structs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='animus_structs.proto',
  package='animus.structs',
  syntax='proto3',
  serialized_options=b'\n\036com.cyberselves.animus.strcutsB\022AnimusStructsProtoH\001Z\"github.com/dcam0050/AnimusMessages\242\002\rAnimusStructs\252\002\016Animus.Structs',
  serialized_pb=b'\n\x14\x61nimus_structs.proto\x12\x0e\x61nimus.structs\"\x81\x01\n\x08Location\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\x0b\n\x03loc\x18\x06 \x01(\t\x12\x0e\n\x06postal\x18\x07 \x01(\t\x12\x0b\n\x03org\x18\x08 \x01(\t\"\xa0\x01\n\x0b\x41udioParams\x12\x10\n\x08\x42\x61\x63kends\x18\x01 \x03(\t\x12\x12\n\nSampleRate\x18\x02 \x01(\r\x12\x10\n\x08\x43hannels\x18\x03 \x01(\r\x12\x14\n\x0cSizeInFrames\x18\x04 \x01(\x08\x12\x14\n\x0cTransmitRate\x18\x05 \x01(\r\x12\x17\n\x0f\x63\x61ptureModality\x18\x06 \x01(\t\x12\x14\n\x0csinkModality\x18\x07 \x01(\t\"U\n\tGeoStruct\x12\x10\n\x08UpperLat\x18\x01 \x01(\x01\x12\x10\n\x08LowerLat\x18\x02 \x01(\x01\x12\x11\n\tUpperLong\x18\x03 \x01(\x01\x12\x11\n\tLowerLong\x18\x04 \x01(\x01\"P\n\x0c\x41ssetLicense\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12.\n\rasset_license\x18\x02 \x01(\x0b\x32\x17.animus.structs.License\"\xb5\x01\n\x0cRobotLicense\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\t\x12.\n\rrobot_license\x18\x03 \x01(\x0b\x32\x17.animus.structs.License\x12\x12\n\nrobot_make\x18\x04 \x01(\t\x12\x13\n\x0brobot_model\x18\x05 \x01(\t\x12\x11\n\tpair_code\x18\x06 \x01(\t\x12\x15\n\rpaired_status\x18\x07 \x01(\x08\"U\n\x07License\x12\x12\n\nlicense_id\x18\x01 \x01(\t\x12\x12\n\nstart_date\x18\x03 \x01(\x03\x12\x10\n\x08\x64uration\x18\x04 \x01(\x03\x12\x10\n\x08\x65nd_date\x18\x05 \x01(\x03\"2\n\x05Share\x12\x17\n\x0frecipient_email\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x03\"\x1d\n\nICEDetails\x12\x0f\n\x07\x64\x65tails\x18\x01 \x01(\t\"\xaf\x01\n\x05\x41sset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x0f\n\x07license\x18\x06 \x01(\t\x12\x0c\n\x04make\x18\x07 \x01(\t\x12\r\n\x05model\x18\x08 \x01(\t\x12+\n\tartifacts\x18\t \x03(\x0b\x32\x18.animus.structs.Artifact\"\xbd\x01\n\x08\x41rtifact\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\t\x12\n\n\x02OS\x18\x03 \x01(\t\x12\x0c\n\x04\x41rch\x18\x04 \x01(\t\x12\x14\n\x0cVersionMajor\x18\x05 \x01(\r\x12\x14\n\x0cVersionMinor\x18\x06 \x01(\r\x12\x14\n\x0cVersionPatch\x18\x07 \x01(\r\x12\x10\n\x08language\x18\x08 \x01(\t\x12\x11\n\ttimestamp\x18\t \x01(\x03\x12\x10\n\x08\x63hecksum\x18\n \x01(\x0c\x42{\n\x1e\x63om.cyberselves.animus.strcutsB\x12\x41nimusStructsProtoH\x01Z\"github.com/dcam0050/AnimusMessages\xa2\x02\rAnimusStructs\xaa\x02\x0e\x41nimus.Structsb\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='animus.structs.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='animus.structs.Location.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='animus.structs.Location.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='animus.structs.Location.city', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region', full_name='animus.structs.Location.region', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='animus.structs.Location.country', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loc', full_name='animus.structs.Location.loc', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postal', full_name='animus.structs.Location.postal', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='animus.structs.Location.org', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=170,
)


_AUDIOPARAMS = _descriptor.Descriptor(
  name='AudioParams',
  full_name='animus.structs.AudioParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Backends', full_name='animus.structs.AudioParams.Backends', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SampleRate', full_name='animus.structs.AudioParams.SampleRate', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Channels', full_name='animus.structs.AudioParams.Channels', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SizeInFrames', full_name='animus.structs.AudioParams.SizeInFrames', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TransmitRate', full_name='animus.structs.AudioParams.TransmitRate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='captureModality', full_name='animus.structs.AudioParams.captureModality', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sinkModality', full_name='animus.structs.AudioParams.sinkModality', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=333,
)


_GEOSTRUCT = _descriptor.Descriptor(
  name='GeoStruct',
  full_name='animus.structs.GeoStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UpperLat', full_name='animus.structs.GeoStruct.UpperLat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LowerLat', full_name='animus.structs.GeoStruct.LowerLat', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UpperLong', full_name='animus.structs.GeoStruct.UpperLong', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LowerLong', full_name='animus.structs.GeoStruct.LowerLong', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=420,
)


_ASSETLICENSE = _descriptor.Descriptor(
  name='AssetLicense',
  full_name='animus.structs.AssetLicense',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='animus.structs.AssetLicense.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_license', full_name='animus.structs.AssetLicense.asset_license', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=502,
)


_ROBOTLICENSE = _descriptor.Descriptor(
  name='RobotLicense',
  full_name='animus.structs.RobotLicense',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='animus.structs.RobotLicense.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='animus.structs.RobotLicense.asset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot_license', full_name='animus.structs.RobotLicense.robot_license', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot_make', full_name='animus.structs.RobotLicense.robot_make', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot_model', full_name='animus.structs.RobotLicense.robot_model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pair_code', full_name='animus.structs.RobotLicense.pair_code', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paired_status', full_name='animus.structs.RobotLicense.paired_status', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=686,
)


_LICENSE = _descriptor.Descriptor(
  name='License',
  full_name='animus.structs.License',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='license_id', full_name='animus.structs.License.license_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='animus.structs.License.start_date', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='animus.structs.License.duration', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='animus.structs.License.end_date', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=688,
  serialized_end=773,
)


_SHARE = _descriptor.Descriptor(
  name='Share',
  full_name='animus.structs.Share',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipient_email', full_name='animus.structs.Share.recipient_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='animus.structs.Share.duration', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=825,
)


_ICEDETAILS = _descriptor.Descriptor(
  name='ICEDetails',
  full_name='animus.structs.ICEDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='animus.structs.ICEDetails.details', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=856,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='animus.structs.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='animus.structs.Asset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='animus.structs.Asset.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='animus.structs.Asset.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='animus.structs.Asset.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='animus.structs.Asset.author', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='license', full_name='animus.structs.Asset.license', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='make', full_name='animus.structs.Asset.make', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='animus.structs.Asset.model', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifacts', full_name='animus.structs.Asset.artifacts', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=1034,
)


_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='animus.structs.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='animus.structs.Artifact.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='animus.structs.Artifact.asset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='OS', full_name='animus.structs.Artifact.OS', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Arch', full_name='animus.structs.Artifact.Arch', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VersionMajor', full_name='animus.structs.Artifact.VersionMajor', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VersionMinor', full_name='animus.structs.Artifact.VersionMinor', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VersionPatch', full_name='animus.structs.Artifact.VersionPatch', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='animus.structs.Artifact.language', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='animus.structs.Artifact.timestamp', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='animus.structs.Artifact.checksum', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1037,
  serialized_end=1226,
)

_ASSETLICENSE.fields_by_name['asset_license'].message_type = _LICENSE
_ROBOTLICENSE.fields_by_name['robot_license'].message_type = _LICENSE
_ASSET.fields_by_name['artifacts'].message_type = _ARTIFACT
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['AudioParams'] = _AUDIOPARAMS
DESCRIPTOR.message_types_by_name['GeoStruct'] = _GEOSTRUCT
DESCRIPTOR.message_types_by_name['AssetLicense'] = _ASSETLICENSE
DESCRIPTOR.message_types_by_name['RobotLicense'] = _ROBOTLICENSE
DESCRIPTOR.message_types_by_name['License'] = _LICENSE
DESCRIPTOR.message_types_by_name['Share'] = _SHARE
DESCRIPTOR.message_types_by_name['ICEDetails'] = _ICEDETAILS
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.Location)
  })
_sym_db.RegisterMessage(Location)

AudioParams = _reflection.GeneratedProtocolMessageType('AudioParams', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOPARAMS,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.AudioParams)
  })
_sym_db.RegisterMessage(AudioParams)

GeoStruct = _reflection.GeneratedProtocolMessageType('GeoStruct', (_message.Message,), {
  'DESCRIPTOR' : _GEOSTRUCT,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.GeoStruct)
  })
_sym_db.RegisterMessage(GeoStruct)

AssetLicense = _reflection.GeneratedProtocolMessageType('AssetLicense', (_message.Message,), {
  'DESCRIPTOR' : _ASSETLICENSE,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.AssetLicense)
  })
_sym_db.RegisterMessage(AssetLicense)

RobotLicense = _reflection.GeneratedProtocolMessageType('RobotLicense', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTLICENSE,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.RobotLicense)
  })
_sym_db.RegisterMessage(RobotLicense)

License = _reflection.GeneratedProtocolMessageType('License', (_message.Message,), {
  'DESCRIPTOR' : _LICENSE,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.License)
  })
_sym_db.RegisterMessage(License)

Share = _reflection.GeneratedProtocolMessageType('Share', (_message.Message,), {
  'DESCRIPTOR' : _SHARE,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.Share)
  })
_sym_db.RegisterMessage(Share)

ICEDetails = _reflection.GeneratedProtocolMessageType('ICEDetails', (_message.Message,), {
  'DESCRIPTOR' : _ICEDETAILS,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.ICEDetails)
  })
_sym_db.RegisterMessage(ICEDetails)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.Asset)
  })
_sym_db.RegisterMessage(Asset)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'animus_structs_pb2'
  # @@protoc_insertion_point(class_scope:animus.structs.Artifact)
  })
_sym_db.RegisterMessage(Artifact)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
