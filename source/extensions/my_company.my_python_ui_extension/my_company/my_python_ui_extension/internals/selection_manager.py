class SelectionManager:

    def __init__(self):
        self._count = 0
        self.mode = "BODY"

    def reset(self):
        self._count = 0
        return "empty"

    def body_click(self):
        self._count += 1
        return f"Body count: {self._count}"

    def face_click(self):
        self._count += 2
        return f"Face count: {self._count}"

    def edge_click(self):
        self._count += 10
        return f"Edge count: {self._count}"

    def vertex_click(self):
        self._count += 5
        return f"Vertex count: {self._count}"