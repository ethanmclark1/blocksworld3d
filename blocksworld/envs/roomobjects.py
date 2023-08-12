import math

from gymnasium import utils
from blocksworld.entity import Box
from blocksworld.core import BlocksWorldEnv


class RoomObjects(BlocksWorldEnv, utils.EzPickle):
    def __init__(self, size=10, **kwargs):
        assert size >= 2
        self.size = size

        BlocksWorldEnv.__init__(self, max_episode_steps=math.inf, **kwargs)
        utils.EzPickle.__init__(self, size, **kwargs)

    def _gen_world(self):
        self.add_rect_room(
            min_x=0,
            max_x=self.size,
            min_z=0,
            max_z=self.size,
            wall_tex="brick_wall",
            floor_tex="asphalt",
            no_ceiling=False,
        )

        # Reduce chances that objects are too close to see
        self.agent.radius = 1.5
        self.place_agent(pos=(5,0,5), dir=0)
        
        self.place_entity(Box(color='yellow', size=0.4), pos=(8,0,4), dir=0)
        self.place_entity(Box(color='blue', size=0.4), pos=(8,0,4.5), dir=0)
        self.place_entity(Box(color='green', size=0.4), pos=(8,0,5), dir=0)
        self.place_entity(Box(color='purple', size=0.4), pos=(8,0,5.5), dir=0)
        self.place_entity(Box(color='red', size=0.4), pos=(8,0,6), dir=0)

    def step(self, action):
        obs, reward, termination, truncation, info = super().step(action)
        return obs, reward, termination, truncation, info