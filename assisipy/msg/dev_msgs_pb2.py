# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dev_msgs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import base_msgs_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dev_msgs.proto',
  package='AssisiMsg',
  serialized_pb='\n\x0e\x64\x65v_msgs.proto\x12\tAssisiMsg\x1a\x0f\x62\x61se_msgs.proto\"\xe8\x01\n\nRangeArray\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x32\n\x04type\x18\x02 \x01(\x0e\x32 .AssisiMsg.RangeArray.SensorType:\x02IR\x12\x1d\n\rfield_of_view\x18\x03 \x01(\x02:\x06\x30.5236\x12\x14\n\tmin_range\x18\x04 \x01(\x02:\x01\x30\x12\x16\n\tmax_range\x18\x05 \x01(\x02:\x03inf\x12\r\n\x05range\x18\x06 \x03(\x02\x12\x11\n\traw_value\x18\x07 \x03(\x02\"\x14\n\nSensorType\x12\x06\n\x02IR\x10\x00\">\n\x0bTemperature\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x0c\n\x04temp\x18\x02 \x02(\x02\"C\n\x10TemperatureArray\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x0c\n\x04temp\x18\x02 \x03(\x02\"d\n\x17TemperatureWithGradient\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x0c\n\x04temp\x18\x02 \x02(\x02\x12\x0b\n\x03\x64tx\x18\x03 \x02(\x02\x12\x0b\n\x03\x64ty\x18\x04 \x02(\x02\"W\n\x11VibrationSetpoint\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x0c\n\x04\x66req\x18\x02 \x02(\x01\x12\x11\n\tamplitude\x18\x03 \x01(\x01\"o\n\x10VibrationReading\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x0c\n\x04\x66req\x18\x02 \x03(\x02\x12\x11\n\tamplitude\x18\x03 \x03(\x02\x12\x17\n\x0f\x61mplitude_stdev\x18\x04 \x03(\x02\"h\n\x15VibrationReadingArray\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12,\n\x07reading\x18\x02 \x03(\x0b\x32\x1b.AssisiMsg.VibrationReading\"S\n\tDiffDrive\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x10\n\x08vel_left\x18\x02 \x02(\x01\x12\x11\n\tvel_right\x18\x03 \x02(\x01\"\x9a\x01\n\x0bObjectArray\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x1d\n\rfield_of_view\x18\x03 \x01(\x02:\x06\x30.5236\x12\x14\n\tmin_range\x18\x04 \x01(\x02:\x01\x30\x12\x16\n\tmax_range\x18\x05 \x01(\x02:\x03inf\x12\r\n\x05range\x18\x06 \x03(\x02\x12\x0c\n\x04type\x18\x07 \x03(\t\"?\n\x07\x41irflow\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x11\n\tintensity\x18\x02 \x02(\x02\"Y\n\x0e\x41irflowReading\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.AssisiMsg.Header\x12\x11\n\tintensity\x18\x02 \x02(\x02\x12\x11\n\tdirection\x18\x03 \x02(\x02')



_RANGEARRAY_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='AssisiMsg.RangeArray.SensorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IR', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=259,
  serialized_end=279,
)


_RANGEARRAY = _descriptor.Descriptor(
  name='RangeArray',
  full_name='AssisiMsg.RangeArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.RangeArray.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='AssisiMsg.RangeArray.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_of_view', full_name='AssisiMsg.RangeArray.field_of_view', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.5236,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_range', full_name='AssisiMsg.RangeArray.min_range', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_range', full_name='AssisiMsg.RangeArray.max_range', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e10000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='AssisiMsg.RangeArray.range', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='AssisiMsg.RangeArray.raw_value', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RANGEARRAY_SENSORTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=47,
  serialized_end=279,
)


_TEMPERATURE = _descriptor.Descriptor(
  name='Temperature',
  full_name='AssisiMsg.Temperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.Temperature.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temp', full_name='AssisiMsg.Temperature.temp', index=1,
      number=2, type=2, cpp_type=6, label=2,
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
  extension_ranges=[],
  serialized_start=281,
  serialized_end=343,
)


_TEMPERATUREARRAY = _descriptor.Descriptor(
  name='TemperatureArray',
  full_name='AssisiMsg.TemperatureArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.TemperatureArray.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temp', full_name='AssisiMsg.TemperatureArray.temp', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=345,
  serialized_end=412,
)


_TEMPERATUREWITHGRADIENT = _descriptor.Descriptor(
  name='TemperatureWithGradient',
  full_name='AssisiMsg.TemperatureWithGradient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.TemperatureWithGradient.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temp', full_name='AssisiMsg.TemperatureWithGradient.temp', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dtx', full_name='AssisiMsg.TemperatureWithGradient.dtx', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dty', full_name='AssisiMsg.TemperatureWithGradient.dty', index=3,
      number=4, type=2, cpp_type=6, label=2,
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
  extension_ranges=[],
  serialized_start=414,
  serialized_end=514,
)


_VIBRATIONSETPOINT = _descriptor.Descriptor(
  name='VibrationSetpoint',
  full_name='AssisiMsg.VibrationSetpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.VibrationSetpoint.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='freq', full_name='AssisiMsg.VibrationSetpoint.freq', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amplitude', full_name='AssisiMsg.VibrationSetpoint.amplitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  extension_ranges=[],
  serialized_start=516,
  serialized_end=603,
)


_VIBRATIONREADING = _descriptor.Descriptor(
  name='VibrationReading',
  full_name='AssisiMsg.VibrationReading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.VibrationReading.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='freq', full_name='AssisiMsg.VibrationReading.freq', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amplitude', full_name='AssisiMsg.VibrationReading.amplitude', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amplitude_stdev', full_name='AssisiMsg.VibrationReading.amplitude_stdev', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=605,
  serialized_end=716,
)


