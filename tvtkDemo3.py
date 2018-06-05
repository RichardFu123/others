from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop
plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name="combxyz.bin",
    q_file_name="combq.bin",
    scalar_function_number=100,
    vector_function_number=200)#读取plot3d数据
plot3d.update()
grid = plot3d.output.get_block(0)#获取读入的数据

con = tvtk.ContourFilter()#创建等值面
con.set_input_data(grid)
con.generate_values(10,grid.point_data.scalars.range)#指定数据范围

m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,input_connection=con.output_port)
a = tvtk.Actor(mapper = m)
a.property.opacity = 0.5#透明度
win  = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
