# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from neural_cam_ros/obstacleStack.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import neural_cam_ros.msg
import geometry_msgs.msg

class obstacleStack(genpy.Message):
  _md5sum = "78f69d2c2bc1534a704126e4efe4e06e"
  _type = "neural_cam_ros/obstacleStack"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string stack_name
uint32 stack_len
obstacle[] stack_obstacles

================================================================================
MSG: neural_cam_ros/obstacle
#info: topleft_, bottomright_ refering to image
#info: planar_ is plane position information

string name
geometry_msgs/Point topleft
geometry_msgs/Point bottomright

#string name
#float32 depth

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['stack_name','stack_len','stack_obstacles']
  _slot_types = ['string','uint32','neural_cam_ros/obstacle[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       stack_name,stack_len,stack_obstacles

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(obstacleStack, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.stack_name is None:
        self.stack_name = ''
      if self.stack_len is None:
        self.stack_len = 0
      if self.stack_obstacles is None:
        self.stack_obstacles = []
    else:
      self.stack_name = ''
      self.stack_len = 0
      self.stack_obstacles = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.stack_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_I.pack(self.stack_len))
      length = len(self.stack_obstacles)
      buff.write(_struct_I.pack(length))
      for val1 in self.stack_obstacles:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v1 = val1.topleft
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v2 = val1.bottomright
        _x = _v2
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.stack_obstacles is None:
        self.stack_obstacles = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.stack_name = str[start:end].decode('utf-8')
      else:
        self.stack_name = str[start:end]
      start = end
      end += 4
      (self.stack_len,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.stack_obstacles = []
      for i in range(0, length):
        val1 = neural_cam_ros.msg.obstacle()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _v3 = val1.topleft
        _x = _v3
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v4 = val1.bottomright
        _x = _v4
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.stack_obstacles.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.stack_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_I.pack(self.stack_len))
      length = len(self.stack_obstacles)
      buff.write(_struct_I.pack(length))
      for val1 in self.stack_obstacles:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _v5 = val1.topleft
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = val1.bottomright
        _x = _v6
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.stack_obstacles is None:
        self.stack_obstacles = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.stack_name = str[start:end].decode('utf-8')
      else:
        self.stack_name = str[start:end]
      start = end
      end += 4
      (self.stack_len,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.stack_obstacles = []
      for i in range(0, length):
        val1 = neural_cam_ros.msg.obstacle()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _v7 = val1.topleft
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v8 = val1.bottomright
        _x = _v8
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.stack_obstacles.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3d = struct.Struct("<3d")
