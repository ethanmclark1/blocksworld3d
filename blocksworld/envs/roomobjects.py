import numpy as np

from gymnasium import utils
from blocksworld.entity import Block
from blocksworld.core import BlocksWorldEnv
from blocksworld.problems import get_problem_instance


class RoomObjects(BlocksWorldEnv, utils.EzPickle):
    BLOCK_SIZE = 0.6

    def __init__(self, size=6, **kwargs):
        self.size = size
        self.spots = [np.array((5, 0, z)) for z in range(1, self.size)]
        
        BlocksWorldEnv.__init__(self, max_episode_steps=100, **kwargs)
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
        self.place_agent(cam_height=0, pos=(1, 0, 3), dir=0)

    def _gen_blocks(self, problem_id):
        """Generate blocks based on the problem ID."""
        start, goal = get_problem_instance(problem_id)
        blocks = []
        for stack_idx, stack in enumerate(start):
            if len(stack) > 0:
                prev_block = None
                for block_idx, block in enumerate(stack):
                    block = Block(color=block, size=self.BLOCK_SIZE)
                    pos = self.spots[stack_idx] + np.array((0, block_idx * self.BLOCK_SIZE, 0))
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
            reward += 10
            termination = True
        
                
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
            self.state[loc].append(block.color)