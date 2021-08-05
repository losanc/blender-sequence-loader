import bpy
from .callback import *
class importer_properties(bpy.types.PropertyGroup):
    path: bpy.props.StringProperty(
        name="Directory",
        default="C:\\Users\\hui\\Desktop\\output\\DamBreakModel\\vtk\\",
        subtype="DIR_PATH",
        description="You need to go to the folder with the sequence, then click \"Accept\". ",
    )
    fileseq: bpy.props.EnumProperty(
        name="File Sequences",
        description="Please choose the file sequences you want",
        items=callback_fileseq,
        update=update_fileseq,
    )
    pattern: bpy.props.StringProperty(
        name="Pattern", description="You can specify the pattern here, in case the sequence can't be deteced.")
    type: bpy.props.EnumProperty(
        name="Type",
        description="choose particles or mesh",
        items=[("mesh", "Add Mesh", ""), ("particle", "Add Particles", "")],
    )


# Structure:
# tool_properties:
#    1. importer (importer_properties object) 
#    2. imported:
#       2.1 imported_seq_properties
#           2.1.1 color_attribute
class color_attribtue(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name='color attr')


class imported_seq_properties(bpy.types.PropertyGroup):
    pattern: bpy.props.StringProperty(
        name='pattern', description="pattern, using absolute path", default='test')
    type: bpy.props.IntProperty(
        name='type', description='type of this sequence, particle or mesh, or other', default=0, min=0, max=1)
    used_color_attribute: bpy.props.PointerProperty(type=color_attribtue)
    all_attributes: bpy.props.CollectionProperty(type=color_attribtue)
    all_attributes_enum: bpy.props.EnumProperty(
        name="Color Field",
        description="choose attributes used for coloring",
        items=callback_color_attribute,
        update=update_color_attribute,
    )
    start: bpy.props.IntProperty(
        name='start', description='start frame number')
    end: bpy.props.IntProperty(name='end', description='end frame number')
    length: bpy.props.IntProperty(
        name='length', description='total frame number')

    # meshes
    # particles
    radius: bpy.props.FloatProperty(name='radius', description='raidus of the particles',
                                    default=0.01, update=update_particle_radius, min=0, precision=6)
    max_value: bpy.props.FloatProperty(name='max value', description='max value to clamp the field',update=update_particle_max_value)
    min_value: bpy.props.FloatProperty(name='min value', description='min value to clamp the field',default=0,update=update_particle_min_value)
    mesh_name: bpy.props.StringProperty()
    obj_name: bpy.props.StringProperty()
    sphere_obj_name: bpy.props.StringProperty()
    material_name: bpy.props.StringProperty()
    tex_image_name: bpy.props.StringProperty()

class tool_properties(bpy.types.PropertyGroup):
    importer: bpy.props.PointerProperty(type=importer_properties)
    imported: bpy.props.CollectionProperty(type=imported_seq_properties)
    imported_num: bpy.props.IntProperty(
        name='imported count', description='the number of imported sequence, when selecting from ui list', default=0)