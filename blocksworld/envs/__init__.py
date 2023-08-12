import gymnasium as gym

from blocksworld.envs.roomobjects import RoomObjects

__all__ = [
    "RoomObjects",
]

gym.register(
    id="BlocksWorld-RoomObjects-v0",
    entry_point="blocksworld.envs.roomobjects:RoomObjects",
)