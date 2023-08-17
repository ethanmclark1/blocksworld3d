import gymnasium as gym
from blocksworld.blocksworld import BlocksWorld

__all__ = [
    "BlocksWorld",
]

gym.register(
    id="BlocksWorld-v0",
    entry_point="blocksworld.blocksworld:BlocksWorld",
)

def env(render_mode=None, max_cycles=100):
    return gym.make("BlocksWorld-v0", view='agent', render_mode=render_mode, max_episode_steps=max_cycles)