import numpy as np
from typing import List, Tuple

def circle(num_points: int, radius: float = 1.0, center: Tuple[float, float] = (0, 0)) -> np.ndarray:
    """Generate a circle curve."""
    angles = np.linspace(0, 2*np.pi, num_points)
    x = radius * np.cos(angles) + center[0]
    y = radius * np.sin(angles) + center[1]
    return np.column_stack((x, y))


def ellipse(num_points: int, major_axis: float = 1.0, minor_axis: float = 0.5, center: Tuple[float, float] = (0, 0)) -> np.ndarray:
    """Generate an ellipse curve."""
    angles = np.linspace(0, 2*np.pi, num_points)
    x = major_axis * np.cos(angles) + center[0]
    y = minor_axis * np.sin(angles) + center[1]
    return np.column_stack((x, y))


def sine(num_points: int, amplitude: float = 1.0, frequency: float = 1.0, phase: float = 0.0) -> np.ndarray:
    """Generate a sine wave curve."""
    x = np.linspace(0, 2*np.pi, num_points)
    y = amplitude * np.sin(frequency * x + phase)
    return np.column_stack((x, y))


def spiral(num_points: int, radius_start: float = 0.1, radius_end: float = 1.0, num_turns: float = 2.0) -> np.ndarray:
    """Generate a spiral curve."""
    t = np.linspace(0, num_turns * 2*np.pi, num_points)
    r = np.linspace(radius_start, radius_end, num_points)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.column_stack((x, y))


def random_walk(num_points: int, step_size: float = 0.1) -> np.ndarray:
    """Generate a random walk curve."""
    x = np.cumsum(np.random.randn(num_points) * step_size)
    y = np.cumsum(np.random.randn(num_points) * step_size)
    return np.column_stack((x, y))
    

def generate_random_walk_curves(num_curves: int, num_points: int, step_size: float = 0.1) -> List[np.ndarray]:
    """Generate random walk curves."""
    curves = []
    for i in range(num_curves):
        curve = random_walk(num_points, step_size)
        curves.append(curve)
    return curves