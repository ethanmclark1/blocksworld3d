import gymnasium as gym
from blocksworld3d.blocksworld3d import BlocksWorld3D

__all__ = [
    "BlocksWorld3D",
]

gym.register(
    id="BlocksWorld3D-v0",
    entry_point="blocksworld3d.blocksworld3d:BlocksWorld3D",
)

def env(render_mode=None, max_cycles=100):
    return gym.make("BlocksWorld3D-v0", view='agent', render_mode=render_mode, max_episode_steps=max_cycles)