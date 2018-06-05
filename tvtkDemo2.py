from tvtk.api import tvtk

def ivtk_scene(actors):
    from tvtk.tools import ivtk
    #创建窗口
    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    win.scene.add_actor(actors)

    #修正子窗口脱离bug
    dialog = win.control.centralWidget().widget(0).widget(0)
    from pyface.qt import QtCore
    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show()

    return win

def event_loop():
    from pyface.api import GUI
    gui=GUI()
    gui.start_event_loop()


if __name__ =="__main__":
    try:
        s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
        m = tvtk.PolyDataMapper(input_connection=s.output_port)
        a = tvtk.Actor(mapper=m)
        win = ivtk_scene(a)
        win.scene.isometric_view()
        event_loop()
    except:
        print("error")
