import math

import pyglet
from pyglet.window import key


class ManualControl:
    def __init__(self, env, no_time_limit, domain_rand):
        self.env = env

        if no_time_limit:
            self.env.max_episode_steps = math.inf
        if domain_rand:
            self.env.domain_rand = True

    def run(self):
        print("============")
        print("Instructions")
        print("============")
        print("move: arrow keys\npickup: P\ndrop: D\ndone: ENTER\nquit: ESC")
        print("============")

        self.env.reset(options={'problem_id': 1})

        # Create the display window
        self.env.render()

        env = self.env

        @env.unwrapped.window.event
        def on_key_press(symbol, modifiers):
            """
            This handler processes keyboard commands that
            control the simulation
            """

            if symbol == key.BACKSPACE or symbol == key.SLASH:
                print("RESET")
                self.env.reset(options={'problem_id': 1})
                self.env.render()
                return

            if symbol == key.ESCAPE:
                self.env.close()

            if symbol == key.UP:
                self.step(self.env.actions.pickup)
            elif symbol == key.DOWN:
                self.step(self.env.actions.drop)
            elif symbol == key.LEFT:
                self.step(self.env.actions.turn_left)
            elif symbol == key.RIGHT:
                self.step(self.env.actions.turn_right)
            elif symbol == key.ENTER:
                self.step(self.env.actions.done)

        @env.unwrapped.window.event
        def on_key_release(symbol, modifiers):
            pass

        @env.unwrapped.window.event
        def on_draw():
            self.env.render()

        @env.unwrapped.window.event
        def on_close():
            pyglet.app.exit()

        # Enter main event loop
        pyglet.app.run()

        self.env.close()

    def step(self, action):
        print(
            "step {}/{}: {}".format(
                self.env.step_count + 1,
                self.env.max_episode_steps,
                self.env.actions(action).name,
            )
        )

        obs, reward, termination, truncation, info = self.env.step(action)

        if reward > 0:
            print(f"reward={reward:.2f}")

        if termination or truncation:
            print("done!")
            self.env.reset()

        self.env.render()
