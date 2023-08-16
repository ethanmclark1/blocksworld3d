import gymnasium as gym

from blocksworld.envs.blocksworld import BlocksWorld

__all__ = [
    "BlocksWorld",
]

gym.register(
    id="BlocksWorld-BlocksWorld-v0",
    entry_point="blocksworld.envs.blocksworld:BlocksWorld",
)