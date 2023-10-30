# An Extension of MiniWorld

Blocksworld3D, building upon the MiniWorld environment, specifically targets the RoomObjects scenario. Designed for reinforcement learning and robotics research, this minimalistic environment aligns with the MiniWorld API.

# Blocksworld3D

Blocksworld3D extends the traditional BlocksWorld planning problem to a 3D domain, adding extra rows of blocks. It presents eight problems, each with unique constraints on initial block positioning and final objectives.

## Installation

Install from ``PyPi`` using:

``pip install blocksworld3d``

Or install from the source using:

```
git clone https://github.com/ethanmclark1/blocksworld3d.git
cd blocksworld3d
pip install -r requirements.txt
pip install -e .
```

## Usage

```
import blocksworld3d

env = blocksworld3d.env()
env.reset(options={'problem_instance': 'gap'}))
observation, _, terminations, truncations, _ = env.last()
env.step(action)
env.close()
```

## List of Problem Instances

| Problem Instance |
| ---------------- |
| ``gap``          |
| ``balance``      |
| ``stairs``       |
| ``pyramid``      |
| ``bed``          |
| ``towers``       |
| ``wave-v0``      |
| ``wave-v1``      |

## Contributing

We welcome contributions to Blocksworld3d! Whether it's bug reports, feature requests, or pull requests, your collaboration helps make Blocksworld3d better.

## Support

If you have questions or need support, please contact us at [eclark715@gmail.com](mailto:eclark715@gmail.com), or create an issue in the GitHub repository.

## License

Blocksworld3d is open-source software licensed under the [MIT license](https://chat.openai.com/LINK_TO_YOUR_LICENSE).

## Paper Citation

If you found this environment helpful, consider citing relevant papers. Here's an example citation for the original MiniWorld environment:

<pre>
@article{MinigridMiniworld23,
  author={Maxime Chevalier-Boisvert and Bolun Dai and Mark Towers and Rodrigo de Lazcano and Lucas Willems and Salem Lahlou and Suman Pal and Pablo Samuel Castro and Jordan Terry},
  title={Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks},
  journal={CoRR},
  volume={abs/2306.13831}
  year={2023}
}
</pre>
