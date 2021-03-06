# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_map_objects_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map import map_cell_pb2 as pogoprotos_dot_map_dot_map__cell__pb2
from pogoprotos.map import map_objects_status_pb2 as pogoprotos_dot_map_dot_map__objects__status__pb2
from pogoprotos.map.weather import client_weather_pb2 as pogoprotos_dot_map_dot_weather_dot_client__weather__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_map_objects_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n>pogoprotos/networking/responses/get_map_objects_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x1dpogoprotos/map/map_cell.proto\x1a\'pogoprotos/map/map_objects_status.proto\x1a+pogoprotos/map/weather/client_weather.proto\"\xb6\x02\n\x15GetMapObjectsResponse\x12*\n\tmap_cells\x18\x01 \x03(\x0b\x32\x17.pogoprotos.map.MapCell\x12\x30\n\x06status\x18\x02 \x01(\x0e\x32 .pogoprotos.map.MapObjectsStatus\x12U\n\x0btime_of_day\x18\x03 \x01(\x0e\x32@.pogoprotos.networking.responses.GetMapObjectsResponse.TimeOfDay\x12=\n\x0e\x63lient_weather\x18\x04 \x03(\x0b\x32%.pogoprotos.map.weather.ClientWeather\")\n\tTimeOfDay\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03\x44\x41Y\x10\x01\x12\t\n\x05NIGHT\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_map__cell__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_map__objects__status__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_weather_dot_client__weather__pb2.DESCRIPTOR,])



_GETMAPOBJECTSRESPONSE_TIMEOFDAY = _descriptor.EnumDescriptor(
  name='TimeOfDay',
  full_name='pogoprotos.networking.responses.GetMapObjectsResponse.TimeOfDay',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NIGHT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=486,
  serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_GETMAPOBJECTSRESPONSE_TIMEOFDAY)


_GETMAPOBJECTSRESPONSE = _descriptor.Descriptor(
  name='GetMapObjectsResponse',
  full_name='pogoprotos.networking.responses.GetMapObjectsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_cells', full_name='pogoprotos.networking.responses.GetMapObjectsResponse.map_cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetMapObjectsResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_of_day', full_name='pogoprotos.networking.responses.GetMapObjectsResponse.time_of_day', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_weather', full_name='pogoprotos.networking.responses.GetMapObjectsResponse.client_weather', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETMAPOBJECTSRESPONSE_TIMEOFDAY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=527,
)

_GETMAPOBJECTSRESPONSE.fields_by_name['map_cells'].message_type = pogoprotos_dot_map_dot_map__cell__pb2._MAPCELL
_GETMAPOBJECTSRESPONSE.fields_by_name['status'].enum_type = pogoprotos_dot_map_dot_map__objects__status__pb2._MAPOBJECTSSTATUS
_GETMAPOBJECTSRESPONSE.fields_by_name['time_of_day'].enum_type = _GETMAPOBJECTSRESPONSE_TIMEOFDAY
_GETMAPOBJECTSRESPONSE.fields_by_name['client_weather'].message_type = pogoprotos_dot_map_dot_weather_dot_client__weather__pb2._CLIENTWEATHER
_GETMAPOBJECTSRESPONSE_TIMEOFDAY.containing_type = _GETMAPOBJECTSRESPONSE
DESCRIPTOR.message_types_by_name['GetMapObjectsResponse'] = _GETMAPOBJECTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMapObjectsResponse = _reflection.GeneratedProtocolMessageType('GetMapObjectsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETMAPOBJECTSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_map_objects_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetMapObjectsResponse)
  ))
_sym_db.RegisterMessage(GetMapObjectsResponse)


# @@protoc_insertion_point(module_scope)
