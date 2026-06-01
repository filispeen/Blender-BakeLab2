import bpy
from . import bakelab_map

from bpy.types import (
            Operator,
            PropertyGroup, 
            Panel
        )
from bpy.props import (
            IntProperty,
            EnumProperty,
            BoolProperty,
            FloatProperty,
            StringProperty,
            PointerProperty,
            CollectionProperty
        )
class BakeObjData(PropertyGroup):
    obj : PointerProperty(
        type=bpy.types.Object
    )
class BakeMapData(PropertyGroup):
    map_type : StringProperty()
    pass_name : StringProperty()
    normal_space : StringProperty()

    image : PointerProperty(
        type=bpy.types.Image
    )

class BakeLab_BakedData(PropertyGroup):
    obj_list : CollectionProperty(
        type=BakeObjData
    )
    map_list : CollectionProperty(
        type=BakeMapData
    )
    
    def AddObj(self, obj):
        item = self.obj_list.add()
        item.obj = obj

    def AddMap(self, bake_map, image):
        item = self.map_list.add()
        
        item.map_type = bake_map.type
        item.pass_name = bake_map.pass_name
        item.normal_space = bake_map.normal_space
        item.image = image
