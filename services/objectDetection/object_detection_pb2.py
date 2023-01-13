# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection.proto',
  package='objectDetection',
  syntax='proto3',
  serialized_options=_b('\n\"com.intel.examples.objectDetectionB\024objectDetectionProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x16object_detection.proto\x12\x0fobjectDetection\",\n\x0cRequestBytes\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0e\n\x06length\x18\x02 \x01(\x05\"C\n\x0fPredictionsList\x12\x30\n\x0bpredictions\x18\x01 \x03(\x0b\x32\x1b.objectDetection.Prediction\"\x8a\x01\n\nPrediction\x12\x0e\n\x06index0\x18\x01 \x01(\x02\x12\x0e\n\x06index1\x18\x02 \x01(\x02\x12\x0e\n\x06index2\x18\x03 \x01(\x02\x12\x0e\n\x06index3\x18\x04 \x01(\x02\x12\x12\n\nconfidence\x18\x05 \x01(\x02\x12\x12\n\nclassIndex\x18\x06 \x01(\x05\x12\x14\n\x0cpredictIndex\x18\x07 \x01(\x05\x32`\n\tDetection\x12S\n\x0egetPredictions\x12\x1d.objectDetection.RequestBytes\x1a .objectDetection.PredictionsList\"\x00\x42\x42\n\"com.intel.examples.objectDetectionB\x14objectDetectionProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_REQUESTBYTES = _descriptor.Descriptor(
  name='RequestBytes',
  full_name='objectDetection.RequestBytes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='objectDetection.RequestBytes.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='objectDetection.RequestBytes.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=43,
  serialized_end=87,
)


_PREDICTIONSLIST = _descriptor.Descriptor(
  name='PredictionsList',
  full_name='objectDetection.PredictionsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predictions', full_name='objectDetection.PredictionsList.predictions', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=89,
  serialized_end=156,
)


_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='objectDetection.Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index0', full_name='objectDetection.Prediction.index0', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index1', full_name='objectDetection.Prediction.index1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index2', full_name='objectDetection.Prediction.index2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index3', full_name='objectDetection.Prediction.index3', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='objectDetection.Prediction.confidence', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classIndex', full_name='objectDetection.Prediction.classIndex', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predictIndex', full_name='objectDetection.Prediction.predictIndex', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=159,
  serialized_end=297,
)

_PREDICTIONSLIST.fields_by_name['predictions'].message_type = _PREDICTION
DESCRIPTOR.message_types_by_name['RequestBytes'] = _REQUESTBYTES
DESCRIPTOR.message_types_by_name['PredictionsList'] = _PREDICTIONSLIST
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestBytes = _reflection.GeneratedProtocolMessageType('RequestBytes', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTBYTES,
  '__module__' : 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:objectDetection.RequestBytes)
  })
_sym_db.RegisterMessage(RequestBytes)

PredictionsList = _reflection.GeneratedProtocolMessageType('PredictionsList', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONSLIST,
  '__module__' : 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:objectDetection.PredictionsList)
  })
_sym_db.RegisterMessage(PredictionsList)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:objectDetection.Prediction)
  })
_sym_db.RegisterMessage(Prediction)


DESCRIPTOR._options = None

_DETECTION = _descriptor.ServiceDescriptor(
  name='Detection',
  full_name='objectDetection.Detection',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=299,
  serialized_end=395,
  methods=[
  _descriptor.MethodDescriptor(
    name='getPredictions',
    full_name='objectDetection.Detection.getPredictions',
    index=0,
    containing_service=None,
    input_type=_REQUESTBYTES,
    output_type=_PREDICTIONSLIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECTION)

DESCRIPTOR.services_by_name['Detection'] = _DETECTION

# @@protoc_insertion_point(module_scope)