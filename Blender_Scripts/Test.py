import bpy

# ------------------------------------------------------------------------
#  Clear scene
# ------------------------------------------------------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ------------------------------------------------------------------------
#  Create a red pyramid (triangular base)
# ------------------------------------------------------------------------
mesh = bpy.data.meshes.new("Red_Pyramid")
verts = [
    (0, 0, 0),     # base corner 1
    (2, 0, 0),     # base corner 2
    (1, 1.732, 0), # base corner 3 (equilateral base)
    (1, 0.577, 1.5)  # apex
]
faces = [(0, 1, 2), (0, 1, 3), (1, 2, 3), (2, 0, 3)]
mesh.from_pydata(verts, [], faces)
pyramid = bpy.data.objects.new("Red_Pyramid", mesh)
bpy.context.collection.objects.link(pyramid)

mat_red = bpy.data.materials.new(name="Red_Mat")
mat_red.diffuse_color = (1, 0, 0, 1)
pyramid.data.materials.append(mat_red)
pyramid.location = (-2, 0, 0)

# ------------------------------------------------------------------------
#  Create green sphere
# ------------------------------------------------------------------------
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.8, location=(0, 0, 0.8))
sphere = bpy.context.active_object
sphere.name = "Green_Sphere"
mat_green = bpy.data.materials.new(name="Green_Mat")
mat_green.diffuse_color = (0, 1, 0, 1)
sphere.data.materials.append(mat_green)

# ------------------------------------------------------------------------
#  Create blue cube
# ------------------------------------------------------------------------
bpy.ops.mesh.primitive_cube_add(size=1.5, location=(2.2, 0, 0.75))
cube = bpy.context.active_object
cube.name = "Blue_Cube"
mat_blue = bpy.data.materials.new(name="Blue_Mat")
mat_blue.diffuse_color = (0, 0, 1, 1)
cube.data.materials.append(mat_blue)

# ------------------------------------------------------------------------
#  Add camera (centered and elevated for perfect view)
# ------------------------------------------------------------------------
bpy.ops.object.camera_add(location=(0, -6, 3.5), rotation=(1.25, 0, 0))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# ------------------------------------------------------------------------
#  Add light
# ------------------------------------------------------------------------
bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
light = bpy.context.active_object
light.data.energy = 5
