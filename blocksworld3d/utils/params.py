from collections import namedtuple
from copy import deepcopy

import numpy as np


class DomainParams:
    """
    Set of simulation parameters
    """

    # Simulation parameter, with domain randomization range
    # The default value is used when domain randomization is disabled
    DomainParam = namedtuple("Domainparam", ["default", "min", "max", "type"])
    DomainParam.__qualname__ = "DomainParams.DomainParam"

    def __init__(self):
        # Dictionary of parameters, indexed by name
        self.params = {}

    def copy(self):
        return deepcopy(self)

    def no_random(self):
        """
        Make a copy in which randomization is disabled for all parameters
        This is useful to then selectively enable randomization on a
        limited subset of the parameters.
        """

        copy = self.copy()

        for name, p in copy.params.items():
            copy.params[name] = DomainParams.DomainParam(
                p.default, p.default, p.default, p.type
            )

        return copy

    def set(self, name, default, min=None, max=None, type="float"):
        """
        Register/modify a named parameter
        """

        if isinstance(default, list):
            default = np.array(default)
        if isinstance(min, list):
            min = np.array(min)
        if isinstance(max, list):
            max = np.array(max)

        if min is None:
            min = default
        if max is None:
            max = default

        if isinstance(default, np.ndarray):
            assert max.shape == default.shape
            assert min.shape == max.shape
            assert np.all(np.greater_equal(max, default))
            assert np.all(np.greater_equal(default, min))

            if type == "float":
                default = default.astype("float")
                min = min.astype("float")
                max = max.astype("float")
        else:
            assert max >= default
            assert default >= min

        # Validation when modifying existing parameters
        if name in self.params:
            p = self.params[name]
            assert type == p.type
            if isinstance(p.default, np.ndarray):
                assert default.shape == p.default.shape

        self.params[name] = DomainParams.DomainParam(default, min, max, type)

    def get_max(self, name):
        assert name in self.params, name
        p = self.params[name]
        return p.max

    def sample(self, rng, name):
        """
        Sample a single parameter
        Note: when rng is None, the default value is returned, which
        has the effect of turning off domain randomization
        """

        assert name in self.params, name
        p = self.params[name]

        if rng is None:
            return p.default

        if p.type == "float":
            return rng.uniform(p.min, p.max)
        elif p.type == "int":
            return rng.integers(p.min, p.max + 1)

        assert False

    def sample_many(self, rng, target_obj, param_names):
        """
        Sample a list of parameters
        """

        for name in param_names:
            setattr(target_obj, name, self.sample(rng, name))


# Default simulation parameters
DEFAULT_PARAMS = DomainParams()
DEFAULT_PARAMS.set("sky_color", [0.25, 0.82, 1], [0.1, 0.1, 0.1], [1.0, 1.0, 1.0])
DEFAULT_PARAMS.set("light_pos", [0, 2.5, 0], [-40, 2.5, -40], [40, 5, 40])
DEFAULT_PARAMS.set("light_color", [0.7, 0.7, 0.7], [0.45, 0.45, 0.45], [0.8, 0.8, 0.8])
DEFAULT_PARAMS.set("light_ambient", [0.45, 0.45, 0.45], [0.35, 0.35, 0.35], [0.55, 0.55, 0.55])
DEFAULT_PARAMS.set("obj_color_bias", [0, 0, 0], [-0.2, -0.2, -0.2], [0.2, 0.2, 0.2])
DEFAULT_PARAMS.set("bot_radius", 0.4, 0.38, 0.42)