_VIBRATIONREADINGARRAY = _descriptor.Descriptor(
  name='VibrationReadingArray',
  full_name='AssisiMsg.VibrationReadingArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.VibrationReadingArray.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reading', full_name='AssisiMsg.VibrationReadingArray.reading', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=718,
  serialized_end=822,
)


_DIFFDRIVE = _descriptor.Descriptor(
  name='DiffDrive',
  full_name='AssisiMsg.DiffDrive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.DiffDrive.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vel_left', full_name='AssisiMsg.DiffDrive.vel_left', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vel_right', full_name='AssisiMsg.DiffDrive.vel_right', index=2,
      number=3, type=1, cpp_type=5, label=2,
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
  extension_ranges=[],
  serialized_start=824,
  serialized_end=907,
)


_OBJECTARRAY = _descriptor.Descriptor(
  name='ObjectArray',
  full_name='AssisiMsg.ObjectArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.ObjectArray.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_of_view', full_name='AssisiMsg.ObjectArray.field_of_view', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.5236,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_range', full_name='AssisiMsg.ObjectArray.min_range', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_range', full_name='AssisiMsg.ObjectArray.max_range', index=3,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e10000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='AssisiMsg.ObjectArray.range', index=4,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='AssisiMsg.ObjectArray.type', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=910,
  serialized_end=1064,
)


_AIRFLOW = _descriptor.Descriptor(
  name='Airflow',
  full_name='AssisiMsg.Airflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.Airflow.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intensity', full_name='AssisiMsg.Airflow.intensity', index=1,
      number=2, type=2, cpp_type=6, label=2,
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
  extension_ranges=[],
  serialized_start=1066,
  serialized_end=1129,
)


_AIRFLOWREADING = _descriptor.Descriptor(
  name='AirflowReading',
  full_name='AssisiMsg.AirflowReading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='AssisiMsg.AirflowReading.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intensity', full_name='AssisiMsg.AirflowReading.intensity', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='AssisiMsg.AirflowReading.direction', index=2,
      number=3, type=2, cpp_type=6, label=2,
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
  extension_ranges=[],
  serialized_start=1131,
  serialized_end=1220,
)

_RANGEARRAY.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_RANGEARRAY.fields_by_name['type'].enum_type = _RANGEARRAY_SENSORTYPE
_RANGEARRAY_SENSORTYPE.containing_type = _RANGEARRAY;
_TEMPERATURE.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_TEMPERATUREARRAY.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_TEMPERATUREWITHGRADIENT.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_VIBRATIONSETPOINT.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_VIBRATIONREADING.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_VIBRATIONREADINGARRAY.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_VIBRATIONREADINGARRAY.fields_by_name['reading'].message_type = _VIBRATIONREADING
_DIFFDRIVE.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_OBJECTARRAY.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_AIRFLOW.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
_AIRFLOWREADING.fields_by_name['header'].message_type = base_msgs_pb2._HEADER
DESCRIPTOR.message_types_by_name['RangeArray'] = _RANGEARRAY
DESCRIPTOR.message_types_by_name['Temperature'] = _TEMPERATURE
DESCRIPTOR.message_types_by_name['TemperatureArray'] = _TEMPERATUREARRAY
DESCRIPTOR.message_types_by_name['TemperatureWithGradient'] = _TEMPERATUREWITHGRADIENT
DESCRIPTOR.message_types_by_name['VibrationSetpoint'] = _VIBRATIONSETPOINT
DESCRIPTOR.message_types_by_name['VibrationReading'] = _VIBRATIONREADING
DESCRIPTOR.message_types_by_name['VibrationReadingArray'] = _VIBRATIONREADINGARRAY
DESCRIPTOR.message_types_by_name['DiffDrive'] = _DIFFDRIVE
DESCRIPTOR.message_types_by_name['ObjectArray'] = _OBJECTARRAY
DESCRIPTOR.message_types_by_name['Airflow'] = _AIRFLOW
DESCRIPTOR.message_types_by_name['AirflowReading'] = _AIRFLOWREADING

class RangeArray(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANGEARRAY

  # @@protoc_insertion_point(class_scope:AssisiMsg.RangeArray)

class Temperature(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEMPERATURE

  # @@protoc_insertion_point(class_scope:AssisiMsg.Temperature)

class TemperatureArray(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEMPERATUREARRAY

  # @@protoc_insertion_point(class_scope:AssisiMsg.TemperatureArray)

class TemperatureWithGradient(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEMPERATUREWITHGRADIENT

  # @@protoc_insertion_point(class_scope:AssisiMsg.TemperatureWithGradient)

class VibrationSetpoint(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VIBRATIONSETPOINT

  # @@protoc_insertion_point(class_scope:AssisiMsg.VibrationSetpoint)

class VibrationReading(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VIBRATIONREADING

  # @@protoc_insertion_point(class_scope:AssisiMsg.VibrationReading)

class VibrationReadingArray(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VIBRATIONREADINGARRAY

  # @@protoc_insertion_point(class_scope:AssisiMsg.VibrationReadingArray)

class DiffDrive(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIFFDRIVE

  # @@protoc_insertion_point(class_scope:AssisiMsg.DiffDrive)

class ObjectArray(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OBJECTARRAY

  # @@protoc_insertion_point(class_scope:AssisiMsg.ObjectArray)

class Airflow(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AIRFLOW

  # @@protoc_insertion_point(class_scope:AssisiMsg.Airflow)

class AirflowReading(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AIRFLOWREADING

  # @@protoc_insertion_point(class_scope:AssisiMsg.AirflowReading)


# @@protoc_insertion_point(module_scope)
