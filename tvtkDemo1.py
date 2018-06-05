from tvtk.api import tvtk


def ShowACube(x,y,z,backgroundcolor=(0,0,0)):
    #立方体源
    s = tvtk.CubeSource(x_length=x,y_length=y,z_length=z)
    #转换源为图形数据
    m = tvtk.PolyDataMapper(input_connection=s.output_port)
    #创建Actor，并将图形数据接入
    a = tvtk.Actor(mapper = m)
    #创建渲染，并将Actor接入
    r = tvtk.Renderer(background = backgroundcolor)
    r.add_actor(a)
    #创建窗口，并将渲染接入
    w = tvtk.RenderWindow(size = (900,900))
    w.add_renderer(r)
    #创建交互，并将窗口接入
    i = tvtk.RenderWindowInteractor(render_window = w)

    #开始运行
    i.initialize()
    i.start()

if __name__ == "__main__":
    
    try:
        x,y,z = tuple(eval(input('please enter (x,y,z): ')))
        ShowACube(x=x,y=y,z=z)
    except:
        print("Input Error, Please input as 'x_length,y_length,z_length'")
