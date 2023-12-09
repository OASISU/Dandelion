bl_info = {
	"name" : "Geometry Nodes.001",
	"author" : "Node To Python",
	"version" : (1, 0, 0),
	"blender" : (3, 6, 2),
	"location" : "Object",
	"category" : "Node"
}

import bpy
import os

class GeometryNodes001(bpy.types.Operator):
	bl_idname = "object.geometry_nodes_001"
	bl_label = "Geometry Nodes.001"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		#initialize geometry_nodes_001 node group
		def geometry_nodes_001_node_group():
			geometry_nodes_001= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Geometry Nodes.001")

			#initialize geometry_nodes_001 nodes
			#node Frame
			frame = geometry_nodes_001.nodes.new("NodeFrame")

			#node Frame.002
			frame_002 = geometry_nodes_001.nodes.new("NodeFrame")

			#node Frame.003
			frame_003 = geometry_nodes_001.nodes.new("NodeFrame")

			#node Frame.001
			frame_001 = geometry_nodes_001.nodes.new("NodeFrame")

			#geometry_nodes_001 inputs
			#input Geometry
			geometry_nodes_001.inputs.new('NodeSocketGeometry', "Geometry")
			geometry_nodes_001.inputs[0].attribute_domain = 'POINT'


			#node Group Input
			group_input = geometry_nodes_001.nodes.new("NodeGroupInput")

			#node RGB Curves
			rgb_curves = geometry_nodes_001.nodes.new("ShaderNodeRGBCurve")
			#mapping settings
			rgb_curves.mapping.extend = 'EXTRAPOLATED'
			rgb_curves.mapping.tone = 'STANDARD'
			rgb_curves.mapping.black_level = (0.0, 0.0, 0.0)
			rgb_curves.mapping.white_level = (1.0, 1.0, 1.0)
			rgb_curves.mapping.clip_min_x = 0.0
			rgb_curves.mapping.clip_min_y = 0.0
			rgb_curves.mapping.clip_max_x = 1.0
			rgb_curves.mapping.clip_max_y = 1.0
			rgb_curves.mapping.use_clip = True
			#curve 0
			rgb_curves_curve_0 = rgb_curves.mapping.curves[0]
			rgb_curves_curve_0_point_0 = rgb_curves_curve_0.points[0]
			rgb_curves_curve_0_point_0.location = (0.0, 0.0)
			rgb_curves_curve_0_point_0.handle_type = 'AUTO'
			rgb_curves_curve_0_point_1 = rgb_curves_curve_0.points[1]
			rgb_curves_curve_0_point_1.location = (1.0, 1.0)
			rgb_curves_curve_0_point_1.handle_type = 'AUTO'
			#curve 1
			rgb_curves_curve_1 = rgb_curves.mapping.curves[1]
			rgb_curves_curve_1_point_0 = rgb_curves_curve_1.points[0]
			rgb_curves_curve_1_point_0.location = (0.0, 0.0)
			rgb_curves_curve_1_point_0.handle_type = 'AUTO'
			rgb_curves_curve_1_point_1 = rgb_curves_curve_1.points[1]
			rgb_curves_curve_1_point_1.location = (1.0, 1.0)
			rgb_curves_curve_1_point_1.handle_type = 'AUTO'
			#curve 2
			rgb_curves_curve_2 = rgb_curves.mapping.curves[2]
			rgb_curves_curve_2_point_0 = rgb_curves_curve_2.points[0]
			rgb_curves_curve_2_point_0.location = (0.0, 0.0)
			rgb_curves_curve_2_point_0.handle_type = 'AUTO'
			rgb_curves_curve_2_point_1 = rgb_curves_curve_2.points[1]
			rgb_curves_curve_2_point_1.location = (1.0, 1.0)
			rgb_curves_curve_2_point_1.handle_type = 'AUTO'
			#curve 3
			rgb_curves_curve_3 = rgb_curves.mapping.curves[3]
			rgb_curves_curve_3_point_0 = rgb_curves_curve_3.points[0]
			rgb_curves_curve_3_point_0.location = (0.0, 0.0)
			rgb_curves_curve_3_point_0.handle_type = 'AUTO'
			rgb_curves_curve_3_point_1 = rgb_curves_curve_3.points[1]
			rgb_curves_curve_3_point_1.location = (0.6363000273704529, 0.3125)
			rgb_curves_curve_3_point_1.handle_type = 'AUTO'
			rgb_curves_curve_3_point_2 = rgb_curves_curve_3.points.new(1.0, 1.0)
			rgb_curves_curve_3_point_2.handle_type = 'AUTO'
			#update curve after changes
			rgb_curves.mapping.update()
			#Fac
			rgb_curves.inputs[0].default_value = 1.0

			#node Spline Parameter
			spline_parameter = geometry_nodes_001.nodes.new("GeometryNodeSplineParameter")

			#node Math.003
			math_003 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_003.operation = 'MULTIPLY'
			#Value_001
			math_003.inputs[1].default_value = 0.20000000298023224
			#Value_002
			math_003.inputs[2].default_value = 0.5

			#node Combine XYZ.002
			combine_xyz_002 = geometry_nodes_001.nodes.new("ShaderNodeCombineXYZ")
			#Y
			combine_xyz_002.inputs[1].default_value = 0.0
			#Z
			combine_xyz_002.inputs[2].default_value = 0.0

			#node Separate XYZ
			separate_xyz = geometry_nodes_001.nodes.new("ShaderNodeSeparateXYZ")

			#node Math
			math = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math.operation = 'MULTIPLY'
			#Value_001
			math.inputs[1].default_value = -0.09999996423721313
			#Value_002
			math.inputs[2].default_value = 0.5

			#node Position
			position = geometry_nodes_001.nodes.new("GeometryNodeInputPosition")

			#node Combine XYZ.001
			combine_xyz_001 = geometry_nodes_001.nodes.new("ShaderNodeCombineXYZ")
			#Y
			combine_xyz_001.inputs[1].default_value = 0.0
			#Z
			combine_xyz_001.inputs[2].default_value = 0.0

			#node Curve Line
			curve_line = geometry_nodes_001.nodes.new("GeometryNodeCurvePrimitiveLine")
			curve_line.mode = 'POINTS'
			#Start
			curve_line.inputs[0].default_value = (0.0, 0.0, 0.0)
			#End
			curve_line.inputs[1].default_value = (0.0, 0.0, 5.0)
			#Direction
			curve_line.inputs[2].default_value = (0.0, 0.0, 1.0)
			#Length
			curve_line.inputs[3].default_value = 1.0

			#node Resample Curve
			resample_curve = geometry_nodes_001.nodes.new("GeometryNodeResampleCurve")
			resample_curve.mode = 'COUNT'
			#Selection
			resample_curve.inputs[1].default_value = True
			#Count
			resample_curve.inputs[2].default_value = 50
			#Length
			resample_curve.inputs[3].default_value = 0.10000000149011612

			#node Simulation Input
			simulation_input = geometry_nodes_001.nodes.new("GeometryNodeSimulationInput")
			#node Scene Time
			scene_time = geometry_nodes_001.nodes.new("GeometryNodeInputSceneTime")

			#node Compare.001
			compare_001 = geometry_nodes_001.nodes.new("FunctionNodeCompare")
			compare_001.data_type = 'FLOAT'
			compare_001.operation = 'LESS_THAN'
			compare_001.mode = 'ELEMENT'
			#B
			compare_001.inputs[1].default_value = 10.0
			#A_INT
			compare_001.inputs[2].default_value = 0
			#B_INT
			compare_001.inputs[3].default_value = 0
			#A_VEC3
			compare_001.inputs[4].default_value = (0.0, 0.0, 0.0)
			#B_VEC3
			compare_001.inputs[5].default_value = (0.0, 0.0, 0.0)
			#A_COL
			compare_001.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
			#B_COL
			compare_001.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
			#A_STR
			compare_001.inputs[8].default_value = ""
			#B_STR
			compare_001.inputs[9].default_value = ""
			#C
			compare_001.inputs[10].default_value = 0.8999999761581421
			#Angle
			compare_001.inputs[11].default_value = 0.08726649731397629
			#Epsilon
			compare_001.inputs[12].default_value = 0.0010000000474974513

			#node Compare
			compare = geometry_nodes_001.nodes.new("FunctionNodeCompare")
			compare.data_type = 'FLOAT'
			compare.operation = 'GREATER_THAN'
			compare.mode = 'ELEMENT'
			#B
			compare.inputs[1].default_value = 5.0
			#A_INT
			compare.inputs[2].default_value = 0
			#B_INT
			compare.inputs[3].default_value = 0
			#A_VEC3
			compare.inputs[4].default_value = (0.0, 0.0, 0.0)
			#B_VEC3
			compare.inputs[5].default_value = (0.0, 0.0, 0.0)
			#A_COL
			compare.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
			#B_COL
			compare.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
			#A_STR
			compare.inputs[8].default_value = ""
			#B_STR
			compare.inputs[9].default_value = ""
			#C
			compare.inputs[10].default_value = 0.8999999761581421
			#Angle
			compare.inputs[11].default_value = 0.08726649731397629
			#Epsilon
			compare.inputs[12].default_value = 0.0010000000474974513

			#node Math.002
			math_002 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_002.operation = 'MULTIPLY'
			#Value_002
			math_002.inputs[2].default_value = 0.5

			#node Named Attribute
			named_attribute = geometry_nodes_001.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "v"

			#node Vector Math
			vector_math = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math.operation = 'ADD'
			#Vector_002
			vector_math.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math.inputs[3].default_value = 1.0

			#node Store Named Attribute.001
			store_named_attribute_001 = geometry_nodes_001.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.data_type = 'FLOAT_VECTOR'
			store_named_attribute_001.domain = 'POINT'
			#Name
			store_named_attribute_001.inputs[2].default_value = "v"
			#Value_Float
			store_named_attribute_001.inputs[4].default_value = 0.0
			#Value_Color
			store_named_attribute_001.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			store_named_attribute_001.inputs[6].default_value = False
			#Value_Int
			store_named_attribute_001.inputs[7].default_value = 0

			#node Vector Math.001
			vector_math_001 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_001.operation = 'SCALE'
			#Vector_001
			vector_math_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Vector_002
			vector_math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_001.inputs[3].default_value = 0.800000011920929

			#node Store Named Attribute
			store_named_attribute = geometry_nodes_001.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.data_type = 'FLOAT_VECTOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "v"
			#Value_Float
			store_named_attribute.inputs[4].default_value = 0.0
			#Value_Color
			store_named_attribute.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			store_named_attribute.inputs[6].default_value = False
			#Value_Int
			store_named_attribute.inputs[7].default_value = 0

			#node Set Position.001
			set_position_001 = geometry_nodes_001.nodes.new("GeometryNodeSetPosition")
			#Selection
			set_position_001.inputs[1].default_value = True
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

			#node Simulation Output
			simulation_output = geometry_nodes_001.nodes.new("GeometryNodeSimulationOutput")
			#remove generated sim state items
			for item in simulation_output.state_items:
				simulation_output.state_items.remove(item)
			#create SSI "Geometry"
			simulation_output.state_items.new('GEOMETRY', "Geometry")
			simulation_output.state_items[0].attribute_domain = 'POINT'

			#geometry_nodes_001 outputs
			#output Geometry
			geometry_nodes_001.outputs.new('NodeSocketGeometry', "Geometry")
			geometry_nodes_001.outputs[0].attribute_domain = 'POINT'

			#output Instances
			geometry_nodes_001.outputs.new('NodeSocketGeometry', "Instances")
			geometry_nodes_001.outputs[1].attribute_domain = 'POINT'


			#node Group Output
			group_output = geometry_nodes_001.nodes.new("NodeGroupOutput")

			#node Transform Geometry.002
			transform_geometry_002 = geometry_nodes_001.nodes.new("GeometryNodeTransform")
			#Translation
			transform_geometry_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

			#node Points
			points = geometry_nodes_001.nodes.new("GeometryNodePoints")
			#Count
			points.inputs[0].default_value = 40
			#Position
			points.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Radius
			points.inputs[2].default_value = 0.10000000149011612

			#node Random Value
			random_value = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value.data_type = 'FLOAT_VECTOR'
			#Min
			random_value.inputs[0].default_value = (-0.20000000298023224, -0.20000000298023224, 0.0)
			#Max
			random_value.inputs[1].default_value = (0.20000000298023224, 0.20000000298023224, 54.5)
			#Min_001
			random_value.inputs[2].default_value = 0.0
			#Max_001
			random_value.inputs[3].default_value = 1.0
			#Min_002
			random_value.inputs[4].default_value = 0
			#Max_002
			random_value.inputs[5].default_value = 100
			#Probability
			random_value.inputs[6].default_value = 0.5
			#ID
			random_value.inputs[7].default_value = 0
			#Seed
			random_value.inputs[8].default_value = 0

			#node Random Value.001
			random_value_001 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_001.data_type = 'FLOAT'
			#Min
			random_value_001.inputs[0].default_value = (-0.20000000298023224, -0.20000000298023224, 0.0)
			#Max
			random_value_001.inputs[1].default_value = (0.20000000298023224, 0.20000000298023224, 54.5)
			#Min_001
			random_value_001.inputs[2].default_value = 0.30000001192092896
			#Max_001
			random_value_001.inputs[3].default_value = 0.6000000238418579
			#Min_002
			random_value_001.inputs[4].default_value = 0
			#Max_002
			random_value_001.inputs[5].default_value = 100
			#Probability
			random_value_001.inputs[6].default_value = 0.5
			#ID
			random_value_001.inputs[7].default_value = 0
			#Seed
			random_value_001.inputs[8].default_value = 0

			#node Curve Line.001
			curve_line_001 = geometry_nodes_001.nodes.new("GeometryNodeCurvePrimitiveLine")
			curve_line_001.mode = 'POINTS'
			#Start
			curve_line_001.inputs[0].default_value = (0.0, 0.0, -1.5)
			#End
			curve_line_001.inputs[1].default_value = (0.0, 0.0, 1.5)
			#Direction
			curve_line_001.inputs[2].default_value = (0.0, 0.0, 1.0)
			#Length
			curve_line_001.inputs[3].default_value = 1.0

			#node Instance on Points.001
			instance_on_points_001 = geometry_nodes_001.nodes.new("GeometryNodeInstanceOnPoints")
			#Selection
			instance_on_points_001.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001.inputs[3].default_value = False
			#Instance Index
			instance_on_points_001.inputs[4].default_value = 0

			#node Translate Instances
			translate_instances = geometry_nodes_001.nodes.new("GeometryNodeTranslateInstances")
			#Selection
			translate_instances.inputs[1].default_value = True
			#Translation
			translate_instances.inputs[2].default_value = (0.0, 0.0, 1.5)
			#Local Space
			translate_instances.inputs[3].default_value = False

			#node Join Geometry
			join_geometry = geometry_nodes_001.nodes.new("GeometryNodeJoinGeometry")

			#node Vector Math.005
			vector_math_005 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_005.operation = 'SCALE'
			#Vector_001
			vector_math_005.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Vector_002
			vector_math_005.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_005.inputs[3].default_value = 0.07000000029802322

			#node Transform Geometry.001
			transform_geometry_001 = geometry_nodes_001.nodes.new("GeometryNodeTransform")
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, -1.4999998807907104)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (0.05000000074505806, 0.029999999329447746, 0.09000000357627869)

			#node Vector Math.004
			vector_math_004 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_004.operation = 'SUBTRACT'
			#Vector_001
			vector_math_004.inputs[1].default_value = (0.5, 0.5, 0.5)
			#Vector_002
			vector_math_004.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_004.inputs[3].default_value = 1.0

			#node UV Sphere.001
			uv_sphere_001 = geometry_nodes_001.nodes.new("GeometryNodeMeshUVSphere")
			#Segments
			uv_sphere_001.inputs[0].default_value = 32
			#Rings
			uv_sphere_001.inputs[1].default_value = 16
			#Radius
			uv_sphere_001.inputs[2].default_value = 1.0

			#node Noise Texture
			noise_texture = geometry_nodes_001.nodes.new("ShaderNodeTexNoise")
			noise_texture.noise_dimensions = '3D'
			#Vector
			noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
			#W
			noise_texture.inputs[1].default_value = 0.0
			#Scale
			noise_texture.inputs[2].default_value = 2.0
			#Detail
			noise_texture.inputs[3].default_value = 5.0
			#Roughness
			noise_texture.inputs[4].default_value = 0.5
			#Distortion
			noise_texture.inputs[5].default_value = 0.0

			#node Curve Circle.001
			curve_circle_001 = geometry_nodes_001.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_001.mode = 'RADIUS'
			#Resolution
			curve_circle_001.inputs[0].default_value = 6
			#Point 1
			curve_circle_001.inputs[1].default_value = (-1.0, 0.0, 0.0)
			#Point 2
			curve_circle_001.inputs[2].default_value = (0.0, 1.0, 0.0)
			#Point 3
			curve_circle_001.inputs[3].default_value = (1.0, 0.0, 0.0)
			#Radius
			curve_circle_001.inputs[4].default_value = 0.006670000031590462

			#node Set Position
			set_position = geometry_nodes_001.nodes.new("GeometryNodeSetPosition")
			#Selection
			set_position.inputs[1].default_value = True
			#Position
			set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

			#node Curve to Mesh.001
			curve_to_mesh_001 = geometry_nodes_001.nodes.new("GeometryNodeCurveToMesh")
			#Fill Caps
			curve_to_mesh_001.inputs[2].default_value = False

			#node Join Geometry.001
			join_geometry_001 = geometry_nodes_001.nodes.new("GeometryNodeJoinGeometry")

			#node Realize Instances
			realize_instances = geometry_nodes_001.nodes.new("GeometryNodeRealizeInstances")

			#node Transform Geometry.003
			transform_geometry_003 = geometry_nodes_001.nodes.new("GeometryNodeTransform")
			#Translation
			transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

			#node Realize Instances.001
			realize_instances_001 = geometry_nodes_001.nodes.new("GeometryNodeRealizeInstances")

			#node Store Named Attribute.002
			store_named_attribute_002 = geometry_nodes_001.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.data_type = 'FLOAT_VECTOR'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "rot"
			#Value_Color
			store_named_attribute_002.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			store_named_attribute_002.inputs[6].default_value = False
			#Value_Int
			store_named_attribute_002.inputs[7].default_value = 0

			#node Distribute Points on Faces
			distribute_points_on_faces = geometry_nodes_001.nodes.new("GeometryNodeDistributePointsOnFaces")
			distribute_points_on_faces.distribute_method = 'RANDOM'
			#Selection
			distribute_points_on_faces.inputs[1].default_value = True
			#Distance Min
			distribute_points_on_faces.inputs[2].default_value = 0.0
			#Density Max
			distribute_points_on_faces.inputs[3].default_value = 10.0
			#Density
			distribute_points_on_faces.inputs[4].default_value = 6471.0
			#Density Factor
			distribute_points_on_faces.inputs[5].default_value = 1.0
			#Seed
			distribute_points_on_faces.inputs[6].default_value = 0

			#node Index
			index = geometry_nodes_001.nodes.new("GeometryNodeInputIndex")

			#node Store Named Attribute.003
			store_named_attribute_003 = geometry_nodes_001.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.data_type = 'FLOAT_VECTOR'
			store_named_attribute_003.domain = 'POINT'
			#Selection
			store_named_attribute_003.inputs[1].default_value = True
			#Name
			store_named_attribute_003.inputs[2].default_value = "norm"
			#Value_Color
			store_named_attribute_003.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			store_named_attribute_003.inputs[6].default_value = False
			#Value_Int
			store_named_attribute_003.inputs[7].default_value = 0

			#node Set Point Radius
			set_point_radius = geometry_nodes_001.nodes.new("GeometryNodeSetPointRadius")
			#Selection
			set_point_radius.inputs[1].default_value = True
			#Radius
			set_point_radius.inputs[2].default_value = 0.004999999888241291

			#node Store Named Attribute.004
			store_named_attribute_004 = geometry_nodes_001.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.data_type = 'FLOAT_VECTOR'
			store_named_attribute_004.domain = 'POINT'
			#Selection
			store_named_attribute_004.inputs[1].default_value = True
			#Name
			store_named_attribute_004.inputs[2].default_value = "pos"
			#Value_Float
			store_named_attribute_004.inputs[4].default_value = 0.0
			#Value_Color
			store_named_attribute_004.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			store_named_attribute_004.inputs[6].default_value = False
			#Value_Int
			store_named_attribute_004.inputs[7].default_value = 0

			#node Position.003
			position_003 = geometry_nodes_001.nodes.new("GeometryNodeInputPosition")

			#node Position.002
			position_002 = geometry_nodes_001.nodes.new("GeometryNodeInputPosition")

			#node Sample Index
			sample_index = geometry_nodes_001.nodes.new("GeometryNodeSampleIndex")
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			#Value_Float
			sample_index.inputs[1].default_value = 0.0
			#Value_Int
			sample_index.inputs[2].default_value = 0
			#Value_Color
			sample_index.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			sample_index.inputs[5].default_value = False

			#node Simulation Input.001
			simulation_input_001 = geometry_nodes_001.nodes.new("GeometryNodeSimulationInput")
			#node Random Value.003
			random_value_003 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_003.data_type = 'FLOAT_VECTOR'
			#Min
			random_value_003.inputs[0].default_value = (0.05000000074505806, -0.009999999776482582, -0.009999999776482582)
			#Max
			random_value_003.inputs[1].default_value = (0.10000000149011612, 0.009999999776482582, 0.009999999776482582)
			#Min_001
			random_value_003.inputs[2].default_value = 0.0
			#Max_001
			random_value_003.inputs[3].default_value = 1.0
			#Min_002
			random_value_003.inputs[4].default_value = 0
			#Max_002
			random_value_003.inputs[5].default_value = 100
			#Probability
			random_value_003.inputs[6].default_value = 0.5
			#ID
			random_value_003.inputs[7].default_value = 0
			#Seed
			random_value_003.inputs[8].default_value = 0

			#node Set Position.002
			set_position_002 = geometry_nodes_001.nodes.new("GeometryNodeSetPosition")
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)

			#node Math.004
			math_004 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_004.operation = 'SUBTRACT'
			#Value
			math_004.inputs[0].default_value = 1.0000001192092896
			#Value_002
			math_004.inputs[2].default_value = 0.5

			#node Set Position.003
			set_position_003 = geometry_nodes_001.nodes.new("GeometryNodeSetPosition")
			#Position
			set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

			#node Random Value.002
			random_value_002 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_002.data_type = 'BOOLEAN'
			#Min
			random_value_002.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Max
			random_value_002.inputs[1].default_value = (1.0, 1.0, 1.0)
			#Min_001
			random_value_002.inputs[2].default_value = 0.0
			#Max_001
			random_value_002.inputs[3].default_value = 1.0
			#Min_002
			random_value_002.inputs[4].default_value = 0
			#Max_002
			random_value_002.inputs[5].default_value = 100
			#Probability
			random_value_002.inputs[6].default_value = 0.020453043282032013
			#ID
			random_value_002.inputs[7].default_value = 0
			#Seed
			random_value_002.inputs[8].default_value = 0

			#node Compare.002
			compare_002 = geometry_nodes_001.nodes.new("FunctionNodeCompare")
			compare_002.data_type = 'FLOAT'
			compare_002.operation = 'GREATER_THAN'
			compare_002.mode = 'ELEMENT'
			#B
			compare_002.inputs[1].default_value = 0.05000000074505806
			#A_INT
			compare_002.inputs[2].default_value = 0
			#B_INT
			compare_002.inputs[3].default_value = 0
			#A_VEC3
			compare_002.inputs[4].default_value = (0.0, 0.0, 0.0)
			#B_VEC3
			compare_002.inputs[5].default_value = (0.0, 0.0, 0.0)
			#A_COL
			compare_002.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
			#B_COL
			compare_002.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
			#A_STR
			compare_002.inputs[8].default_value = ""
			#B_STR
			compare_002.inputs[9].default_value = ""
			#C
			compare_002.inputs[10].default_value = 0.8999999761581421
			#Angle
			compare_002.inputs[11].default_value = 0.08726649731397629
			#Epsilon
			compare_002.inputs[12].default_value = 0.0010000000474974513

			#node Simulation Output.001
			simulation_output_001 = geometry_nodes_001.nodes.new("GeometryNodeSimulationOutput")
			#remove generated sim state items
			for item in simulation_output_001.state_items:
				simulation_output_001.state_items.remove(item)
			#create SSI "Geometry"
			simulation_output_001.state_items.new('GEOMETRY', "Geometry")
			simulation_output_001.state_items[0].attribute_domain = 'POINT'

			#node Named Attribute.002
			named_attribute_002 = geometry_nodes_001.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002.inputs[0].default_value = "norm"

			#node Named Attribute.003
			named_attribute_003 = geometry_nodes_001.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "rot"

			#node Store Named Attribute.005
			store_named_attribute_005 = geometry_nodes_001.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.data_type = 'FLOAT'
			store_named_attribute_005.domain = 'POINT'
			#Selection
			store_named_attribute_005.inputs[1].default_value = True
			#Name
			store_named_attribute_005.inputs[2].default_value = "off"
			#Value_Vector
			store_named_attribute_005.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Value_Color
			store_named_attribute_005.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			store_named_attribute_005.inputs[6].default_value = False
			#Value_Int
			store_named_attribute_005.inputs[7].default_value = 0

			#node Math.001
			math_001 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_001.operation = 'ADD'
			math_001.use_clamp = True
			#Value_002
			math_001.inputs[2].default_value = 0.5

			#node Random Value.004
			random_value_004 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_004.data_type = 'FLOAT'
			#Min
			random_value_004.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Max
			random_value_004.inputs[1].default_value = (1.0, 1.0, 1.0)
			#Min_001
			random_value_004.inputs[2].default_value = 0.35999998450279236
			#Max_001
			random_value_004.inputs[3].default_value = 0.30000001192092896
			#Min_002
			random_value_004.inputs[4].default_value = 0
			#Max_002
			random_value_004.inputs[5].default_value = 100
			#Probability
			random_value_004.inputs[6].default_value = 0.5
			#ID
			random_value_004.inputs[7].default_value = 0
			#Seed
			random_value_004.inputs[8].default_value = 0

			#node Separate XYZ.001
			separate_xyz_001 = geometry_nodes_001.nodes.new("ShaderNodeSeparateXYZ")

			#node Vector Math.006
			vector_math_006 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_006.operation = 'SCALE'
			#Vector_001
			vector_math_006.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Vector_002
			vector_math_006.inputs[2].default_value = (0.0, 0.0, 0.0)

			#node Vector Math.009
			vector_math_009 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_009.operation = 'ADD'
			#Vector_002
			vector_math_009.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_009.inputs[3].default_value = 1.0

			#node Instance on Points.002
			instance_on_points_002 = geometry_nodes_001.nodes.new("GeometryNodeInstanceOnPoints")
			#Selection
			instance_on_points_002.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_002.inputs[3].default_value = False
			#Instance Index
			instance_on_points_002.inputs[4].default_value = 0

			#node Random Value.007
			random_value_007 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_007.data_type = 'FLOAT_VECTOR'
			#Min
			random_value_007.inputs[0].default_value = (-0.029999999329447746, -0.029999999329447746, -0.029999999329447746)
			#Max
			random_value_007.inputs[1].default_value = (0.029999999329447746, 0.029999999329447746, 0.029999999329447746)
			#Min_001
			random_value_007.inputs[2].default_value = 0.0
			#Max_001
			random_value_007.inputs[3].default_value = 1.0
			#Min_002
			random_value_007.inputs[4].default_value = 0
			#Max_002
			random_value_007.inputs[5].default_value = 100
			#Probability
			random_value_007.inputs[6].default_value = 0.5
			#ID
			random_value_007.inputs[7].default_value = 0
			#Seed
			random_value_007.inputs[8].default_value = 0

			#node Set Position.004
			set_position_004 = geometry_nodes_001.nodes.new("GeometryNodeSetPosition")
			#Selection
			set_position_004.inputs[1].default_value = True
			#Position
			set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)

			#node Random Value.005
			random_value_005 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_005.data_type = 'FLOAT_VECTOR'
			#Min
			random_value_005.inputs[0].default_value = (-40.79999923706055, -21.899999618530273, -21.899999618530273)
			#Max
			random_value_005.inputs[1].default_value = (15.600000381469727, 15.600000381469727, 15.600000381469727)
			#Min_001
			random_value_005.inputs[2].default_value = 0.1599999964237213
			#Max_001
			random_value_005.inputs[3].default_value = 0.30000001192092896
			#Min_002
			random_value_005.inputs[4].default_value = 0
			#Max_002
			random_value_005.inputs[5].default_value = 100
			#Probability
			random_value_005.inputs[6].default_value = 0.5
			#ID
			random_value_005.inputs[7].default_value = 0
			#Seed
			random_value_005.inputs[8].default_value = 0

			#node Math.005
			math_005 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_005.operation = 'ADD'
			#Value_001
			math_005.inputs[1].default_value = 0.05999999865889549
			#Value_002
			math_005.inputs[2].default_value = 0.5

			#node Map Range
			map_range = geometry_nodes_001.nodes.new("ShaderNodeMapRange")
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			map_range.clamp = True
			#From Min
			map_range.inputs[1].default_value = 0.1599999964237213
			#From Max
			map_range.inputs[2].default_value = 0.30000001192092896
			#To Min
			map_range.inputs[3].default_value = 0.07100000232458115
			#To Max
			map_range.inputs[4].default_value = 0.15000000596046448
			#Steps
			map_range.inputs[5].default_value = 4.0
			#Vector
			map_range.inputs[6].default_value = (0.0, 0.0, 0.0)
			#From_Min_FLOAT3
			map_range.inputs[7].default_value = (0.0, 0.0, 0.0)
			#From_Max_FLOAT3
			map_range.inputs[8].default_value = (1.0, 1.0, 1.0)
			#To_Min_FLOAT3
			map_range.inputs[9].default_value = (0.0, 0.0, 0.0)
			#To_Max_FLOAT3
			map_range.inputs[10].default_value = (1.0, 1.0, 1.0)
			#Steps_FLOAT3
			map_range.inputs[11].default_value = (4.0, 4.0, 4.0)

			#node Join Geometry.002
			join_geometry_002 = geometry_nodes_001.nodes.new("GeometryNodeJoinGeometry")

			#node Named Attribute.004
			named_attribute_004 = geometry_nodes_001.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.data_type = 'FLOAT'
			#Name
			named_attribute_004.inputs[0].default_value = "off"

			#node Math.006
			math_006 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_006.operation = 'SUBTRACT'
			#Value
			math_006.inputs[0].default_value = 1.0
			#Value_002
			math_006.inputs[2].default_value = 0.5

			#node Random Value.006
			random_value_006 = geometry_nodes_001.nodes.new("FunctionNodeRandomValue")
			random_value_006.data_type = 'FLOAT'
			#Min
			random_value_006.inputs[0].default_value = (-21.899999618530273, -21.899999618530273, -21.899999618530273)
			#Max
			random_value_006.inputs[1].default_value = (15.600000381469727, 15.600000381469727, 15.600000381469727)
			#Min_001
			random_value_006.inputs[2].default_value = 0.0
			#Max_001
			random_value_006.inputs[3].default_value = 1.0
			#Min_002
			random_value_006.inputs[4].default_value = 0
			#Max_002
			random_value_006.inputs[5].default_value = 100
			#Probability
			random_value_006.inputs[6].default_value = 0.5
			#ID
			random_value_006.inputs[7].default_value = 0
			#Seed
			random_value_006.inputs[8].default_value = 0

			#node Scene Time.001
			scene_time_001 = geometry_nodes_001.nodes.new("GeometryNodeInputSceneTime")

			#node Vector Math.007
			vector_math_007 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_007.operation = 'NORMALIZE'
			#Vector_001
			vector_math_007.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Vector_002
			vector_math_007.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_007.inputs[3].default_value = 1.0

			#node Vector Math.008
			vector_math_008 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_008.operation = 'SCALE'
			#Vector_001
			vector_math_008.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Vector_002
			vector_math_008.inputs[2].default_value = (0.0, 0.0, 0.0)

			#node Math.007
			math_007 = geometry_nodes_001.nodes.new("ShaderNodeMath")
			math_007.operation = 'MULTIPLY'
			#Value_002
			math_007.inputs[2].default_value = 0.5

			#node Vector Math.002
			vector_math_002 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_002.operation = 'ADD'
			#Vector_002
			vector_math_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_002.inputs[3].default_value = 1.0

			#node Endpoint Selection
			endpoint_selection = geometry_nodes_001.nodes.new("GeometryNodeCurveEndpointSelection")
			#Start Size
			endpoint_selection.inputs[0].default_value = 0
			#End Size
			endpoint_selection.inputs[1].default_value = 1

			#initialize redistribute_curve_points node group
			def redistribute_curve_points_node_group():
				redistribute_curve_points= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Redistribute Curve Points")

				#initialize redistribute_curve_points nodes
				#node Frame
				frame_1 = redistribute_curve_points.nodes.new("NodeFrame")

				#node Frame.004
				frame_004 = redistribute_curve_points.nodes.new("NodeFrame")
				frame_004.label = "Equidistant Distribution"

				#node Frame.003
				frame_003_1 = redistribute_curve_points.nodes.new("NodeFrame")

				#node Frame.002
				frame_002_1 = redistribute_curve_points.nodes.new("NodeFrame")
				frame_002_1.label = "Resample Position Along Curves"

				#node Frame.001
				frame_001_1 = redistribute_curve_points.nodes.new("NodeFrame")
				frame_001_1.label = "Mask Selection"

				#redistribute_curve_points inputs
				#input Curves
				redistribute_curve_points.inputs.new('NodeSocketGeometry', "Curves")
				redistribute_curve_points.inputs[0].attribute_domain = 'POINT'

				#input Factor
				redistribute_curve_points.inputs.new('NodeSocketFloatFactor', "Factor")
				redistribute_curve_points.inputs[1].default_value = 1.0
				redistribute_curve_points.inputs[1].min_value = 0.0
				redistribute_curve_points.inputs[1].max_value = 1.0
				redistribute_curve_points.inputs[1].attribute_domain = 'POINT'
				redistribute_curve_points.inputs[1].description = "Factor to blend overall effect"

				#input Feature Awareness
				redistribute_curve_points.inputs.new('NodeSocketBool', "Feature Awareness")
				redistribute_curve_points.inputs[2].default_value = False
				redistribute_curve_points.inputs[2].attribute_domain = 'POINT'
				redistribute_curve_points.inputs[2].description = "Use simeple feature awareness to keep feature definition"


				#node Group Input
				group_input_1 = redistribute_curve_points.nodes.new("NodeGroupInput")
				group_input_1.outputs[1].hide = True
				group_input_1.outputs[2].hide = True
				group_input_1.outputs[3].hide = True

				#node Blur Attribute
				blur_attribute = redistribute_curve_points.nodes.new("GeometryNodeBlurAttribute")
				blur_attribute.data_type = 'FLOAT'
				#Value_Int
				blur_attribute.inputs[1].default_value = 0
				#Value_Vector
				blur_attribute.inputs[2].default_value = (0.0, 0.0, 0.0)
				#Value_Color
				blur_attribute.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
				#Iterations
				blur_attribute.inputs[4].default_value = 10

				#node Spline Parameter.001
				spline_parameter_001 = redistribute_curve_points.nodes.new("GeometryNodeSplineParameter")
				spline_parameter_001.outputs[1].hide = True
				spline_parameter_001.outputs[2].hide = True

				#node Spline Parameter
				spline_parameter_1 = redistribute_curve_points.nodes.new("GeometryNodeSplineParameter")
				spline_parameter_1.outputs[1].hide = True
				spline_parameter_1.outputs[2].hide = True

				#node Group Input.002
				group_input_002 = redistribute_curve_points.nodes.new("NodeGroupInput")
				group_input_002.outputs[0].hide = True
				group_input_002.outputs[2].hide = True
				group_input_002.outputs[3].hide = True

				#node Group Input.001
				group_input_001 = redistribute_curve_points.nodes.new("NodeGroupInput")
				group_input_001.outputs[0].hide = True
				group_input_001.outputs[1].hide = True
				group_input_001.outputs[3].hide = True

				#node Set Position.002
				set_position_002_1 = redistribute_curve_points.nodes.new("GeometryNodeSetPosition")
				set_position_002_1.inputs[3].hide = True
				#Offset
				set_position_002_1.inputs[3].default_value = (0.0, 0.0, 0.0)

				#node Reroute.002
				reroute_002 = redistribute_curve_points.nodes.new("NodeReroute")
				#redistribute_curve_points outputs
				#output Curves
				redistribute_curve_points.outputs.new('NodeSocketGeometry', "Curves")
				redistribute_curve_points.outputs[0].attribute_domain = 'POINT'


				#node Group Output
				group_output_1 = redistribute_curve_points.nodes.new("NodeGroupOutput")

				#node Sample Curve.001
				sample_curve_001 = redistribute_curve_points.nodes.new("GeometryNodeSampleCurve")
				sample_curve_001.data_type = 'FLOAT_VECTOR'
				sample_curve_001.mode = 'FACTOR'
				sample_curve_001.inputs[1].hide = True
				sample_curve_001.inputs[2].hide = True
				sample_curve_001.inputs[3].hide = True
				sample_curve_001.inputs[4].hide = True
				sample_curve_001.inputs[5].hide = True
				sample_curve_001.inputs[7].hide = True
				sample_curve_001.outputs[0].hide = True
				sample_curve_001.outputs[1].hide = True
				sample_curve_001.outputs[2].hide = True
				sample_curve_001.outputs[3].hide = True
				sample_curve_001.outputs[4].hide = True
				sample_curve_001.outputs[6].hide = True
				sample_curve_001.outputs[7].hide = True
				#Value_Float
				sample_curve_001.inputs[1].default_value = 0.0
				#Value_Int
				sample_curve_001.inputs[2].default_value = 0
				#Value_Vector
				sample_curve_001.inputs[3].default_value = (0.0, 0.0, 0.0)
				#Value_Color
				sample_curve_001.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
				#Value_Bool
				sample_curve_001.inputs[5].default_value = False
				#Length
				sample_curve_001.inputs[7].default_value = 0.9999999403953552

				#node Mix.001
				mix_001 = redistribute_curve_points.nodes.new("ShaderNodeMix")
				mix_001.data_type = 'FLOAT'
				mix_001.blend_type = 'MIX'
				mix_001.clamp_factor = True
				mix_001.factor_mode = 'UNIFORM'
				#Factor_Vector
				mix_001.inputs[1].default_value = (0.5, 0.5, 0.5)
				#A_Vector
				mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
				#B_Vector
				mix_001.inputs[5].default_value = (0.0, 0.0, 0.0)
				#A_Color
				mix_001.inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)
				#B_Color
				mix_001.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)

				#node Switch
				switch = redistribute_curve_points.nodes.new("GeometryNodeSwitch")
				switch.input_type = 'FLOAT'
				#Switch_001
				switch.inputs[1].default_value = False
				#False_001
				switch.inputs[4].default_value = 0
				#True_001
				switch.inputs[5].default_value = 0
				#False_002
				switch.inputs[6].default_value = False
				#True_002
				switch.inputs[7].default_value = True
				#False_003
				switch.inputs[8].default_value = (0.0, 0.0, 0.0)
				#True_003
				switch.inputs[9].default_value = (0.0, 0.0, 0.0)
				#False_004
				switch.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
				#True_004
				switch.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
				#False_005
				switch.inputs[12].default_value = ""
				#True_005
				switch.inputs[13].default_value = ""

				#node Spline Parameter.002
				spline_parameter_002 = redistribute_curve_points.nodes.new("GeometryNodeSplineParameter")
				spline_parameter_002.outputs[0].hide = True
				spline_parameter_002.outputs[1].hide = True

				#node Math.002
				math_002_1 = redistribute_curve_points.nodes.new("ShaderNodeMath")
				math_002_1.operation = 'SUBTRACT'
				#Value_001
				math_002_1.inputs[1].default_value = 1.0
				#Value_002
				math_002_1.inputs[2].default_value = 0.5

				#initialize curve_info node group
				def curve_info_node_group():
					curve_info= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Curve Info")

					#initialize curve_info nodes
					#node Frame
					frame_2 = curve_info.nodes.new("NodeFrame")
					frame_2.label = "ID per Curve"

					#curve_info outputs
					#output Curve Index
					curve_info.outputs.new('NodeSocketInt', "Curve Index")
					curve_info.outputs[0].default_value = 0
					curve_info.outputs[0].min_value = -2147483648
					curve_info.outputs[0].max_value = 2147483647
					curve_info.outputs[0].attribute_domain = 'CURVE'
					curve_info.outputs[0].description = "Index of each Curve"

					#output Curve ID
					curve_info.outputs.new('NodeSocketInt', "Curve ID")
					curve_info.outputs[1].default_value = 0
					curve_info.outputs[1].min_value = -2147483648
					curve_info.outputs[1].max_value = 2147483647
					curve_info.outputs[1].attribute_domain = 'CURVE'
					curve_info.outputs[1].description = "ID of each Curve"

					#output Length
					curve_info.outputs.new('NodeSocketFloat', "Length")
					curve_info.outputs[2].default_value = 0.0
					curve_info.outputs[2].min_value = -3.4028234663852886e+38
					curve_info.outputs[2].max_value = 3.4028234663852886e+38
					curve_info.outputs[2].attribute_domain = 'CURVE'
					curve_info.outputs[2].description = "Length of each Curve"

					#output Direction
					curve_info.outputs.new('NodeSocketVector', "Direction")
					curve_info.outputs[3].default_value = (0.0, 0.0, 0.0)
					curve_info.outputs[3].min_value = -3.4028234663852886e+38
					curve_info.outputs[3].max_value = 3.4028234663852886e+38
					curve_info.outputs[3].attribute_domain = 'CURVE'
					curve_info.outputs[3].description = "Direction from root to tip of each Curve"

					#output Random
					curve_info.outputs.new('NodeSocketFloat', "Random")
					curve_info.outputs[4].default_value = 0.0
					curve_info.outputs[4].min_value = -3.4028234663852886e+38
					curve_info.outputs[4].max_value = 3.4028234663852886e+38
					curve_info.outputs[4].attribute_domain = 'CURVE'
					curve_info.outputs[4].description = "Random vector for each Curve"

					#output Surface UV
					curve_info.outputs.new('NodeSocketVector', "Surface UV")
					curve_info.outputs[5].default_value = (0.0, 0.0, 0.0)
					curve_info.outputs[5].min_value = -3.4028234663852886e+38
					curve_info.outputs[5].max_value = 3.4028234663852886e+38
					curve_info.outputs[5].attribute_domain = 'CURVE'
					curve_info.outputs[5].description = "Attachment surface UV coordinate of each Curve"


					#node Group Output
					group_output_2 = curve_info.nodes.new("NodeGroupOutput")

					#node Named Attribute
					named_attribute_1 = curve_info.nodes.new("GeometryNodeInputNamedAttribute")
					named_attribute_1.data_type = 'FLOAT_VECTOR'
					#Name
					named_attribute_1.inputs[0].default_value = "surface_uv_coordinate"

					#initialize curve_tip node group
					def curve_tip_node_group():
						curve_tip= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Curve Tip")

						#initialize curve_tip nodes
						#node Position.002
						position_002_1 = curve_tip.nodes.new("GeometryNodeInputPosition")

						#node Interpolate Domain
						interpolate_domain = curve_tip.nodes.new("GeometryNodeFieldOnDomain")
						interpolate_domain.data_type = 'INT'
						interpolate_domain.domain = 'CURVE'
						#Value_Float
						interpolate_domain.inputs[0].default_value = 0.0
						#Value_Vector
						interpolate_domain.inputs[2].default_value = (0.0, 0.0, 0.0)
						#Value_Color
						interpolate_domain.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						interpolate_domain.inputs[4].default_value = False

						#node Interpolate Domain.001
						interpolate_domain_001 = curve_tip.nodes.new("GeometryNodeFieldOnDomain")
						interpolate_domain_001.data_type = 'FLOAT_VECTOR'
						interpolate_domain_001.domain = 'CURVE'
						#Value_Float
						interpolate_domain_001.inputs[0].default_value = 0.0
						#Value_Int
						interpolate_domain_001.inputs[1].default_value = 0
						#Value_Color
						interpolate_domain_001.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						interpolate_domain_001.inputs[4].default_value = False

						#node Field at Index.003
						field_at_index_003 = curve_tip.nodes.new("GeometryNodeFieldAtIndex")
						field_at_index_003.data_type = 'FLOAT_VECTOR'
						field_at_index_003.domain = 'POINT'
						#Value_Float
						field_at_index_003.inputs[1].default_value = 0.0
						#Value_Int
						field_at_index_003.inputs[2].default_value = 0
						#Value_Color
						field_at_index_003.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						field_at_index_003.inputs[5].default_value = False

						#node Curve Tangent
						curve_tangent = curve_tip.nodes.new("GeometryNodeInputTangent")

						#node Endpoint Selection
						endpoint_selection_1 = curve_tip.nodes.new("GeometryNodeCurveEndpointSelection")
						#Start Size
						endpoint_selection_1.inputs[0].default_value = 0
						#End Size
						endpoint_selection_1.inputs[1].default_value = 1

						#node Field at Index.004
						field_at_index_004 = curve_tip.nodes.new("GeometryNodeFieldAtIndex")
						field_at_index_004.data_type = 'FLOAT_VECTOR'
						field_at_index_004.domain = 'POINT'
						#Value_Float
						field_at_index_004.inputs[1].default_value = 0.0
						#Value_Int
						field_at_index_004.inputs[2].default_value = 0
						#Value_Color
						field_at_index_004.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						field_at_index_004.inputs[5].default_value = False

						#node Interpolate Domain.002
						interpolate_domain_002 = curve_tip.nodes.new("GeometryNodeFieldOnDomain")
						interpolate_domain_002.data_type = 'FLOAT_VECTOR'
						interpolate_domain_002.domain = 'CURVE'
						#Value_Float
						interpolate_domain_002.inputs[0].default_value = 0.0
						#Value_Int
						interpolate_domain_002.inputs[1].default_value = 0
						#Value_Color
						interpolate_domain_002.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						interpolate_domain_002.inputs[4].default_value = False

						#curve_tip outputs
						#output Tip Selection
						curve_tip.outputs.new('NodeSocketBool', "Tip Selection")
						curve_tip.outputs[0].default_value = False
						curve_tip.outputs[0].attribute_domain = 'POINT'
						curve_tip.outputs[0].description = "Boolean selection of curve tip points"

						#output Tip Position
						curve_tip.outputs.new('NodeSocketVector', "Tip Position")
						curve_tip.outputs[1].default_value = (0.0, 0.0, 0.0)
						curve_tip.outputs[1].min_value = -3.4028234663852886e+38
						curve_tip.outputs[1].max_value = 3.4028234663852886e+38
						curve_tip.outputs[1].attribute_domain = 'CURVE'
						curve_tip.outputs[1].description = "Position of the tip point of a Curve"

						#output Tip Direction
						curve_tip.outputs.new('NodeSocketVector', "Tip Direction")
						curve_tip.outputs[2].default_value = (0.0, 0.0, 0.0)
						curve_tip.outputs[2].min_value = -3.4028234663852886e+38
						curve_tip.outputs[2].max_value = 3.4028234663852886e+38
						curve_tip.outputs[2].attribute_domain = 'CURVE'
						curve_tip.outputs[2].description = "Direction of the tip segment of a Curve"

						#output Tip Index
						curve_tip.outputs.new('NodeSocketInt', "Tip Index")
						curve_tip.outputs[3].default_value = 0
						curve_tip.outputs[3].min_value = -2147483648
						curve_tip.outputs[3].max_value = 2147483647
						curve_tip.outputs[3].attribute_domain = 'CURVE'
						curve_tip.outputs[3].description = "Index of the tip point of a Curve"


						#node Group Output
						group_output_3 = curve_tip.nodes.new("NodeGroupOutput")

						#node Points of Curve
						points_of_curve = curve_tip.nodes.new("GeometryNodePointsOfCurve")
						points_of_curve.inputs[0].hide = True
						points_of_curve.inputs[1].hide = True
						points_of_curve.outputs[1].hide = True
						#Curve Index
						points_of_curve.inputs[0].default_value = 0
						#Weights
						points_of_curve.inputs[1].default_value = 0.0
						#Sort Index
						points_of_curve.inputs[2].default_value = -1


						#Set locations
						position_002_1.location = (-628.2557983398438, -70.55813598632812)
						interpolate_domain.location = (-628.2557983398438, 90.18605041503906)
						interpolate_domain_001.location = (-246.4883575439453, 90.18605041503906)
						field_at_index_003.location = (-427.3255615234375, 90.18605041503906)
						curve_tangent.location = (-628.2557983398438, -231.3023223876953)
						endpoint_selection_1.location = (-246.4883575439453, 210.7441864013672)
						field_at_index_004.location = (-427.3255615234375, -90.65116882324219)
						interpolate_domain_002.location = (-246.4883575439453, -90.65116882324219)
						group_output_3.location = (75.0, 50.0)
						points_of_curve.location = (-829.18603515625, 50.0)

						#Set dimensions
						position_002_1.width, position_002_1.height = 140.0, 100.0
						interpolate_domain.width, interpolate_domain.height = 140.0, 100.0
						interpolate_domain_001.width, interpolate_domain_001.height = 140.0, 100.0
						field_at_index_003.width, field_at_index_003.height = 140.0, 100.0
						curve_tangent.width, curve_tangent.height = 140.0, 100.0
						endpoint_selection_1.width, endpoint_selection_1.height = 140.0, 100.0
						field_at_index_004.width, field_at_index_004.height = 140.0, 100.0
						interpolate_domain_002.width, interpolate_domain_002.height = 140.0, 100.0
						group_output_3.width, group_output_3.height = 140.0, 100.0
						points_of_curve.width, points_of_curve.height = 140.0, 100.0

						#initialize curve_tip links
						#position_002_1.Position -> field_at_index_003.Value
						curve_tip.links.new(position_002_1.outputs[0], field_at_index_003.inputs[3])
						#interpolate_domain.Value -> field_at_index_003.Index
						curve_tip.links.new(interpolate_domain.outputs[1], field_at_index_003.inputs[0])
						#points_of_curve.Point Index -> interpolate_domain.Value
						curve_tip.links.new(points_of_curve.outputs[0], interpolate_domain.inputs[1])
						#interpolate_domain_001.Value -> group_output_3.Tip Position
						curve_tip.links.new(interpolate_domain_001.outputs[2], group_output_3.inputs[1])
						#interpolate_domain.Value -> group_output_3.Tip Index
						curve_tip.links.new(interpolate_domain.outputs[1], group_output_3.inputs[3])
						#endpoint_selection_1.Selection -> group_output_3.Tip Selection
						curve_tip.links.new(endpoint_selection_1.outputs[0], group_output_3.inputs[0])
						#field_at_index_003.Value -> interpolate_domain_001.Value
						curve_tip.links.new(field_at_index_003.outputs[2], interpolate_domain_001.inputs[2])
						#interpolate_domain_002.Value -> group_output_3.Tip Direction
						curve_tip.links.new(interpolate_domain_002.outputs[2], group_output_3.inputs[2])
						#curve_tangent.Tangent -> field_at_index_004.Value
						curve_tip.links.new(curve_tangent.outputs[0], field_at_index_004.inputs[3])
						#interpolate_domain.Value -> field_at_index_004.Index
						curve_tip.links.new(interpolate_domain.outputs[1], field_at_index_004.inputs[0])
						#field_at_index_004.Value -> interpolate_domain_002.Value
						curve_tip.links.new(field_at_index_004.outputs[2], interpolate_domain_002.inputs[2])
						return curve_tip

					curve_tip = curve_tip_node_group()

					#node Group.002
					group_002 = curve_info.nodes.new("GeometryNodeGroup")
					group_002.outputs[0].hide = True
					group_002.outputs[2].hide = True
					group_002.outputs[3].hide = True
					group_002.node_tree = bpy.data.node_groups["Curve Tip"]

					#initialize curve_root node group
					def curve_root_node_group():
						curve_root= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Curve Root")

						#initialize curve_root nodes
						#node Position.002
						position_002_2 = curve_root.nodes.new("GeometryNodeInputPosition")

						#node Interpolate Domain
						interpolate_domain_1 = curve_root.nodes.new("GeometryNodeFieldOnDomain")
						interpolate_domain_1.data_type = 'INT'
						interpolate_domain_1.domain = 'CURVE'
						#Value_Float
						interpolate_domain_1.inputs[0].default_value = 0.0
						#Value_Vector
						interpolate_domain_1.inputs[2].default_value = (0.0, 0.0, 0.0)
						#Value_Color
						interpolate_domain_1.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						interpolate_domain_1.inputs[4].default_value = False

						#node Field at Index.003
						field_at_index_003_1 = curve_root.nodes.new("GeometryNodeFieldAtIndex")
						field_at_index_003_1.data_type = 'FLOAT_VECTOR'
						field_at_index_003_1.domain = 'POINT'
						#Value_Float
						field_at_index_003_1.inputs[1].default_value = 0.0
						#Value_Int
						field_at_index_003_1.inputs[2].default_value = 0
						#Value_Color
						field_at_index_003_1.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						field_at_index_003_1.inputs[5].default_value = False

						#node Interpolate Domain.001
						interpolate_domain_001_1 = curve_root.nodes.new("GeometryNodeFieldOnDomain")
						interpolate_domain_001_1.data_type = 'FLOAT_VECTOR'
						interpolate_domain_001_1.domain = 'CURVE'
						#Value_Float
						interpolate_domain_001_1.inputs[0].default_value = 0.0
						#Value_Int
						interpolate_domain_001_1.inputs[1].default_value = 0
						#Value_Color
						interpolate_domain_001_1.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						interpolate_domain_001_1.inputs[4].default_value = False

						#node Curve Tangent
						curve_tangent_1 = curve_root.nodes.new("GeometryNodeInputTangent")

						#node Endpoint Selection
						endpoint_selection_2 = curve_root.nodes.new("GeometryNodeCurveEndpointSelection")
						#Start Size
						endpoint_selection_2.inputs[0].default_value = 1
						#End Size
						endpoint_selection_2.inputs[1].default_value = 0

						#node Field at Index.004
						field_at_index_004_1 = curve_root.nodes.new("GeometryNodeFieldAtIndex")
						field_at_index_004_1.data_type = 'FLOAT_VECTOR'
						field_at_index_004_1.domain = 'POINT'
						#Value_Float
						field_at_index_004_1.inputs[1].default_value = 0.0
						#Value_Int
						field_at_index_004_1.inputs[2].default_value = 0
						#Value_Color
						field_at_index_004_1.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						field_at_index_004_1.inputs[5].default_value = False

						#node Interpolate Domain.002
						interpolate_domain_002_1 = curve_root.nodes.new("GeometryNodeFieldOnDomain")
						interpolate_domain_002_1.data_type = 'FLOAT_VECTOR'
						interpolate_domain_002_1.domain = 'CURVE'
						#Value_Float
						interpolate_domain_002_1.inputs[0].default_value = 0.0
						#Value_Int
						interpolate_domain_002_1.inputs[1].default_value = 0
						#Value_Color
						interpolate_domain_002_1.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
						#Value_Bool
						interpolate_domain_002_1.inputs[4].default_value = False

						#curve_root outputs
						#output Root Selection
						curve_root.outputs.new('NodeSocketBool', "Root Selection")
						curve_root.outputs[0].default_value = False
						curve_root.outputs[0].attribute_domain = 'POINT'
						curve_root.outputs[0].description = "Boolean selection of curve root points"

						#output Root Position
						curve_root.outputs.new('NodeSocketVector', "Root Position")
						curve_root.outputs[1].default_value = (0.0, 0.0, 0.0)
						curve_root.outputs[1].min_value = -3.4028234663852886e+38
						curve_root.outputs[1].max_value = 3.4028234663852886e+38
						curve_root.outputs[1].attribute_domain = 'CURVE'
						curve_root.outputs[1].description = "Position of the root point of a Curve"

						#output Root Direction
						curve_root.outputs.new('NodeSocketVector', "Root Direction")
						curve_root.outputs[2].default_value = (0.0, 0.0, 0.0)
						curve_root.outputs[2].min_value = -3.4028234663852886e+38
						curve_root.outputs[2].max_value = 3.4028234663852886e+38
						curve_root.outputs[2].attribute_domain = 'CURVE'
						curve_root.outputs[2].description = "Direction of the root segment of a Curve"

						#output Root Index
						curve_root.outputs.new('NodeSocketInt', "Root Index")
						curve_root.outputs[3].default_value = 0
						curve_root.outputs[3].min_value = -2147483648
						curve_root.outputs[3].max_value = 2147483647
						curve_root.outputs[3].attribute_domain = 'CURVE'
						curve_root.outputs[3].description = "Index of the root point of a Curve"


						#node Group Output
						group_output_4 = curve_root.nodes.new("NodeGroupOutput")

						#node Points of Curve
						points_of_curve_1 = curve_root.nodes.new("GeometryNodePointsOfCurve")
						points_of_curve_1.inputs[0].hide = True
						points_of_curve_1.inputs[1].hide = True
						points_of_curve_1.outputs[1].hide = True
						#Curve Index
						points_of_curve_1.inputs[0].default_value = 0
						#Weights
						points_of_curve_1.inputs[1].default_value = 0.0
						#Sort Index
						points_of_curve_1.inputs[2].default_value = 0


						#Set locations
						position_002_2.location = (-608.1627807617188, -70.55814361572266)
						interpolate_domain_1.location = (-608.1627807617188, 90.18604278564453)
						field_at_index_003_1.location = (-407.2325439453125, 70.09302520751953)
						interpolate_domain_001_1.location = (-206.30230712890625, 70.09302520751953)
						curve_tangent_1.location = (-608.1627807617188, -271.4883728027344)
						endpoint_selection_2.location = (-206.30230712890625, 190.65118408203125)
						field_at_index_004_1.location = (-407.2325439453125, -130.83721923828125)
						interpolate_domain_002_1.location = (-206.30230712890625, -130.83721923828125)
						group_output_4.location = (75.0, 50.0)
						points_of_curve_1.location = (-789.0, 50.0)

						#Set dimensions
						position_002_2.width, position_002_2.height = 140.0, 100.0
						interpolate_domain_1.width, interpolate_domain_1.height = 140.0, 100.0
						field_at_index_003_1.width, field_at_index_003_1.height = 140.0, 100.0
						interpolate_domain_001_1.width, interpolate_domain_001_1.height = 140.0, 100.0
						curve_tangent_1.width, curve_tangent_1.height = 140.0, 100.0
						endpoint_selection_2.width, endpoint_selection_2.height = 140.0, 100.0
						field_at_index_004_1.width, field_at_index_004_1.height = 140.0, 100.0
						interpolate_domain_002_1.width, interpolate_domain_002_1.height = 140.0, 100.0
						group_output_4.width, group_output_4.height = 140.0, 100.0
						points_of_curve_1.width, points_of_curve_1.height = 140.0, 100.0

						#initialize curve_root links
						#position_002_2.Position -> field_at_index_003_1.Value
						curve_root.links.new(position_002_2.outputs[0], field_at_index_003_1.inputs[3])
						#interpolate_domain_001_1.Value -> group_output_4.Root Position
						curve_root.links.new(interpolate_domain_001_1.outputs[2], group_output_4.inputs[1])
						#interpolate_domain_1.Value -> field_at_index_003_1.Index
						curve_root.links.new(interpolate_domain_1.outputs[1], field_at_index_003_1.inputs[0])
						#points_of_curve_1.Point Index -> interpolate_domain_1.Value
						curve_root.links.new(points_of_curve_1.outputs[0], interpolate_domain_1.inputs[1])
						#interpolate_domain_1.Value -> group_output_4.Root Index
						curve_root.links.new(interpolate_domain_1.outputs[1], group_output_4.inputs[3])
						#endpoint_selection_2.Selection -> group_output_4.Root Selection
						curve_root.links.new(endpoint_selection_2.outputs[0], group_output_4.inputs[0])
						#field_at_index_003_1.Value -> interpolate_domain_001_1.Value
						curve_root.links.new(field_at_index_003_1.outputs[2], interpolate_domain_001_1.inputs[2])
						#interpolate_domain_002_1.Value -> group_output_4.Root Direction
						curve_root.links.new(interpolate_domain_002_1.outputs[2], group_output_4.inputs[2])
						#interpolate_domain_1.Value -> field_at_index_004_1.Index
						curve_root.links.new(interpolate_domain_1.outputs[1], field_at_index_004_1.inputs[0])
						#curve_tangent_1.Tangent -> field_at_index_004_1.Value
						curve_root.links.new(curve_tangent_1.outputs[0], field_at_index_004_1.inputs[3])
						#field_at_index_004_1.Value -> interpolate_domain_002_1.Value
						curve_root.links.new(field_at_index_004_1.outputs[2], interpolate_domain_002_1.inputs[2])
						return curve_root

					curve_root = curve_root_node_group()

					#node Group.001
					group_001 = curve_info.nodes.new("GeometryNodeGroup")
					group_001.outputs[0].hide = True
					group_001.outputs[2].hide = True
					group_001.outputs[3].hide = True
					group_001.node_tree = bpy.data.node_groups["Curve Root"]

					#node Evaluate at Index
					evaluate_at_index = curve_info.nodes.new("GeometryNodeFieldAtIndex")
					evaluate_at_index.data_type = 'FLOAT'
					evaluate_at_index.domain = 'POINT'
					#Value_Int
					evaluate_at_index.inputs[2].default_value = 0
					#Value_Vector
					evaluate_at_index.inputs[3].default_value = (0.0, 0.0, 0.0)
					#Value_Color
					evaluate_at_index.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					evaluate_at_index.inputs[5].default_value = False

					#node Evaluate on Domain.001
					evaluate_on_domain_001 = curve_info.nodes.new("GeometryNodeFieldOnDomain")
					evaluate_on_domain_001.data_type = 'FLOAT'
					evaluate_on_domain_001.domain = 'CURVE'
					#Value_Int
					evaluate_on_domain_001.inputs[1].default_value = 0
					#Value_Vector
					evaluate_on_domain_001.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Value_Color
					evaluate_on_domain_001.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					evaluate_on_domain_001.inputs[4].default_value = False

					#node Group.003
					group_003 = curve_info.nodes.new("GeometryNodeGroup")
					group_003.outputs[0].hide = True
					group_003.outputs[1].hide = True
					group_003.outputs[2].hide = True
					group_003.node_tree = bpy.data.node_groups["Curve Root"]

					#node Random Value.002
					random_value_002_1 = curve_info.nodes.new("FunctionNodeRandomValue")
					random_value_002_1.data_type = 'FLOAT'
					#Min
					random_value_002_1.inputs[0].default_value = (0.0, 0.0, 0.0)
					#Max
					random_value_002_1.inputs[1].default_value = (1.0, 1.0, 1.0)
					#Min_001
					random_value_002_1.inputs[2].default_value = 0.0
					#Max_001
					random_value_002_1.inputs[3].default_value = 1.0
					#Min_002
					random_value_002_1.inputs[4].default_value = 0
					#Max_002
					random_value_002_1.inputs[5].default_value = 100
					#Probability
					random_value_002_1.inputs[6].default_value = 0.5
					#Seed
					random_value_002_1.inputs[8].default_value = 0

					#node Reroute
					reroute = curve_info.nodes.new("NodeReroute")
					#node Vector Math
					vector_math_1 = curve_info.nodes.new("ShaderNodeVectorMath")
					vector_math_1.operation = 'SUBTRACT'
					#Vector_002
					vector_math_1.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Scale
					vector_math_1.inputs[3].default_value = 1.0

					#node Vector Math.001
					vector_math_001_1 = curve_info.nodes.new("ShaderNodeVectorMath")
					vector_math_001_1.operation = 'NORMALIZE'
					#Vector_001
					vector_math_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
					#Vector_002
					vector_math_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Scale
					vector_math_001_1.inputs[3].default_value = 1.0

					#node Evaluate on Domain
					evaluate_on_domain = curve_info.nodes.new("GeometryNodeFieldOnDomain")
					evaluate_on_domain.data_type = 'INT'
					evaluate_on_domain.domain = 'CURVE'
					#Value_Float
					evaluate_on_domain.inputs[0].default_value = 0.0
					#Value_Vector
					evaluate_on_domain.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Value_Color
					evaluate_on_domain.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					evaluate_on_domain.inputs[4].default_value = False

					#node Index.001
					index_001 = curve_info.nodes.new("GeometryNodeInputIndex")

					#node Spline Length
					spline_length = curve_info.nodes.new("GeometryNodeSplineLength")
					spline_length.outputs[1].hide = True

					#node Evaluate at Index.001
					evaluate_at_index_001 = curve_info.nodes.new("GeometryNodeFieldAtIndex")
					evaluate_at_index_001.data_type = 'INT'
					evaluate_at_index_001.domain = 'POINT'
					#Value_Float
					evaluate_at_index_001.inputs[1].default_value = 0.0
					#Value_Vector
					evaluate_at_index_001.inputs[3].default_value = (0.0, 0.0, 0.0)
					#Value_Color
					evaluate_at_index_001.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					evaluate_at_index_001.inputs[5].default_value = False

					#node Evaluate on Domain.002
					evaluate_on_domain_002 = curve_info.nodes.new("GeometryNodeFieldOnDomain")
					evaluate_on_domain_002.data_type = 'INT'
					evaluate_on_domain_002.domain = 'CURVE'
					#Value_Float
					evaluate_on_domain_002.inputs[0].default_value = 0.0
					#Value_Color
					evaluate_on_domain_002.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					evaluate_on_domain_002.inputs[4].default_value = False

					#node Group
					group = curve_info.nodes.new("GeometryNodeGroup")
					group.outputs[0].hide = True
					group.outputs[1].hide = True
					group.outputs[2].hide = True
					group.node_tree = bpy.data.node_groups["Curve Root"]

					#node ID
					id = curve_info.nodes.new("GeometryNodeInputID")

					#Set parents
					evaluate_at_index_001.parent = frame_2
					evaluate_on_domain_002.parent = frame_2
					group.parent = frame_2
					id.parent = frame_2

					#Set locations
					frame_2.location = (-547.8837280273438, -130.83721923828125)
					group_output_2.location = (75.0, 50.0)
					named_attribute_1.location = (-166.11627197265625, -371.9534912109375)
					group_002.location = (-527.7907104492188, -90.65116882324219)
					group_001.location = (-527.7907104492188, -171.02325439453125)
					evaluate_at_index.location = (-346.9534912109375, -211.2093048095703)
					evaluate_on_domain_001.location = (-166.11627197265625, -211.2093048095703)
					group_003.location = (-527.7907104492188, -251.39535522460938)
					random_value_002_1.location = (-527.7907104492188, -331.7674560546875)
					reroute.location = (-608.162841796875, 29.906982421875)
					vector_math_1.location = (-346.9534912109375, -70.55814361572266)
					vector_math_001_1.location = (-166.11627197265625, -70.55814361572266)
					evaluate_on_domain.location = (-166.11627197265625, 70.093017578125)
					index_001.location = (-346.9534912109375, 110.27906799316406)
					spline_length.location = (-166.11627197265625, -10.279067993164062)
					evaluate_at_index_001.location = (-442.0465087890625, 241.1162872314453)
					evaluate_on_domain_002.location = (-261.2093200683594, 241.1162872314453)
					group.location = (-622.8837280273438, 221.02325439453125)
					id.location = (-622.8837280273438, 140.6511688232422)

					#Set dimensions
					frame_2.width, frame_2.height = 561.9534301757812, 225.93026733398438
					group_output_2.width, group_output_2.height = 140.0, 100.0
					named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
					group_002.width, group_002.height = 140.0, 100.0
					group_001.width, group_001.height = 140.0, 100.0
					evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
					evaluate_on_domain_001.width, evaluate_on_domain_001.height = 140.0, 100.0
					group_003.width, group_003.height = 140.0, 100.0
					random_value_002_1.width, random_value_002_1.height = 140.0, 100.0
					reroute.width, reroute.height = 16.0, 100.0
					vector_math_1.width, vector_math_1.height = 140.0, 100.0
					vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
					evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
					index_001.width, index_001.height = 140.0, 100.0
					spline_length.width, spline_length.height = 140.0, 100.0
					evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
					evaluate_on_domain_002.width, evaluate_on_domain_002.height = 140.0, 100.0
					group.width, group.height = 140.0, 100.0
					id.width, id.height = 140.0, 100.0

					#initialize curve_info links
					#index_001.Index -> evaluate_on_domain.Value
					curve_info.links.new(index_001.outputs[0], evaluate_on_domain.inputs[1])
					#evaluate_on_domain.Value -> group_output_2.Curve Index
					curve_info.links.new(evaluate_on_domain.outputs[1], group_output_2.inputs[0])
					#named_attribute_1.Attribute -> group_output_2.Surface UV
					curve_info.links.new(named_attribute_1.outputs[0], group_output_2.inputs[5])
					#evaluate_at_index_001.Value -> evaluate_on_domain_002.Value
					curve_info.links.new(evaluate_at_index_001.outputs[2], evaluate_on_domain_002.inputs[2])
					#evaluate_at_index_001.Value -> evaluate_on_domain_002.Value
					curve_info.links.new(evaluate_at_index_001.outputs[1], evaluate_on_domain_002.inputs[1])
					#group.Root Index -> evaluate_at_index_001.Index
					curve_info.links.new(group.outputs[3], evaluate_at_index_001.inputs[0])
					#reroute.Output -> group_output_2.Curve ID
					curve_info.links.new(reroute.outputs[0], group_output_2.inputs[1])
					#id.ID -> evaluate_at_index_001.Value
					curve_info.links.new(id.outputs[0], evaluate_at_index_001.inputs[2])
					#spline_length.Length -> group_output_2.Length
					curve_info.links.new(spline_length.outputs[0], group_output_2.inputs[2])
					#group_002.Tip Position -> vector_math_1.Vector
					curve_info.links.new(group_002.outputs[1], vector_math_1.inputs[0])
					#group_001.Root Position -> vector_math_1.Vector
					curve_info.links.new(group_001.outputs[1], vector_math_1.inputs[1])
					#vector_math_001_1.Vector -> group_output_2.Direction
					curve_info.links.new(vector_math_001_1.outputs[0], group_output_2.inputs[3])
					#vector_math_1.Vector -> vector_math_001_1.Vector
					curve_info.links.new(vector_math_1.outputs[0], vector_math_001_1.inputs[0])
					#reroute.Output -> random_value_002_1.ID
					curve_info.links.new(reroute.outputs[0], random_value_002_1.inputs[7])
					#evaluate_at_index.Value -> evaluate_on_domain_001.Value
					curve_info.links.new(evaluate_at_index.outputs[0], evaluate_on_domain_001.inputs[0])
					#evaluate_on_domain_001.Value -> group_output_2.Random
					curve_info.links.new(evaluate_on_domain_001.outputs[0], group_output_2.inputs[4])
					#random_value_002_1.Value -> evaluate_at_index.Value
					curve_info.links.new(random_value_002_1.outputs[1], evaluate_at_index.inputs[1])
					#group_003.Root Index -> evaluate_at_index.Index
					curve_info.links.new(group_003.outputs[3], evaluate_at_index.inputs[0])
					#evaluate_on_domain_002.Value -> reroute.Input
					curve_info.links.new(evaluate_on_domain_002.outputs[1], reroute.inputs[0])
					return curve_info

				curve_info = curve_info_node_group()

				#node Group.002
				group_002_1 = redistribute_curve_points.nodes.new("GeometryNodeGroup")
				group_002_1.outputs[1].hide = True
				group_002_1.outputs[2].hide = True
				group_002_1.outputs[3].hide = True
				group_002_1.outputs[4].hide = True
				group_002_1.outputs[5].hide = True
				group_002_1.node_tree = bpy.data.node_groups["Curve Info"]

				#node Points of Curve
				points_of_curve_2 = redistribute_curve_points.nodes.new("GeometryNodePointsOfCurve")
				points_of_curve_2.inputs[1].hide = True
				points_of_curve_2.inputs[2].hide = True
				points_of_curve_2.outputs[0].hide = True
				#Weights
				points_of_curve_2.inputs[1].default_value = 0.0
				#Sort Index
				points_of_curve_2.inputs[2].default_value = 0

				#node Math.001
				math_001_1 = redistribute_curve_points.nodes.new("ShaderNodeMath")
				math_001_1.operation = 'DIVIDE'
				#Value_002
				math_001_1.inputs[2].default_value = 0.5

				#node Endpoint Selection.001
				endpoint_selection_001 = redistribute_curve_points.nodes.new("GeometryNodeCurveEndpointSelection")
				#Start Size
				endpoint_selection_001.inputs[0].default_value = 1
				#End Size
				endpoint_selection_001.inputs[1].default_value = 1

				#initialize curve_segment node group
				def curve_segment_node_group():
					curve_segment= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Curve Segment")

					#initialize curve_segment nodes
					#node Vector Math.009
					vector_math_009_1 = curve_segment.nodes.new("ShaderNodeVectorMath")
					vector_math_009_1.operation = 'NORMALIZE'
					#Vector_001
					vector_math_009_1.inputs[1].default_value = (0.0, 0.0, 0.0)
					#Vector_002
					vector_math_009_1.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Scale
					vector_math_009_1.inputs[3].default_value = 1.0

					#node Reroute.015
					reroute_015 = curve_segment.nodes.new("NodeReroute")
					#node Reroute.017
					reroute_017 = curve_segment.nodes.new("NodeReroute")
					#node Field at Index.001
					field_at_index_001 = curve_segment.nodes.new("GeometryNodeFieldAtIndex")
					field_at_index_001.data_type = 'FLOAT_VECTOR'
					field_at_index_001.domain = 'POINT'
					#Value_Float
					field_at_index_001.inputs[1].default_value = 0.0
					#Value_Int
					field_at_index_001.inputs[2].default_value = 0
					#Value_Color
					field_at_index_001.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					field_at_index_001.inputs[5].default_value = False

					#node Vector Math.008
					vector_math_008_1 = curve_segment.nodes.new("ShaderNodeVectorMath")
					vector_math_008_1.operation = 'SUBTRACT'
					#Vector_002
					vector_math_008_1.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Scale
					vector_math_008_1.inputs[3].default_value = 1.0

					#node Reroute.018
					reroute_018 = curve_segment.nodes.new("NodeReroute")
					#node Interpolate Domain.002
					interpolate_domain_002_2 = curve_segment.nodes.new("GeometryNodeFieldOnDomain")
					interpolate_domain_002_2.data_type = 'FLOAT_VECTOR'
					interpolate_domain_002_2.domain = 'POINT'
					#Value_Float
					interpolate_domain_002_2.inputs[0].default_value = 0.0
					#Value_Int
					interpolate_domain_002_2.inputs[1].default_value = 0
					#Value_Color
					interpolate_domain_002_2.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					interpolate_domain_002_2.inputs[4].default_value = False

					#curve_segment outputs
					#output Segment Length
					curve_segment.outputs.new('NodeSocketFloat', "Segment Length")
					curve_segment.outputs[0].default_value = 0.0
					curve_segment.outputs[0].min_value = -3.4028234663852886e+38
					curve_segment.outputs[0].max_value = 3.4028234663852886e+38
					curve_segment.outputs[0].attribute_domain = 'POINT'
					curve_segment.outputs[0].description = "Distance to previous point on Curve"

					#output Segment Direction
					curve_segment.outputs.new('NodeSocketVector', "Segment Direction")
					curve_segment.outputs[1].default_value = (0.0, 0.0, 0.0)
					curve_segment.outputs[1].min_value = -3.4028234663852886e+38
					curve_segment.outputs[1].max_value = 3.4028234663852886e+38
					curve_segment.outputs[1].attribute_domain = 'POINT'
					curve_segment.outputs[1].description = "Direction from previous neighboring point on segment"

					#output Neighbor Index
					curve_segment.outputs.new('NodeSocketInt', "Neighbor Index")
					curve_segment.outputs[2].default_value = 0
					curve_segment.outputs[2].min_value = -2147483648
					curve_segment.outputs[2].max_value = 2147483647
					curve_segment.outputs[2].attribute_domain = 'POINT'
					curve_segment.outputs[2].description = "Index of previous neighboring point on segment"


					#node Group Output
					group_output_5 = curve_segment.nodes.new("NodeGroupOutput")

					#node Vector Math.007
					vector_math_007_1 = curve_segment.nodes.new("ShaderNodeVectorMath")
					vector_math_007_1.operation = 'LENGTH'
					#Vector_001
					vector_math_007_1.inputs[1].default_value = (0.0, 0.0, 0.0)
					#Vector_002
					vector_math_007_1.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Scale
					vector_math_007_1.inputs[3].default_value = 1.0

					#node Interpolate Domain.003
					interpolate_domain_003 = curve_segment.nodes.new("GeometryNodeFieldOnDomain")
					interpolate_domain_003.data_type = 'INT'
					interpolate_domain_003.domain = 'POINT'
					#Value_Float
					interpolate_domain_003.inputs[0].default_value = 0.0
					#Value_Vector
					interpolate_domain_003.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Value_Color
					interpolate_domain_003.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
					#Value_Bool
					interpolate_domain_003.inputs[4].default_value = False

					#node Reroute
					reroute_1 = curve_segment.nodes.new("NodeReroute")
					#node Switch.004
					switch_004 = curve_segment.nodes.new("GeometryNodeSwitch")
					switch_004.input_type = 'VECTOR'
					#Switch_001
					switch_004.inputs[1].default_value = False
					#False
					switch_004.inputs[2].default_value = 0.0
					#True
					switch_004.inputs[3].default_value = 0.0
					#False_001
					switch_004.inputs[4].default_value = 0
					#True_001
					switch_004.inputs[5].default_value = 0
					#False_002
					switch_004.inputs[6].default_value = False
					#True_002
					switch_004.inputs[7].default_value = True
					#False_003
					switch_004.inputs[8].default_value = (0.0, 0.0, 0.0)
					#False_004
					switch_004.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#True_004
					switch_004.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#False_005
					switch_004.inputs[12].default_value = ""
					#True_005
					switch_004.inputs[13].default_value = ""

					#node Switch.003
					switch_003 = curve_segment.nodes.new("GeometryNodeSwitch")
					switch_003.input_type = 'FLOAT'
					#Switch_001
					switch_003.inputs[1].default_value = False
					#False
					switch_003.inputs[2].default_value = 0.0
					#False_001
					switch_003.inputs[4].default_value = 0
					#True_001
					switch_003.inputs[5].default_value = 0
					#False_002
					switch_003.inputs[6].default_value = False
					#True_002
					switch_003.inputs[7].default_value = True
					#False_003
					switch_003.inputs[8].default_value = (0.0, 0.0, 0.0)
					#True_003
					switch_003.inputs[9].default_value = (0.0, 0.0, 0.0)
					#False_004
					switch_003.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#True_004
					switch_003.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#False_005
					switch_003.inputs[12].default_value = ""
					#True_005
					switch_003.inputs[13].default_value = ""

					#node Boolean
					boolean = curve_segment.nodes.new("FunctionNodeInputBool")
					boolean.boolean = True

					#node Interpolate Domain
					interpolate_domain_2 = curve_segment.nodes.new("GeometryNodeFieldOnDomain")
					interpolate_domain_2.data_type = 'BOOLEAN'
					interpolate_domain_2.domain = 'CURVE'
					#Value_Float
					interpolate_domain_2.inputs[0].default_value = 0.0
					#Value_Int
					interpolate_domain_2.inputs[1].default_value = 0
					#Value_Vector
					interpolate_domain_2.inputs[2].default_value = (0.0, 0.0, 0.0)
					#Value_Color
					interpolate_domain_2.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)

					#node Switch.005
					switch_005 = curve_segment.nodes.new("GeometryNodeSwitch")
					switch_005.input_type = 'INT'
					#Switch_001
					switch_005.inputs[1].default_value = False
					#False
					switch_005.inputs[2].default_value = 0.0
					#True
					switch_005.inputs[3].default_value = 0.0
					#False_001
					switch_005.inputs[4].default_value = 0
					#False_002
					switch_005.inputs[6].default_value = False
					#True_002
					switch_005.inputs[7].default_value = True
					#False_003
					switch_005.inputs[8].default_value = (0.0, 0.0, 0.0)
					#True_003
					switch_005.inputs[9].default_value = (0.0, 0.0, 0.0)
					#False_004
					switch_005.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#True_004
					switch_005.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#False_005
					switch_005.inputs[12].default_value = ""
					#True_005
					switch_005.inputs[13].default_value = ""

					#node Index.002
					index_002 = curve_segment.nodes.new("GeometryNodeInputIndex")

					#node Switch.001
					switch_001 = curve_segment.nodes.new("GeometryNodeSwitch")
					switch_001.input_type = 'INT'
					#Switch_001
					switch_001.inputs[1].default_value = False
					#False
					switch_001.inputs[2].default_value = 0.0
					#True
					switch_001.inputs[3].default_value = 0.0
					#False_002
					switch_001.inputs[6].default_value = False
					#True_002
					switch_001.inputs[7].default_value = True
					#False_003
					switch_001.inputs[8].default_value = (0.0, 0.0, 0.0)
					#True_003
					switch_001.inputs[9].default_value = (0.0, 0.0, 0.0)
					#False_004
					switch_001.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#True_004
					switch_001.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
					#False_005
					switch_001.inputs[12].default_value = ""
					#True_005
					switch_001.inputs[13].default_value = ""

					#node Offset Point in Curve
					offset_point_in_curve = curve_segment.nodes.new("GeometryNodeOffsetPointInCurve")
					#Point Index
					offset_point_in_curve.inputs[0].default_value = 0
					#Offset
					offset_point_in_curve.inputs[1].default_value = -1

					#node Position.002
					position_002_3 = curve_segment.nodes.new("GeometryNodeInputPosition")


					#Set locations
					vector_math_009_1.location = (-389.8524169921875, 30.443286895751953)
					reroute_015.location = (-456.8948974609375, 4.604297637939453)
					reroute_017.location = (-1012.7362060546875, -9.742748260498047)
					field_at_index_001.location = (-992.6431884765625, 70.62931823730469)
					vector_math_008_1.location = (-811.805908203125, 70.62931823730469)
					reroute_018.location = (-1032.8292236328125, 110.81541442871094)
					interpolate_domain_002_2.location = (-630.9686279296875, 70.62931823730469)
					group_output_5.location = (75.0, 50.0)
					vector_math_007_1.location = (-389.8524169921875, 151.00144958496094)
					interpolate_domain_003.location = (-390.85833740234375, -97.25408935546875)
					reroute_1.location = (-342.979248046875, 193.345458984375)
					switch_004.location = (-178.8756103515625, 10.35025405883789)
					switch_003.location = (-178.8756103515625, 90.72234344482422)
					boolean.location = (-781.6663208007812, 291.652587890625)
					interpolate_domain_2.location = (-600.8291015625, 311.74560546875)
					switch_005.location = (-178.8756103515625, -70.0218505859375)
					index_002.location = (-1404.550048828125, 211.28048706054688)
					switch_001.location = (-1223.712890625, 231.37350463867188)
					offset_point_in_curve.location = (-1404.550048828125, 151.0014190673828)
					position_002_3.location = (-1223.712890625, 30.44327163696289)

					#Set dimensions
					vector_math_009_1.width, vector_math_009_1.height = 140.0, 100.0
					reroute_015.width, reroute_015.height = 16.0, 100.0
					reroute_017.width, reroute_017.height = 16.0, 100.0
					field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
					vector_math_008_1.width, vector_math_008_1.height = 140.0, 100.0
					reroute_018.width, reroute_018.height = 16.0, 100.0
					interpolate_domain_002_2.width, interpolate_domain_002_2.height = 140.0, 100.0
					group_output_5.width, group_output_5.height = 140.0, 100.0
					vector_math_007_1.width, vector_math_007_1.height = 140.0, 100.0
					interpolate_domain_003.width, interpolate_domain_003.height = 140.0, 100.0
					reroute_1.width, reroute_1.height = 16.0, 100.0
					switch_004.width, switch_004.height = 140.0, 100.0
					switch_003.width, switch_003.height = 140.0, 100.0
					boolean.width, boolean.height = 140.0, 100.0
					interpolate_domain_2.width, interpolate_domain_2.height = 140.0, 100.0
					switch_005.width, switch_005.height = 140.0, 100.0
					index_002.width, index_002.height = 140.0, 100.0
					switch_001.width, switch_001.height = 140.0, 100.0
					offset_point_in_curve.width, offset_point_in_curve.height = 140.0, 100.0
					position_002_3.width, position_002_3.height = 140.0, 100.0

					#initialize curve_segment links
					#reroute_015.Output -> vector_math_007_1.Vector
					curve_segment.links.new(reroute_015.outputs[0], vector_math_007_1.inputs[0])
					#reroute_018.Output -> field_at_index_001.Index
					curve_segment.links.new(reroute_018.outputs[0], field_at_index_001.inputs[0])
					#vector_math_008_1.Vector -> interpolate_domain_002_2.Value
					curve_segment.links.new(vector_math_008_1.outputs[0], interpolate_domain_002_2.inputs[2])
					#reroute_017.Output -> vector_math_008_1.Vector
					curve_segment.links.new(reroute_017.outputs[0], vector_math_008_1.inputs[0])
					#reroute_015.Output -> vector_math_009_1.Vector
					curve_segment.links.new(reroute_015.outputs[0], vector_math_009_1.inputs[0])
					#reroute_017.Output -> field_at_index_001.Value
					curve_segment.links.new(reroute_017.outputs[0], field_at_index_001.inputs[3])
					#field_at_index_001.Value -> vector_math_008_1.Vector
					curve_segment.links.new(field_at_index_001.outputs[2], vector_math_008_1.inputs[1])
					#position_002_3.Position -> reroute_017.Input
					curve_segment.links.new(position_002_3.outputs[0], reroute_017.inputs[0])
					#interpolate_domain_002_2.Value -> reroute_015.Input
					curve_segment.links.new(interpolate_domain_002_2.outputs[2], reroute_015.inputs[0])
					#switch_004.Output -> group_output_5.Segment Direction
					curve_segment.links.new(switch_004.outputs[3], group_output_5.inputs[1])
					#switch_005.Output -> group_output_5.Neighbor Index
					curve_segment.links.new(switch_005.outputs[1], group_output_5.inputs[2])
					#boolean.Boolean -> interpolate_domain_2.Value
					curve_segment.links.new(boolean.outputs[0], interpolate_domain_2.inputs[4])
					#reroute_018.Output -> interpolate_domain_003.Value
					curve_segment.links.new(reroute_018.outputs[0], interpolate_domain_003.inputs[1])
					#vector_math_007_1.Value -> switch_003.True
					curve_segment.links.new(vector_math_007_1.outputs[1], switch_003.inputs[3])
					#reroute_1.Output -> switch_003.Switch
					curve_segment.links.new(reroute_1.outputs[0], switch_003.inputs[0])
					#switch_003.Output -> group_output_5.Segment Length
					curve_segment.links.new(switch_003.outputs[0], group_output_5.inputs[0])
					#vector_math_009_1.Vector -> switch_004.True
					curve_segment.links.new(vector_math_009_1.outputs[0], switch_004.inputs[9])
					#interpolate_domain_2.Value -> reroute_1.Input
					curve_segment.links.new(interpolate_domain_2.outputs[4], reroute_1.inputs[0])
					#reroute_1.Output -> switch_004.Switch
					curve_segment.links.new(reroute_1.outputs[0], switch_004.inputs[0])
					#interpolate_domain_003.Value -> switch_005.True
					curve_segment.links.new(interpolate_domain_003.outputs[1], switch_005.inputs[5])
					#reroute_1.Output -> switch_005.Switch
					curve_segment.links.new(reroute_1.outputs[0], switch_005.inputs[0])
					#offset_point_in_curve.Is Valid Offset -> switch_001.Switch
					curve_segment.links.new(offset_point_in_curve.outputs[0], switch_001.inputs[0])
					#offset_point_in_curve.Point Index -> switch_001.True
					curve_segment.links.new(offset_point_in_curve.outputs[1], switch_001.inputs[5])
					#index_002.Index -> switch_001.False
					curve_segment.links.new(index_002.outputs[0], switch_001.inputs[4])
					#switch_001.Output -> reroute_018.Input
					curve_segment.links.new(switch_001.outputs[1], reroute_018.inputs[0])
					return curve_segment

				curve_segment = curve_segment_node_group()

				#node Group
				group_1 = redistribute_curve_points.nodes.new("GeometryNodeGroup")
				group_1.outputs[0].hide = True
				group_1.outputs[2].hide = True
				group_1.node_tree = bpy.data.node_groups["Curve Segment"]

				#node Curve Tangent
				curve_tangent_2 = redistribute_curve_points.nodes.new("GeometryNodeInputTangent")

				#node Boolean Math.001
				boolean_math_001 = redistribute_curve_points.nodes.new("FunctionNodeBooleanMath")
				boolean_math_001.operation = 'NOT'
				#Boolean_001
				boolean_math_001.inputs[1].default_value = False

				#node Math.003
				math_003_1 = redistribute_curve_points.nodes.new("ShaderNodeMath")
				math_003_1.operation = 'MULTIPLY'
				#Value_002
				math_003_1.inputs[2].default_value = 0.5

				#node Map Range
				map_range_1 = redistribute_curve_points.nodes.new("ShaderNodeMapRange")
				map_range_1.data_type = 'FLOAT'
				map_range_1.interpolation_type = 'SMOOTHSTEP'
				map_range_1.clamp = True
				map_range_1.inputs[1].hide = True
				map_range_1.inputs[2].hide = True
				map_range_1.inputs[3].hide = True
				map_range_1.inputs[4].hide = True
				map_range_1.inputs[5].hide = True
				map_range_1.inputs[6].hide = True
				map_range_1.inputs[7].hide = True
				map_range_1.inputs[8].hide = True
				map_range_1.inputs[9].hide = True
				map_range_1.inputs[10].hide = True
				map_range_1.inputs[11].hide = True
				map_range_1.outputs[1].hide = True
				#From Min
				map_range_1.inputs[1].default_value = 0.0
				#From Max
				map_range_1.inputs[2].default_value = 1.0
				#To Min
				map_range_1.inputs[3].default_value = 0.0
				#To Max
				map_range_1.inputs[4].default_value = 1.0
				#Steps
				map_range_1.inputs[5].default_value = 4.0
				#Vector
				map_range_1.inputs[6].default_value = (0.0, 0.0, 0.0)
				#From_Min_FLOAT3
				map_range_1.inputs[7].default_value = (0.0, 0.0, 0.0)
				#From_Max_FLOAT3
				map_range_1.inputs[8].default_value = (1.0, 1.0, 1.0)
				#To_Min_FLOAT3
				map_range_1.inputs[9].default_value = (0.0, 0.0, 0.0)
				#To_Max_FLOAT3
				map_range_1.inputs[10].default_value = (1.0, 1.0, 1.0)
				#Steps_FLOAT3
				map_range_1.inputs[11].default_value = (4.0, 4.0, 4.0)

				#node Math
				math_1 = redistribute_curve_points.nodes.new("ShaderNodeMath")
				math_1.operation = 'ABSOLUTE'
				#Value_001
				math_1.inputs[1].default_value = 0.5
				#Value_002
				math_1.inputs[2].default_value = 0.5

				#node Vector Math
				vector_math_2 = redistribute_curve_points.nodes.new("ShaderNodeVectorMath")
				vector_math_2.operation = 'DOT_PRODUCT'
				#Vector_002
				vector_math_2.inputs[2].default_value = (0.0, 0.0, 0.0)
				#Scale
				vector_math_2.inputs[3].default_value = 1.0

				#node Endpoint Selection
				endpoint_selection_3 = redistribute_curve_points.nodes.new("GeometryNodeCurveEndpointSelection")
				#Start Size
				endpoint_selection_3.inputs[0].default_value = 1
				#End Size
				endpoint_selection_3.inputs[1].default_value = 1

				#node Group Input.003
				group_input_003 = redistribute_curve_points.nodes.new("NodeGroupInput")
				group_input_003.outputs[0].hide = True
				group_input_003.outputs[2].hide = True
				group_input_003.outputs[3].hide = True

				#node Boolean Math
				boolean_math = redistribute_curve_points.nodes.new("FunctionNodeBooleanMath")
				boolean_math.operation = 'NOT'
				#Boolean_001
				boolean_math.inputs[1].default_value = False

				#node Boolean Math.002
				boolean_math_002 = redistribute_curve_points.nodes.new("FunctionNodeBooleanMath")
				boolean_math_002.operation = 'AND'

				#node Compare
				compare_1 = redistribute_curve_points.nodes.new("FunctionNodeCompare")
				compare_1.data_type = 'FLOAT'
				compare_1.operation = 'GREATER_THAN'
				compare_1.mode = 'ELEMENT'
				#B
				compare_1.inputs[1].default_value = 0.0
				#A_INT
				compare_1.inputs[2].default_value = 0
				#B_INT
				compare_1.inputs[3].default_value = 0
				#A_VEC3
				compare_1.inputs[4].default_value = (0.0, 0.0, 0.0)
				#B_VEC3
				compare_1.inputs[5].default_value = (0.0, 0.0, 0.0)
				#A_COL
				compare_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
				#B_COL
				compare_1.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
				#A_STR
				compare_1.inputs[8].default_value = ""
				#B_STR
				compare_1.inputs[9].default_value = ""
				#C
				compare_1.inputs[10].default_value = 0.8999999761581421
				#Angle
				compare_1.inputs[11].default_value = 0.08726649731397629
				#Epsilon
				compare_1.inputs[12].default_value = 0.0010000000474974513

				#node Group.001
				group_001_1 = redistribute_curve_points.nodes.new("GeometryNodeGroup")
				group_001_1.outputs[1].hide = True
				group_001_1.outputs[2].hide = True
				group_001_1.outputs[3].hide = True
				group_001_1.outputs[4].hide = True
				group_001_1.outputs[5].hide = True
				group_001_1.node_tree = bpy.data.node_groups["Curve Info"]

				#Set parents
				blur_attribute.parent = frame_1
				spline_parameter_001.parent = frame_1
				spline_parameter_1.parent = frame_003_1
				group_input_002.parent = frame_003_1
				group_input_001.parent = frame_003_1
				set_position_002_1.parent = frame_002_1
				reroute_002.parent = frame_002_1
				sample_curve_001.parent = frame_002_1
				mix_001.parent = frame_003_1
				switch.parent = frame_003_1
				spline_parameter_002.parent = frame_004
				math_002_1.parent = frame_004
				group_002_1.parent = frame_004
				points_of_curve_2.parent = frame_004
				math_001_1.parent = frame_004
				endpoint_selection_001.parent = frame_1
				group_1.parent = frame_1
				curve_tangent_2.parent = frame_1
				boolean_math_001.parent = frame_1
				math_003_1.parent = frame_1
				map_range_1.parent = frame_1
				math_1.parent = frame_1
				vector_math_2.parent = frame_1
				endpoint_selection_3.parent = frame_001_1
				group_input_003.parent = frame_001_1
				boolean_math.parent = frame_001_1
				boolean_math_002.parent = frame_001_1
				compare_1.parent = frame_001_1
				group_001_1.parent = frame_002_1

				#Set locations
				frame_1.location = (-1090.3953857421875, -1376.604736328125)
				frame_004.location = (-1542.64697265625, -534.53271484375)
				frame_003_1.location = (-1622.947998046875, -341.8126220703125)
				frame_002_1.location = (-1622.757568359375, -341.7691650390625)
				frame_001_1.location = (-1681.17822265625, -253.91152954101562)
				group_input_1.location = (-929.6511840820312, 50.0)
				blur_attribute.location = (-401.8604736328125, 783.6279296875)
				spline_parameter_001.location = (-602.7907104492188, 743.44189453125)
				spline_parameter_1.location = (522.4186401367188, 80.3720932006836)
				group_input_002.location = (522.4186401367188, 160.7441864013672)
				group_input_001.location = (281.3023376464844, 20.0930233001709)
				set_position_002_1.location = (1486.8837890625, 401.8604736328125)
				reroute_002.location = (1105.1163330078125, 341.5813903808594)
				group_output_1.location = (75.0, 50.0)
				sample_curve_001.location = (1275.8043212890625, 311.39703369140625)
				mix_001.location = (743.44189453125, 160.7441864013672)
				switch.location = (522.4186401367188, 0.0)
				spline_parameter_002.location = (-230.91111755371094, 202.76522827148438)
				math_002_1.location = (-230.91111755371094, 122.39313507080078)
				group_002_1.location = (-592.5855712890625, 122.39313507080078)
				points_of_curve_2.location = (-411.7483215332031, 142.4861602783203)
				math_001_1.location = (-34.19317626953125, 213.08636474609375)
				endpoint_selection_001.location = (-964.4651489257812, 663.06982421875)
				group_1.location = (-1326.1396484375, 442.04656982421875)
				curve_tangent_2.location = (-1326.1396484375, 522.4186401367188)
				boolean_math_001.location = (-783.6279296875, 663.06982421875)
				math_003_1.location = (-602.7907104492188, 663.06982421875)
				map_range_1.location = (-783.6279296875, 542.51171875)
				math_1.location = (-964.4651489257812, 542.51171875)
				vector_math_2.location = (-1145.3023681640625, 542.51171875)
				endpoint_selection_3.location = (842.119384765625, 591.204833984375)
				group_input_003.location = (844.0751342773438, 472.60711669921875)
				boolean_math.location = (1032.82958984375, 605.3068237304688)
				boolean_math_002.location = (1213.666748046875, 585.2138061523438)
				compare_1.location = (1032.82958984375, 504.84173583984375)
				group_001_1.location = (1060.93115234375, 170.603271484375)

				#Set dimensions
				frame_1.width, frame_1.height = 1122.666748046875, 444.0
				frame_004.width, frame_004.height = 756.6666259765625, 212.5
				frame_003_1.width, frame_003_1.height = 660.0000610351562, 334.66668701171875
				frame_002_1.width, frame_002_1.height = 624.0, 343.83331298828125
				frame_001_1.width, frame_001_1.height = 569.9999389648438, 264.5
				group_input_1.width, group_input_1.height = 140.0, 100.0
				blur_attribute.width, blur_attribute.height = 140.0, 100.0
				spline_parameter_001.width, spline_parameter_001.height = 140.0, 100.0
				spline_parameter_1.width, spline_parameter_1.height = 140.0, 100.0
				group_input_002.width, group_input_002.height = 140.0, 100.0
				group_input_001.width, group_input_001.height = 140.0, 100.0
				set_position_002_1.width, set_position_002_1.height = 140.0, 100.0
				reroute_002.width, reroute_002.height = 16.0, 100.0
				group_output_1.width, group_output_1.height = 140.0, 100.0
				sample_curve_001.width, sample_curve_001.height = 140.0, 100.0
				mix_001.width, mix_001.height = 140.0, 100.0
				switch.width, switch.height = 140.0, 100.0
				spline_parameter_002.width, spline_parameter_002.height = 140.0, 100.0
				math_002_1.width, math_002_1.height = 140.0, 100.0
				group_002_1.width, group_002_1.height = 140.0, 100.0
				points_of_curve_2.width, points_of_curve_2.height = 140.0, 100.0
				math_001_1.width, math_001_1.height = 140.0, 100.0
				endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
				group_1.width, group_1.height = 140.0, 100.0
				curve_tangent_2.width, curve_tangent_2.height = 140.0, 100.0
				boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
				math_003_1.width, math_003_1.height = 140.0, 100.0
				map_range_1.width, map_range_1.height = 140.0, 100.0
				math_1.width, math_1.height = 140.0, 100.0
				vector_math_2.width, vector_math_2.height = 140.0, 100.0
				endpoint_selection_3.width, endpoint_selection_3.height = 140.0, 100.0
				group_input_003.width, group_input_003.height = 140.0, 100.0
				boolean_math.width, boolean_math.height = 140.0, 100.0
				boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
				compare_1.width, compare_1.height = 140.0, 100.0
				group_001_1.width, group_001_1.height = 140.0, 100.0

				#initialize redistribute_curve_points links
				#group_input_1.Curves -> reroute_002.Input
				redistribute_curve_points.links.new(group_input_1.outputs[0], reroute_002.inputs[0])
				#reroute_002.Output -> sample_curve_001.Curves
				redistribute_curve_points.links.new(reroute_002.outputs[0], sample_curve_001.inputs[0])
				#reroute_002.Output -> set_position_002_1.Geometry
				redistribute_curve_points.links.new(reroute_002.outputs[0], set_position_002_1.inputs[0])
				#math_002_1.Value -> math_001_1.Value
				redistribute_curve_points.links.new(math_002_1.outputs[0], math_001_1.inputs[1])
				#spline_parameter_002.Index -> math_001_1.Value
				redistribute_curve_points.links.new(spline_parameter_002.outputs[2], math_001_1.inputs[0])
				#points_of_curve_2.Total -> math_002_1.Value
				redistribute_curve_points.links.new(points_of_curve_2.outputs[1], math_002_1.inputs[0])
				#sample_curve_001.Position -> set_position_002_1.Position
				redistribute_curve_points.links.new(sample_curve_001.outputs[5], set_position_002_1.inputs[2])
				#set_position_002_1.Geometry -> group_output_1.Curves
				redistribute_curve_points.links.new(set_position_002_1.outputs[0], group_output_1.inputs[0])
				#endpoint_selection_3.Selection -> boolean_math.Boolean
				redistribute_curve_points.links.new(endpoint_selection_3.outputs[0], boolean_math.inputs[0])
				#spline_parameter_001.Factor -> blur_attribute.Value
				redistribute_curve_points.links.new(spline_parameter_001.outputs[0], blur_attribute.inputs[0])
				#endpoint_selection_001.Selection -> boolean_math_001.Boolean
				redistribute_curve_points.links.new(endpoint_selection_001.outputs[0], boolean_math_001.inputs[0])
				#math_003_1.Value -> blur_attribute.Weight
				redistribute_curve_points.links.new(math_003_1.outputs[0], blur_attribute.inputs[5])
				#mix_001.Result -> sample_curve_001.Factor
				redistribute_curve_points.links.new(mix_001.outputs[0], sample_curve_001.inputs[6])
				#curve_tangent_2.Tangent -> vector_math_2.Vector
				redistribute_curve_points.links.new(curve_tangent_2.outputs[0], vector_math_2.inputs[0])
				#group_1.Segment Direction -> vector_math_2.Vector
				redistribute_curve_points.links.new(group_1.outputs[1], vector_math_2.inputs[1])
				#vector_math_2.Value -> math_1.Value
				redistribute_curve_points.links.new(vector_math_2.outputs[1], math_1.inputs[0])
				#math_1.Value -> map_range_1.Value
				redistribute_curve_points.links.new(math_1.outputs[0], map_range_1.inputs[0])
				#boolean_math_001.Boolean -> math_003_1.Value
				redistribute_curve_points.links.new(boolean_math_001.outputs[0], math_003_1.inputs[0])
				#map_range_1.Result -> math_003_1.Value
				redistribute_curve_points.links.new(map_range_1.outputs[0], math_003_1.inputs[1])
				#group_input_002.Factor -> mix_001.Factor
				redistribute_curve_points.links.new(group_input_002.outputs[1], mix_001.inputs[0])
				#spline_parameter_1.Factor -> mix_001.A
				redistribute_curve_points.links.new(spline_parameter_1.outputs[0], mix_001.inputs[2])
				#switch.Output -> mix_001.B
				redistribute_curve_points.links.new(switch.outputs[0], mix_001.inputs[3])
				#math_001_1.Value -> switch.False
				redistribute_curve_points.links.new(math_001_1.outputs[0], switch.inputs[2])
				#group_input_001.Feature Awareness -> switch.Switch
				redistribute_curve_points.links.new(group_input_001.outputs[2], switch.inputs[0])
				#blur_attribute.Value -> switch.True
				redistribute_curve_points.links.new(blur_attribute.outputs[0], switch.inputs[3])
				#boolean_math.Boolean -> boolean_math_002.Boolean
				redistribute_curve_points.links.new(boolean_math.outputs[0], boolean_math_002.inputs[0])
				#boolean_math_002.Boolean -> set_position_002_1.Selection
				redistribute_curve_points.links.new(boolean_math_002.outputs[0], set_position_002_1.inputs[1])
				#compare_1.Result -> boolean_math_002.Boolean
				redistribute_curve_points.links.new(compare_1.outputs[0], boolean_math_002.inputs[1])
				#group_input_003.Factor -> compare_1.A
				redistribute_curve_points.links.new(group_input_003.outputs[1], compare_1.inputs[0])
				#group_001_1.Curve Index -> sample_curve_001.Curve Index
				redistribute_curve_points.links.new(group_001_1.outputs[0], sample_curve_001.inputs[8])
				#group_002_1.Curve Index -> points_of_curve_2.Curve Index
				redistribute_curve_points.links.new(group_002_1.outputs[0], points_of_curve_2.inputs[0])
				return redistribute_curve_points

			redistribute_curve_points = redistribute_curve_points_node_group()

			#node Group
			group_2 = geometry_nodes_001.nodes.new("GeometryNodeGroup")
			group_2.node_tree = bpy.data.node_groups["Redistribute Curve Points"]
			#Input_2
			group_2.inputs[1].default_value = 1.0
			#Input_3
			group_2.inputs[2].default_value = False

			#node Curve Circle
			curve_circle = geometry_nodes_001.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.mode = 'RADIUS'
			#Resolution
			curve_circle.inputs[0].default_value = 32
			#Point 1
			curve_circle.inputs[1].default_value = (-1.0, 0.0, 0.0)
			#Point 2
			curve_circle.inputs[2].default_value = (0.0, 1.0, 0.0)
			#Point 3
			curve_circle.inputs[3].default_value = (1.0, 0.0, 0.0)
			#Radius
			curve_circle.inputs[4].default_value = 0.05000000074505806

			#node Trim Curve
			trim_curve = geometry_nodes_001.nodes.new("GeometryNodeTrimCurve")
			trim_curve.mode = 'LENGTH'
			#Selection
			trim_curve.inputs[1].default_value = True
			#Start
			trim_curve.inputs[2].default_value = 0.0
			#End
			trim_curve.inputs[3].default_value = 1.0
			#Start_001
			trim_curve.inputs[4].default_value = 0.0
			#End_001
			trim_curve.inputs[5].default_value = 3.0

			#node Curve to Mesh
			curve_to_mesh = geometry_nodes_001.nodes.new("GeometryNodeCurveToMesh")
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = False

			#node Instance on Points
			instance_on_points = geometry_nodes_001.nodes.new("GeometryNodeInstanceOnPoints")
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

			#node Capture Attribute
			capture_attribute = geometry_nodes_001.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.data_type = 'FLOAT_VECTOR'
			capture_attribute.domain = 'POINT'
			#Value_001
			capture_attribute.inputs[2].default_value = 0.0
			#Value_002
			capture_attribute.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_003
			capture_attribute.inputs[4].default_value = False
			#Value_004
			capture_attribute.inputs[5].default_value = 0

			#node Position.001
			position_001 = geometry_nodes_001.nodes.new("GeometryNodeInputPosition")

			#node Evaluate at Index
			evaluate_at_index_1 = geometry_nodes_001.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			#Index
			evaluate_at_index_1.inputs[0].default_value = 49
			#Value_Float
			evaluate_at_index_1.inputs[1].default_value = 0.0
			#Value_Int
			evaluate_at_index_1.inputs[2].default_value = 0
			#Value_Color
			evaluate_at_index_1.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			evaluate_at_index_1.inputs[5].default_value = False

			#node Evaluate at Index.001
			evaluate_at_index_001_1 = geometry_nodes_001.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_1.domain = 'POINT'
			#Index
			evaluate_at_index_001_1.inputs[0].default_value = 48
			#Value_Float
			evaluate_at_index_001_1.inputs[1].default_value = 0.0
			#Value_Int
			evaluate_at_index_001_1.inputs[2].default_value = 0
			#Value_Color
			evaluate_at_index_001_1.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
			#Value_Bool
			evaluate_at_index_001_1.inputs[5].default_value = False

			#node Vector Math.003
			vector_math_003 = geometry_nodes_001.nodes.new("ShaderNodeVectorMath")
			vector_math_003.operation = 'SUBTRACT'
			#Vector_002
			vector_math_003.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			vector_math_003.inputs[3].default_value = 1.0

			#node Align Euler to Vector
			align_euler_to_vector = geometry_nodes_001.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0

			#node Named Attribute.001
			named_attribute_001 = geometry_nodes_001.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "pos"

			#node Transform Geometry
			transform_geometry = geometry_nodes_001.nodes.new("GeometryNodeTransform")
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (0.10499999672174454, 0.07400000095367432, 0.050999999046325684)

			#node UV Sphere
			uv_sphere = geometry_nodes_001.nodes.new("GeometryNodeMeshUVSphere")
			#Segments
			uv_sphere.inputs[0].default_value = 32
			#Rings
			uv_sphere.inputs[1].default_value = 16
			#Radius
			uv_sphere.inputs[2].default_value = 1.0

			#node Color Ramp
			color_ramp = geometry_nodes_001.nodes.new("ShaderNodeValToRGB")
			color_ramp.color_ramp.color_mode = 'RGB'
			color_ramp.color_ramp.hue_interpolation = 'NEAR'
			color_ramp.color_ramp.interpolation = 'LINEAR'

			color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
			color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
			color_ramp_cre_0.position = 0.0
			color_ramp_cre_0.alpha = 1.0
			color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

			color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
			color_ramp_cre_1.alpha = 1.0
			color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)


			#node Material Selection
			material_selection = geometry_nodes_001.nodes.new("GeometryNodeMaterialSelection")
			if "Material.001" in bpy.data.materials:
				material_selection.inputs[0].default_value = bpy.data.materials["Material.001"]

			#node Rotate Instances
			rotate_instances = geometry_nodes_001.nodes.new("GeometryNodeRotateInstances")
			#Pivot Point
			rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Local Space
			rotate_instances.inputs[4].default_value = True

			simulation_input.pair_with_output(simulation_output)
			#Pivot Point
			rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Local Space
			rotate_instances.inputs[4].default_value = True

			simulation_input_001.pair_with_output(simulation_output_001)
			#Pivot Point
			rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Local Space
			rotate_instances.inputs[4].default_value = True

			#Set parents
			rgb_curves.parent = frame
			spline_parameter.parent = frame
			math_003.parent = frame
			combine_xyz_002.parent = frame
			separate_xyz.parent = frame
			math.parent = frame
			position.parent = frame
			combine_xyz_001.parent = frame
			curve_line.parent = frame
			resample_curve.parent = frame
			simulation_input.parent = frame
			scene_time.parent = frame
			compare_001.parent = frame
			compare.parent = frame
			math_002.parent = frame
			named_attribute.parent = frame
			vector_math.parent = frame
			store_named_attribute_001.parent = frame
			vector_math_001.parent = frame
			store_named_attribute.parent = frame
			set_position_001.parent = frame
			simulation_output.parent = frame
			transform_geometry_002.parent = frame_002
			points.parent = frame_002
			random_value.parent = frame_002
			random_value_001.parent = frame_002
			curve_line_001.parent = frame_002
			instance_on_points_001.parent = frame_002
			translate_instances.parent = frame_002
			join_geometry.parent = frame_002
			vector_math_005.parent = frame_002
			transform_geometry_001.parent = frame_002
			vector_math_004.parent = frame_002
			uv_sphere_001.parent = frame_002
			noise_texture.parent = frame_002
			curve_circle_001.parent = frame_002
			set_position.parent = frame_002
			curve_to_mesh_001.parent = frame_002
			join_geometry_001.parent = frame_002
			realize_instances.parent = frame_002
			transform_geometry_003.parent = frame_002
			realize_instances_001.parent = frame_003
			store_named_attribute_002.parent = frame_003
			distribute_points_on_faces.parent = frame_003
			index.parent = frame_003
			store_named_attribute_003.parent = frame_003
			set_point_radius.parent = frame_003
			store_named_attribute_004.parent = frame_003
			position_003.parent = frame_003
			position_002.parent = frame_003
			sample_index.parent = frame_003
			simulation_input_001.parent = frame_003
			random_value_003.parent = frame_003
			set_position_002.parent = frame_003
			math_004.parent = frame_003
			set_position_003.parent = frame_003
			random_value_002.parent = frame_003
			compare_002.parent = frame_003
			simulation_output_001.parent = frame_003
			named_attribute_002.parent = frame_003
			named_attribute_003.parent = frame_003
			store_named_attribute_005.parent = frame_003
			math_001.parent = frame_003
			random_value_004.parent = frame_003
			separate_xyz_001.parent = frame_003
			vector_math_006.parent = frame_003
			vector_math_009.parent = frame_003
			instance_on_points_002.parent = frame_003
			random_value_007.parent = frame_003
			set_position_004.parent = frame_003
			random_value_005.parent = frame_003
			math_005.parent = frame_003
			map_range.parent = frame_003
			join_geometry_002.parent = frame_003
			named_attribute_004.parent = frame_003
			math_006.parent = frame_003
			random_value_006.parent = frame_003
			scene_time_001.parent = frame_003
			vector_math_007.parent = frame_003
			vector_math_008.parent = frame_003
			math_007.parent = frame_003
			vector_math_002.parent = frame
			endpoint_selection.parent = frame_001
			group_2.parent = frame_001
			curve_circle.parent = frame_001
			trim_curve.parent = frame_001
			curve_to_mesh.parent = frame_001
			instance_on_points.parent = frame_001
			capture_attribute.parent = frame_001
			position_001.parent = frame_001
			evaluate_at_index_1.parent = frame_001
			evaluate_at_index_001_1.parent = frame_001
			vector_math_003.parent = frame_001
			align_euler_to_vector.parent = frame_001
			named_attribute_001.parent = frame_003
			transform_geometry.parent = frame_001
			uv_sphere.parent = frame_001
			rotate_instances.parent = frame_003

			#Set locations
			frame.location = (0.0, 0.0)
			frame_002.location = (-1929.8265380859375, -1695.379150390625)
			frame_003.location = (207.721435546875, -67.03167724609375)
			frame_001.location = (160.030029296875, -162.61773681640625)
			group_input.location = (-9.179261207580566, 553.5494995117188)
			rgb_curves.location = (562.5985717773438, 919.0752563476562)
			spline_parameter.location = (403.492431640625, 914.0485229492188)
			math_003.location = (820.427978515625, 917.2951049804688)
			combine_xyz_002.location = (978.8331909179688, 913.8880004882812)
			separate_xyz.location = (469.1748962402344, 592.1019897460938)
			math.location = (642.3269653320312, 585.4978637695312)
			position.location = (308.5922546386719, 594.6189575195312)
			combine_xyz_001.location = (802.489990234375, 585.1517333984375)
			curve_line.location = (619.9505615234375, 415.4534606933594)
			resample_curve.location = (786.505615234375, 410.9842529296875)
			simulation_input.location = (960.47607421875, 411.6775817871094)
			scene_time.location = (1038.4346923828125, 690.9902954101562)
			compare_001.location = (1234.59130859375, 832.103515625)
			compare.location = (1235.2298583984375, 671.0863037109375)
			math_002.location = (1412.8681640625, 761.7216186523438)
			named_attribute.location = (1074.4830322265625, 242.11695861816406)
			vector_math.location = (1487.0057373046875, 386.60888671875)
			store_named_attribute_001.location = (1670.64453125, 620.0098876953125)
			vector_math_001.location = (1654.4990234375, 392.2271728515625)
			store_named_attribute.location = (1839.5830078125, 616.7182006835938)
			set_position_001.location = (2003.6351318359375, 618.562744140625)
			simulation_output.location = (2164.583740234375, 617.6746826171875)
			group_output.location = (7721.48388671875, 630.1264038085938)
			transform_geometry_002.location = (4031.538330078125, 1229.0740966796875)
			points.location = (3861.342529296875, 1411.7318115234375)
			random_value.location = (4032.301025390625, 1525.0078125)
			random_value_001.location = (4033.69921875, 1707.3994140625)
			curve_line_001.location = (3859.985595703125, 1223.0955810546875)
			instance_on_points_001.location = (4221.14013671875, 1427.5419921875)
			translate_instances.location = (4380.41357421875, 1424.7889404296875)
			join_geometry.location = (4547.21240234375, 1202.572021484375)
			vector_math_005.location = (4384.41162109375, 695.89306640625)
			transform_geometry_001.location = (4384.513671875, 1028.18505859375)
			vector_math_004.location = (4228.06640625, 697.93896484375)
			uv_sphere_001.location = (4218.17724609375, 1026.4007568359375)
			noise_texture.location = (4069.699462890625, 699.6007690429688)
			curve_circle_001.location = (4547.30419921875, 1160.5030517578125)
			set_position.location = (4546.64990234375, 1027.2611083984375)
			curve_to_mesh_001.location = (4724.14892578125, 1193.37841796875)
			join_geometry_001.location = (4882.6630859375, 1189.180419921875)
			realize_instances.location = (4885.1494140625, 1152.128173828125)
			transform_geometry_003.location = (5045.2255859375, 1128.267578125)
			realize_instances_001.location = (3346.597412109375, 364.8573913574219)
			store_named_attribute_002.location = (3544.441650390625, 256.0726013183594)
			distribute_points_on_faces.location = (3350.126220703125, 272.425048828125)
			index.location = (3848.022705078125, 333.5399169921875)
			store_named_attribute_003.location = (3700.318603515625, 256.0726013183594)
			set_point_radius.location = (3858.569580078125, 247.1632843017578)
			store_named_attribute_004.location = (4031.177490234375, 219.2108612060547)
			position_003.location = (4028.557373046875, 20.33513832092285)
			position_002.location = (3848.718505859375, 389.9635925292969)
			sample_index.location = (4035.2529296875, 426.510498046875)
			simulation_input_001.location = (4228.98681640625, 295.7141418457031)
			random_value_003.location = (4414.14599609375, 744.437255859375)
			set_position_002.location = (4409.1982421875, 252.1443634033203)
			math_004.location = (4411.93505859375, 452.2938537597656)
			set_position_003.location = (4616.5458984375, 393.4349670410156)
			random_value_002.location = (3846.4423828125, 550.1259155273438)
			compare_002.location = (4012.206298828125, 661.3277587890625)
			simulation_output_001.location = (5017.73388671875, 394.107666015625)
			named_attribute_002.location = (5012.2138671875, 540.8441772460938)
			named_attribute_003.location = (5388.77490234375, 137.1885223388672)
			store_named_attribute_005.location = (4808.021484375, 414.2499084472656)
			math_001.location = (4182.28857421875, 628.9763793945312)
			random_value_004.location = (4794.75634765625, 114.27330780029297)
			separate_xyz_001.location = (3845.625244140625, 678.5164794921875)
			vector_math_006.location = (5209.728515625, 347.5942077636719)
			vector_math_009.location = (5402.7646484375, 312.87933349609375)
			instance_on_points_002.location = (5748.0283203125, 352.9821472167969)
			random_value_007.location = (5206.7353515625, 653.0548706054688)
			set_position_004.location = (5566.9345703125, 402.4853820800781)
			random_value_005.location = (5742.4501953125, 677.2108764648438)
			math_005.location = (5120.873046875, 111.13076782226562)
			map_range.location = (4963.7431640625, 110.49208068847656)
			join_geometry_002.location = (6642.818359375, 266.67041015625)
			named_attribute_004.location = (5388.6611328125, 669.8258056640625)
			math_006.location = (5569.5126953125, 665.1727294921875)
			random_value_006.location = (5606.3896484375, 904.4669799804688)
			scene_time_001.location = (5825.3876953125, 798.4075927734375)
			vector_math_007.location = (5985.4912109375, 604.2029418945312)
			vector_math_008.location = (6160.2734375, 602.8807983398438)
			math_007.location = (6054.7978515625, 808.5275268554688)
			vector_math_002.location = (1281.555419921875, 477.897216796875)
			endpoint_selection.location = (3090.129150390625, 721.2492065429688)
			group_2.location = (2594.26123046875, 750.1569213867188)
			curve_circle.location = (2592.83447265625, 624.2626342773438)
			trim_curve.location = (2439.082275390625, 749.8038940429688)
			curve_to_mesh.location = (2752.789306640625, 745.5303344726562)
			instance_on_points.location = (3083.401611328125, 606.3497924804688)
			capture_attribute.location = (2265.288818359375, 731.7088012695312)
			position_001.location = (2225.552978515625, 1080.819091796875)
			evaluate_at_index_1.location = (2385.400390625, 1095.013671875)
			evaluate_at_index_001_1.location = (2383.978759765625, 936.2144165039062)
			vector_math_003.location = (2550.744140625, 1036.363037109375)
			align_euler_to_vector.location = (2709.927978515625, 1043.439453125)
			named_attribute_001.location = (3688.0478515625, 681.4520874023438)
			transform_geometry.location = (2919.540283203125, 605.6742553710938)
			uv_sphere.location = (2759.693115234375, 606.5806274414062)
			color_ramp.location = (1393.59033203125, 11.13238525390625)
			material_selection.location = (1101.9635009765625, -2.5297648906707764)
			rotate_instances.location = (6453.1708984375, 459.6465148925781)

			#Set dimensions
			frame.width, frame.height = 2056.0, 864.0
			frame_002.width, frame_002.height = 1385.0, 1283.0
			frame_003.width, frame_003.height = 3496.999755859375, 1101.0
			frame_001.width, frame_001.height = 1064.0, 869.9999389648438
			group_input.width, group_input.height = 140.0, 100.0
			rgb_curves.width, rgb_curves.height = 240.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			combine_xyz_002.width, combine_xyz_002.height = 147.7833709716797, 100.0
			separate_xyz.width, separate_xyz.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			curve_line.width, curve_line.height = 140.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			simulation_input.width, simulation_input.height = 140.0, 100.0
			scene_time.width, scene_time.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			simulation_output.width, simulation_output.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			points.width, points.height = 140.0, 100.0
			random_value.width, random_value.height = 140.0, 100.0
			random_value_001.width, random_value_001.height = 140.0, 100.0
			curve_line_001.width, curve_line_001.height = 140.0, 100.0
			instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
			translate_instances.width, translate_instances.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			uv_sphere_001.width, uv_sphere_001.height = 140.0, 100.0
			noise_texture.width, noise_texture.height = 140.0, 100.0
			curve_circle_001.width, curve_circle_001.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
			realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			distribute_points_on_faces.width, distribute_points_on_faces.height = 170.0, 100.0
			index.width, index.height = 140.0, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
			set_point_radius.width, set_point_radius.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			position_003.width, position_003.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			simulation_input_001.width, simulation_input_001.height = 140.0, 100.0
			random_value_003.width, random_value_003.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			set_position_003.width, set_position_003.height = 140.0, 100.0
			random_value_002.width, random_value_002.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			simulation_output_001.width, simulation_output_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			random_value_004.width, random_value_004.height = 140.0, 100.0
			separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
			random_value_007.width, random_value_007.height = 140.0, 100.0
			set_position_004.width, set_position_004.height = 140.0, 100.0
			random_value_005.width, random_value_005.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			random_value_006.width, random_value_006.height = 140.0, 100.0
			scene_time_001.width, scene_time_001.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			trim_curve.width, trim_curve.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 127.65071105957031, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			uv_sphere.width, uv_sphere.height = 140.0, 100.0
			color_ramp.width, color_ramp.height = 240.0, 100.0
			material_selection.width, material_selection.height = 140.0, 100.0
			rotate_instances.width, rotate_instances.height = 140.0, 100.0

			#initialize geometry_nodes_001 links
			#curve_line.Curve -> resample_curve.Curve
			geometry_nodes_001.links.new(curve_line.outputs[0], resample_curve.inputs[0])
			#set_position_001.Geometry -> simulation_output.Geometry
			geometry_nodes_001.links.new(set_position_001.outputs[0], simulation_output.inputs[0])
			#store_named_attribute.Geometry -> set_position_001.Geometry
			geometry_nodes_001.links.new(store_named_attribute.outputs[0], set_position_001.inputs[0])
			#position.Position -> separate_xyz.Vector
			geometry_nodes_001.links.new(position.outputs[0], separate_xyz.inputs[0])
			#separate_xyz.X -> math.Value
			geometry_nodes_001.links.new(separate_xyz.outputs[0], math.inputs[0])
			#math.Value -> combine_xyz_001.X
			geometry_nodes_001.links.new(math.outputs[0], combine_xyz_001.inputs[0])
			#vector_math_001.Vector -> store_named_attribute.Value
			geometry_nodes_001.links.new(vector_math_001.outputs[0], store_named_attribute.inputs[3])
			#named_attribute.Attribute -> vector_math.Vector
			geometry_nodes_001.links.new(named_attribute.outputs[0], vector_math.inputs[0])
			#combine_xyz_001.Vector -> vector_math.Vector
			geometry_nodes_001.links.new(combine_xyz_001.outputs[0], vector_math.inputs[1])
			#named_attribute.Attribute -> set_position_001.Offset
			geometry_nodes_001.links.new(named_attribute.outputs[0], set_position_001.inputs[3])
			#vector_math.Vector -> vector_math_001.Vector
			geometry_nodes_001.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
			#resample_curve.Curve -> simulation_input.Geometry
			geometry_nodes_001.links.new(resample_curve.outputs[0], simulation_input.inputs[0])
			#math_003.Value -> combine_xyz_002.X
			geometry_nodes_001.links.new(math_003.outputs[0], combine_xyz_002.inputs[0])
			#named_attribute.Attribute -> vector_math_002.Vector
			geometry_nodes_001.links.new(named_attribute.outputs[0], vector_math_002.inputs[0])
			#store_named_attribute_001.Geometry -> store_named_attribute.Geometry
			geometry_nodes_001.links.new(store_named_attribute_001.outputs[0], store_named_attribute.inputs[0])
			#simulation_input.Geometry -> store_named_attribute_001.Geometry
			geometry_nodes_001.links.new(simulation_input.outputs[1], store_named_attribute_001.inputs[0])
			#vector_math_002.Vector -> store_named_attribute_001.Value
			geometry_nodes_001.links.new(vector_math_002.outputs[0], store_named_attribute_001.inputs[3])
			#scene_time.Frame -> compare.A
			geometry_nodes_001.links.new(scene_time.outputs[1], compare.inputs[0])
			#scene_time.Frame -> compare_001.A
			geometry_nodes_001.links.new(scene_time.outputs[1], compare_001.inputs[0])
			#compare_001.Result -> math_002.Value
			geometry_nodes_001.links.new(compare_001.outputs[0], math_002.inputs[0])
			#compare.Result -> math_002.Value
			geometry_nodes_001.links.new(compare.outputs[0], math_002.inputs[1])
			#math_002.Value -> store_named_attribute_001.Selection
			geometry_nodes_001.links.new(math_002.outputs[0], store_named_attribute_001.inputs[1])
			#spline_parameter.Factor -> rgb_curves.Color
			geometry_nodes_001.links.new(spline_parameter.outputs[0], rgb_curves.inputs[1])
			#rgb_curves.Color -> math_003.Value
			geometry_nodes_001.links.new(rgb_curves.outputs[0], math_003.inputs[0])
			#combine_xyz_002.Vector -> vector_math_002.Vector
			geometry_nodes_001.links.new(combine_xyz_002.outputs[0], vector_math_002.inputs[1])
			#capture_attribute.Geometry -> trim_curve.Curve
			geometry_nodes_001.links.new(capture_attribute.outputs[0], trim_curve.inputs[0])
			#trim_curve.Curve -> group_2.Curves
			geometry_nodes_001.links.new(trim_curve.outputs[0], group_2.inputs[0])
			#group_2.Curves -> curve_to_mesh.Curve
			geometry_nodes_001.links.new(group_2.outputs[0], curve_to_mesh.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			geometry_nodes_001.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#uv_sphere.Mesh -> transform_geometry.Geometry
			geometry_nodes_001.links.new(uv_sphere.outputs[0], transform_geometry.inputs[0])
			#group_2.Curves -> instance_on_points.Points
			geometry_nodes_001.links.new(group_2.outputs[0], instance_on_points.inputs[0])
			#transform_geometry.Geometry -> instance_on_points.Instance
			geometry_nodes_001.links.new(transform_geometry.outputs[0], instance_on_points.inputs[2])
			#endpoint_selection.Selection -> instance_on_points.Selection
			geometry_nodes_001.links.new(endpoint_selection.outputs[0], instance_on_points.inputs[1])
			#evaluate_at_index_1.Value -> vector_math_003.Vector
			geometry_nodes_001.links.new(evaluate_at_index_1.outputs[2], vector_math_003.inputs[0])
			#evaluate_at_index_001_1.Value -> vector_math_003.Vector
			geometry_nodes_001.links.new(evaluate_at_index_001_1.outputs[2], vector_math_003.inputs[1])
			#vector_math_003.Vector -> align_euler_to_vector.Vector
			geometry_nodes_001.links.new(vector_math_003.outputs[0], align_euler_to_vector.inputs[2])
			#position_001.Position -> evaluate_at_index_1.Value
			geometry_nodes_001.links.new(position_001.outputs[0], evaluate_at_index_1.inputs[3])
			#position_001.Position -> evaluate_at_index_001_1.Value
			geometry_nodes_001.links.new(position_001.outputs[0], evaluate_at_index_001_1.inputs[3])
			#uv_sphere_001.Mesh -> transform_geometry_001.Geometry
			geometry_nodes_001.links.new(uv_sphere_001.outputs[0], transform_geometry_001.inputs[0])
			#transform_geometry_001.Geometry -> set_position.Geometry
			geometry_nodes_001.links.new(transform_geometry_001.outputs[0], set_position.inputs[0])
			#vector_math_005.Vector -> set_position.Offset
			geometry_nodes_001.links.new(vector_math_005.outputs[0], set_position.inputs[3])
			#noise_texture.Color -> vector_math_004.Vector
			geometry_nodes_001.links.new(noise_texture.outputs[1], vector_math_004.inputs[0])
			#vector_math_004.Vector -> vector_math_005.Vector
			geometry_nodes_001.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
			#transform_geometry_002.Geometry -> instance_on_points_001.Instance
			geometry_nodes_001.links.new(transform_geometry_002.outputs[0], instance_on_points_001.inputs[2])
			#points.Geometry -> instance_on_points_001.Points
			geometry_nodes_001.links.new(points.outputs[0], instance_on_points_001.inputs[0])
			#curve_line_001.Curve -> transform_geometry_002.Geometry
			geometry_nodes_001.links.new(curve_line_001.outputs[0], transform_geometry_002.inputs[0])
			#random_value.Value -> instance_on_points_001.Rotation
			geometry_nodes_001.links.new(random_value.outputs[0], instance_on_points_001.inputs[5])
			#random_value_001.Value -> instance_on_points_001.Scale
			geometry_nodes_001.links.new(random_value_001.outputs[1], instance_on_points_001.inputs[6])
			#instance_on_points_001.Instances -> translate_instances.Instances
			geometry_nodes_001.links.new(instance_on_points_001.outputs[0], translate_instances.inputs[0])
			#translate_instances.Instances -> join_geometry.Geometry
			geometry_nodes_001.links.new(translate_instances.outputs[0], join_geometry.inputs[0])
			#curve_line_001.Curve -> join_geometry.Geometry
			geometry_nodes_001.links.new(curve_line_001.outputs[0], join_geometry.inputs[0])
			#join_geometry.Geometry -> curve_to_mesh_001.Curve
			geometry_nodes_001.links.new(join_geometry.outputs[0], curve_to_mesh_001.inputs[0])
			#curve_circle_001.Curve -> curve_to_mesh_001.Profile Curve
			geometry_nodes_001.links.new(curve_circle_001.outputs[0], curve_to_mesh_001.inputs[1])
			#curve_to_mesh_001.Mesh -> join_geometry_001.Geometry
			geometry_nodes_001.links.new(curve_to_mesh_001.outputs[0], join_geometry_001.inputs[0])
			#set_position.Geometry -> join_geometry_001.Geometry
			geometry_nodes_001.links.new(set_position.outputs[0], join_geometry_001.inputs[0])
			#realize_instances.Geometry -> transform_geometry_003.Geometry
			geometry_nodes_001.links.new(realize_instances.outputs[0], transform_geometry_003.inputs[0])
			#join_geometry_001.Geometry -> realize_instances.Geometry
			geometry_nodes_001.links.new(join_geometry_001.outputs[0], realize_instances.inputs[0])
			#instance_on_points.Instances -> realize_instances_001.Geometry
			geometry_nodes_001.links.new(instance_on_points.outputs[0], realize_instances_001.inputs[0])
			#realize_instances_001.Geometry -> distribute_points_on_faces.Mesh
			geometry_nodes_001.links.new(realize_instances_001.outputs[0], distribute_points_on_faces.inputs[0])
			#distribute_points_on_faces.Points -> store_named_attribute_002.Geometry
			geometry_nodes_001.links.new(distribute_points_on_faces.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
			geometry_nodes_001.links.new(store_named_attribute_002.outputs[0], store_named_attribute_003.inputs[0])
			#distribute_points_on_faces.Normal -> store_named_attribute_003.Value
			geometry_nodes_001.links.new(distribute_points_on_faces.outputs[1], store_named_attribute_003.inputs[4])
			#distribute_points_on_faces.Rotation -> store_named_attribute_002.Value
			geometry_nodes_001.links.new(distribute_points_on_faces.outputs[2], store_named_attribute_002.inputs[4])
			#distribute_points_on_faces.Rotation -> store_named_attribute_002.Value
			geometry_nodes_001.links.new(distribute_points_on_faces.outputs[2], store_named_attribute_002.inputs[3])
			#distribute_points_on_faces.Normal -> store_named_attribute_003.Value
			geometry_nodes_001.links.new(distribute_points_on_faces.outputs[1], store_named_attribute_003.inputs[3])
			#store_named_attribute_003.Geometry -> set_point_radius.Points
			geometry_nodes_001.links.new(store_named_attribute_003.outputs[0], set_point_radius.inputs[0])
			#set_point_radius.Points -> store_named_attribute_004.Geometry
			geometry_nodes_001.links.new(set_point_radius.outputs[0], store_named_attribute_004.inputs[0])
			#set_point_radius.Points -> sample_index.Geometry
			geometry_nodes_001.links.new(set_point_radius.outputs[0], sample_index.inputs[0])
			#position_003.Position -> store_named_attribute_004.Value
			geometry_nodes_001.links.new(position_003.outputs[0], store_named_attribute_004.inputs[3])
			#index.Index -> sample_index.Index
			geometry_nodes_001.links.new(index.outputs[0], sample_index.inputs[6])
			#position_002.Position -> sample_index.Value
			geometry_nodes_001.links.new(position_002.outputs[0], sample_index.inputs[3])
			#named_attribute_001.Attribute -> separate_xyz_001.Vector
			geometry_nodes_001.links.new(named_attribute_001.outputs[0], separate_xyz_001.inputs[0])
			#separate_xyz_001.X -> compare_002.A
			geometry_nodes_001.links.new(separate_xyz_001.outputs[0], compare_002.inputs[0])
			#compare_002.Result -> math_001.Value
			geometry_nodes_001.links.new(compare_002.outputs[0], math_001.inputs[0])
			#random_value_002.Value -> math_001.Value
			geometry_nodes_001.links.new(random_value_002.outputs[3], math_001.inputs[1])
			#store_named_attribute_004.Geometry -> simulation_input_001.Geometry
			geometry_nodes_001.links.new(store_named_attribute_004.outputs[0], simulation_input_001.inputs[0])
			#simulation_input_001.Geometry -> set_position_002.Geometry
			geometry_nodes_001.links.new(simulation_input_001.outputs[1], set_position_002.inputs[0])
			#sample_index.Value -> set_position_002.Position
			geometry_nodes_001.links.new(sample_index.outputs[2], set_position_002.inputs[2])
			#math_001.Value -> set_position_002.Selection
			geometry_nodes_001.links.new(math_001.outputs[0], set_position_002.inputs[1])
			#math_001.Value -> math_004.Value
			geometry_nodes_001.links.new(math_001.outputs[0], math_004.inputs[1])
			#random_value_003.Value -> set_position_003.Offset
			geometry_nodes_001.links.new(random_value_003.outputs[0], set_position_003.inputs[3])
			#set_position_002.Geometry -> set_position_003.Geometry
			geometry_nodes_001.links.new(set_position_002.outputs[0], set_position_003.inputs[0])
			#math_004.Value -> set_position_003.Selection
			geometry_nodes_001.links.new(math_004.outputs[0], set_position_003.inputs[1])
			#store_named_attribute_005.Geometry -> simulation_output_001.Geometry
			geometry_nodes_001.links.new(store_named_attribute_005.outputs[0], simulation_output_001.inputs[0])
			#random_value_004.Value -> map_range.Value
			geometry_nodes_001.links.new(random_value_004.outputs[1], map_range.inputs[0])
			#map_range.Result -> math_005.Value
			geometry_nodes_001.links.new(map_range.outputs[0], math_005.inputs[0])
			#named_attribute_002.Attribute -> vector_math_006.Vector
			geometry_nodes_001.links.new(named_attribute_002.outputs[0], vector_math_006.inputs[0])
			#math_005.Value -> vector_math_006.Scale
			geometry_nodes_001.links.new(math_005.outputs[0], vector_math_006.inputs[3])
			#simulation_output_001.Geometry -> set_position_004.Geometry
			geometry_nodes_001.links.new(simulation_output_001.outputs[0], set_position_004.inputs[0])
			#set_position_004.Geometry -> instance_on_points_002.Points
			geometry_nodes_001.links.new(set_position_004.outputs[0], instance_on_points_002.inputs[0])
			#transform_geometry_003.Geometry -> instance_on_points_002.Instance
			geometry_nodes_001.links.new(transform_geometry_003.outputs[0], instance_on_points_002.inputs[2])
			#named_attribute_003.Attribute -> instance_on_points_002.Rotation
			geometry_nodes_001.links.new(named_attribute_003.outputs[0], instance_on_points_002.inputs[5])
			#map_range.Result -> instance_on_points_002.Scale
			geometry_nodes_001.links.new(map_range.outputs[0], instance_on_points_002.inputs[6])
			#rotate_instances.Instances -> join_geometry_002.Geometry
			geometry_nodes_001.links.new(rotate_instances.outputs[0], join_geometry_002.inputs[0])
			#join_geometry_002.Geometry -> group_output.Geometry
			geometry_nodes_001.links.new(join_geometry_002.outputs[0], group_output.inputs[0])
			#instance_on_points.Instances -> join_geometry_002.Geometry
			geometry_nodes_001.links.new(instance_on_points.outputs[0], join_geometry_002.inputs[0])
			#instance_on_points_002.Instances -> rotate_instances.Instances
			geometry_nodes_001.links.new(instance_on_points_002.outputs[0], rotate_instances.inputs[0])
			#set_position_003.Geometry -> store_named_attribute_005.Geometry
			geometry_nodes_001.links.new(set_position_003.outputs[0], store_named_attribute_005.inputs[0])
			#named_attribute_004.Attribute -> math_006.Value
			geometry_nodes_001.links.new(named_attribute_004.outputs[1], math_006.inputs[1])
			#math_006.Value -> rotate_instances.Selection
			geometry_nodes_001.links.new(math_006.outputs[0], rotate_instances.inputs[1])
			#random_value_005.Value -> vector_math_007.Vector
			geometry_nodes_001.links.new(random_value_005.outputs[0], vector_math_007.inputs[0])
			#vector_math_007.Vector -> vector_math_008.Vector
			geometry_nodes_001.links.new(vector_math_007.outputs[0], vector_math_008.inputs[0])
			#simulation_output.Geometry -> capture_attribute.Geometry
			geometry_nodes_001.links.new(simulation_output.outputs[0], capture_attribute.inputs[0])
			#math_001.Value -> store_named_attribute_005.Value
			geometry_nodes_001.links.new(math_001.outputs[0], store_named_attribute_005.inputs[4])
			#vector_math_009.Vector -> set_position_004.Offset
			geometry_nodes_001.links.new(vector_math_009.outputs[0], set_position_004.inputs[3])
			#vector_math_006.Vector -> vector_math_009.Vector
			geometry_nodes_001.links.new(vector_math_006.outputs[0], vector_math_009.inputs[0])
			#random_value_007.Value -> vector_math_009.Vector
			geometry_nodes_001.links.new(random_value_007.outputs[0], vector_math_009.inputs[1])
			#math_007.Value -> vector_math_008.Scale
			geometry_nodes_001.links.new(math_007.outputs[0], vector_math_008.inputs[3])
			#scene_time_001.Seconds -> math_007.Value
			geometry_nodes_001.links.new(scene_time_001.outputs[0], math_007.inputs[0])
			#random_value_006.Value -> math_007.Value
			geometry_nodes_001.links.new(random_value_006.outputs[1], math_007.inputs[1])
			#vector_math_008.Vector -> rotate_instances.Rotation
			geometry_nodes_001.links.new(vector_math_008.outputs[0], rotate_instances.inputs[2])
			#curve_to_mesh.Mesh -> join_geometry_002.Geometry
			geometry_nodes_001.links.new(curve_to_mesh.outputs[0], join_geometry_002.inputs[0])
			#capture_attribute.Attribute -> instance_on_points.Rotation
			geometry_nodes_001.links.new(capture_attribute.outputs[1], instance_on_points.inputs[5])
			#align_euler_to_vector.Rotation -> capture_attribute.Value
			geometry_nodes_001.links.new(align_euler_to_vector.outputs[0], capture_attribute.inputs[1])
			#material_selection.Selection -> color_ramp.Fac
			geometry_nodes_001.links.new(material_selection.outputs[0], color_ramp.inputs[0])
			return geometry_nodes_001

		geometry_nodes_001 = geometry_nodes_001_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Geometry Nodes.001", type = 'NODES')
		mod.node_group = geometry_nodes_001
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(GeometryNodes001.bl_idname)

def register():
	bpy.utils.register_class(GeometryNodes001)
	bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
	bpy.utils.unregister_class(GeometryNodes001)
	bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
	register()