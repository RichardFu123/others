from tvtk.api import tvtk
from tvtkfunc import ivtk_scene,event_loop

plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name = "combxyz.bin",
    q_file_name = "combq.bin",
    scalar_function_number = 100,
    vector_function_number = 200
    )
plot3d.update()
grid = plot3d.output.get_block(0)
#用MaskPoints来pooling
mask = tvtk.MaskPoints(random_mode=True, on_ratio=10)#随机选点，10选一
mask.set_input_data(grid)
glyph_source = tvtk.ArrowSource()

#用Glyph3D在MaskPoints的点上放上ArrowSource（箭头）
glyph = tvtk.Glyph3D(input_connection=mask.output_port,scale_factor=1)
glyph.set_source_connection(glyph_source.output_port)
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=glyph.output_port)
a = tvtk.Actor(mapper=m)

win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
