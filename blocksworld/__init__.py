import gymnasium as gym
from blocksworld import envs

def env(render_mode=None):
    return gym.make("BlocksWorld-v0", view='agent', render_mode=render_mode)
