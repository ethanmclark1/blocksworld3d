import math

from gymnasium import utils
from blocksworld.entity import Box
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
        
        # TODO: Fix placing block in the crosshairs
        # TODO: Fix picking up a block in the crosshairs
        
        self.place_entity(Box(color='yellow', size=0.8), pos=(5,0,1), dir=0)
        self.place_entity(Box(color='blue', size=0.8), pos=(5,0,2), dir=0)
        self.place_entity(Box(color='green', size=0.8), pos=(5,0,3), dir=0)
        self.place_entity(Box(color='purple', size=0.8), pos=(5,0,4), dir=0)
        self.place_entity(Box(color='red', size=0.8), pos=(5,0,5), dir=0)
        
        self.blocks = [entity for entity in self.entities if isinstance(entity, Box)]

    def step(self, action):
        obs, reward, termination, truncation, info = super().step(action)
        
        # if not self.agent.carrying:
        #     if self.near(self.red_box, self.yellow_box):
        #         reward += self._reward()
        #         termination = True
                
        return obs, reward, termination, truncation, info