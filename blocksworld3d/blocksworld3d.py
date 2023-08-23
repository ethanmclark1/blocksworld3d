import math
import numpy as np

from gymnasium import utils
from .utils.entity import Block
from .utils.core import MiniWorldEnv
from .utils.problems import get_problem_instance


class BlocksWorld3D(MiniWorldEnv, utils.EzPickle):
    BLOCK_SIZE = 0.8

    def __init__(self, size=8, **kwargs):
        self.size = size
        self.cur_row = 0
        self.prev_move = None
        self.spots = [[np.array((4, 0, z)) for z in range(2, self.size - 1)],
                      [np.array((7, 0, z)) for z in range(2, self.size - 1)]]
        
        MiniWorldEnv.__init__(self, max_episode_steps=100, **kwargs)
        utils.EzPickle.__init__(self, size, **kwargs)
    
    def _gen_world(self, problem_instance):
        """Generate the world based on the problem ID."""
        self._create_room()
        self._place_agent()
        self.blocks, self.state, self.goal = self._gen_blocks(problem_instance)

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
        loc = np.random.choice((2, self.size-2))
        self.place_agent(pos=(2, 0, loc), dir=0)

    def _gen_blocks(self, problem_instance):
        """Generate blocks based on the problem instance."""
        blocks = []
        start, goal = get_problem_instance(problem_instance)
        
        for row_idx, row in enumerate(start):
            for stack_idx, stack in enumerate(row):
                if stack != 0:
                    prev_block = None
                    for block_idx in range(stack):
                        block = Block(color='blue', size=self.BLOCK_SIZE)
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
            reward = 10
            termination = True
        
        reward = -0.1 if reward == 0 else reward
                
        return obs, reward, termination, truncation, info
    
    def update_representation(self, loc, action):
        """Update the internal representation of the blocksworld state."""
        if action is 'pickup':
            # Remove block from state during pickup action
            self.state[self.cur_row][loc] -= 1
        else:
            # Add block to state during drop action
            self.state[self.cur_row][loc] += 1