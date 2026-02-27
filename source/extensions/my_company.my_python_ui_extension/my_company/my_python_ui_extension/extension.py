import omni.ext
import omni.ui as ui
from .internals.selection_manager import SelectionManager

def some_public_function(x: int):
    """This is a public function that can be called from other extensions."""
    print(f"[my_company.my_python_ui_extension] some_public_function was called with {x}")
    return x ** x

class MyExtension(omni.ext.IExt):

    def on_startup(self, _ext_id):
        """This is called every time the extension is activated."""
        print("[my_company.my_python_ui_extension] Extension startup")
        self._window = ui.Window(
            "Selection Type", width=300, height=200
        )
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("empty")
                self.manager = SelectionManager()
                with ui.HStack():
                        ui.Button("B", clicked_fn=lambda: setattr(label, "text", self.manager.body_click()))
                        ui.Button("F", clicked_fn=lambda: setattr(label, "text", self.manager.face_click()))
                        ui.Button("E", clicked_fn=lambda: setattr(label, "text", self.manager.edge_click()))
                        ui.Button("V", clicked_fn=lambda: setattr(label, "text", self.manager.vertex_click()))

    def on_shutdown(self):
        """This is called every time the extension is deactivated. It is used
        to clean up the extension state."""
        print("[my_company.my_python_ui_extension] Extension shutdown")
