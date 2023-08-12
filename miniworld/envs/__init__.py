import gymnasium as gym

from miniworld.envs.roomobjects import RoomObjects

__all__ = [
    "RoomObjects",
]

gym.register(
    id="MiniWorld-RoomObjects-v0",
    entry_point="miniworld.envs.roomobjects:RoomObjects",
)