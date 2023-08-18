import math
import numpy as np

from gymnasium import utils
from .utils.entity import Block
from .utils.core import MiniWorldEnv
from .utils.problems import get_problem_instance


class BlocksWorld3D(MiniWorldEnv, utils.EzPickle):
    BLOCK_SIZE = 0.6

    def __init__(self, size=6, **kwargs):
        self.size = size
        self.cur_row = 0
        self.prev_dir = None
        self.spots = [[np.array((4, 0, z)) for z in range(1, self.size)],
                      [np.array((5, 0, z)) for z in range(1, self.size)]]
        
        MiniWorldEnv.__init__(self, max_episode_steps=100, **kwargs)
        utils.EzPickle.__init__(self, size, **kwargs)
        
    def _gen_world(self, problem_id):
        """Generate the world based on the problem ID."""
        self._create_room()
        self._place_agent()
        self.blocks, self.state, self.goal = self._gen_blocks(problem_id)

    def _create_room(self):
        """Add room with specific boundaries and textures."""
        self.add_rect_room(
            min_x=0,
            max_x=self.size,
            min_z=0,
            max_z=self.size,
            wall_tex="brick_wall",
            floor_tex="asphalt",
            no_ceiling=False,
        )

    def _place_agent(self):
        """Place the agent in the world."""
        self.agent.radius = 1
        dir = np.random.choice((-1, 1)) * 30 * math.pi / 180
        self.place_agent(cam_height=0, pos=(1, 0, 3), dir=dir)

    def _gen_blocks(self, problem_id):
        """Generate blocks based on the problem ID."""
        start, goal = get_problem_instance(problem_id)
        blocks = []
        
        for row_idx, row in enumerate(start):
            for stack_idx, stack in enumerate(row):
                if len(stack) > 0:
                    prev_block = None
                    for block_idx, block in enumerate(stack):
                        block = Block(color=block, size=self.BLOCK_SIZE)
                        pos = self.spots[row_idx][stack_idx] + np.array((0, block_idx * self.BLOCK_SIZE, 0))
                        self.place_entity(block, pos=pos, dir=0)

                        if prev_block:
                            prev_block.is_beneath = block
                            block.is_above = prev_block

                        blocks.append(block)
                        prev_block = block

        return blocks, start, goal

    def step(self, action):
        """Step the environment with the given action."""
        obs, reward, termination, truncation, info = super().step(action)
        
        if self.state == self.goal:
            reward = 5
            termination = True
        
        reward = -0.1 if reward == 0 else reward
                
        return obs, reward, termination, truncation, info
    
    def update_representation(self, block, loc=None):
        """Update the internal representation of the blocksworld state."""
        if loc is None:
            # Remove block from state during pickup action
            for idx, stack in enumerate(self.state):
                if block.color in stack:
                    self.state[idx].remove(block.color)
                    break
        else:
            # Add block to state during drop action
            self.state[self.cur_row][loc].append(block.color)