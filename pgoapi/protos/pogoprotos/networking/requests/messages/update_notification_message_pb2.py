# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/update_notification_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import notification_state_pb2 as pogoprotos_dot_enums_dot_notification__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/update_notification_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/requests/messages/update_notification_message.proto\x12\'pogoprotos.networking.requests.messages\x1a)pogoprotos/enums/notification_state.proto\"\x86\x01\n\x19UpdateNotificationMessage\x12\x18\n\x10notification_ids\x18\x01 \x03(\t\x12\x1b\n\x13\x63reate_timestamp_ms\x18\x02 \x03(\x03\x12\x32\n\x05state\x18\x03 \x01(\x0e\x32#.pogoprotos.enums.NotificationStateb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_notification__state__pb2.DESCRIPTOR,])




_UPDATENOTIFICATIONMESSAGE = _descriptor.Descriptor(
  name='UpdateNotificationMessage',
  full_name='pogoprotos.networking.requests.messages.UpdateNotificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_ids', full_name='pogoprotos.networking.requests.messages.UpdateNotificationMessage.notification_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_timestamp_ms', full_name='pogoprotos.networking.requests.messages.UpdateNotificationMessage.create_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='pogoprotos.networking.requests.messages.UpdateNotificationMessage.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=296,
)

_UPDATENOTIFICATIONMESSAGE.fields_by_name['state'].enum_type = pogoprotos_dot_enums_dot_notification__state__pb2._NOTIFICATIONSTATE
DESCRIPTOR.message_types_by_name['UpdateNotificationMessage'] = _UPDATENOTIFICATIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateNotificationMessage = _reflection.GeneratedProtocolMessageType('UpdateNotificationMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATENOTIFICATIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.update_notification_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UpdateNotificationMessage)
  ))
_sym_db.RegisterMessage(UpdateNotificationMessage)


# @@protoc_insertion_point(module_scope)
