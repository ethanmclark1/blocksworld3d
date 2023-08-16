import math
import numpy as np

from gymnasium import utils
from blocksworld.entity import Block, COLOR_NAMES
from blocksworld.core import BlocksWorldEnv


class RoomObjects(BlocksWorldEnv, utils.EzPickle):
    def __init__(self, size=6, **kwargs):
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

        self.agent.radius = 1
        self.place_agent(cam_height=0, pos=(1,0,3), dir=0)
        self.drop_spots = [np.array((5,0,z)) for z in range(1,6)]
        self.blocks = [Block(color=color, size=0.8) for color in COLOR_NAMES[:5]]
        
        # TODO: Add random ordering of blocks
        for blocks, pos in zip(self.blocks, self.drop_spots):
            self.place_entity(blocks, pos=pos, dir=0)
                

    def step(self, action):
        obs, reward, termination, truncation, info = super().step(action)
        
        # if not self.agent.carrying:
        #     if self.near(self.red_box, self.yellow_box):
        #         reward += self._reward()
        #         termination = True
                
        return obs, reward, termination, truncation, info