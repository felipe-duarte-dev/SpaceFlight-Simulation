from src.physics.vector_2d import Vector2D

class Camera:
    def __init__(self, width: int, height: int, scale: float = 20.0, min_scale: float = 5.0, max_scale: float = 100.0, zoom_factor: float = 1.1) -> None:
        self.center_x = width // 2
        self.center_y = height // 2
        self.scale = scale
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.zoom_factor = zoom_factor

    def world_to_screen(self, position: Vector2D) -> tuple[int, int]:
        screen_x = int(self.center_x + position.x * self.scale)
        screen_y = int(self.center_y + position.y * self.scale)

        return screen_x, screen_y

    def scale_length(self, length: float, min_pixels: int = 2) -> int:
        return max(min_pixels, int(length * self.scale))

    def zoom_in(self) -> bool:
        previous_scale = self.scale
        self.scale = min(self.max_scale, self.scale * self.zoom_factor)
        return self.scale != previous_scale

    def zoom_out(self) -> bool:
        previous_scale = self.scale
        self.scale = max(self.min_scale, self.scale / self.zoom_factor)
        return self.scale != previous_scale