import copy
from itertools import chain

problems = {
    'gap': {
        'start': [
            [3, 2, 2, 5, 1],
            [0, 1, 3, 2, 1]
            ],
        'goal': [
            [0, 3, 1, 3, 0],
            [4, 0, 5, 0, 4]
            ]
    },
    'balance': {
        'start': [
            [5, 0, 4, 1, 2],
            [0, 0, 1, 3, 4]
            ],
        'goal': [
            [3, 1, 2, 1, 3],
            [3, 1, 2, 1, 3]
            ]
    },
    'stairs': {
        'start': [
            [4, 1, 0, 2, 0],
            [1, 2, 2, 3, 5]
            ],
        'goal': [
            [3, 2, 1, 2, 3],
            [2, 2, 1, 2, 2]
            ]
    },
    'pyramid': {
        'start': [
            [0, 2, 4, 3, 4],
            [2, 3, 1, 0, 1]
            ],
        'goal': [
            [0, 0, 1, 0, 0],
            [3, 4, 5, 4, 3]
            ]
    },
    'bed': {
        'start': [
            [1, 3, 1, 0, 1],
            [3, 2, 0, 4, 5]
            ],
        'goal': [
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2]
            ]
    },
    'towers': {
        'start': [
            [5, 1, 0, 2, 1],
            [0, 5, 3, 1, 2]
            ],
        'goal': [
            [0, 0, 0, 0, 0],
            [4, 4, 4, 4, 4]
            ]
    },
    'wave-v0': {
        'start': [
            [1, 1, 4, 0, 2],
            [2, 3, 2, 4, 1]
            ],
        'goal': [
            [0, 1, 2, 3, 4], 
            [0, 1, 2, 3, 4]
            ]
    },
    'wave-v1': {
        'start': [
            [0, 2, 3, 1, 3],
            [3, 0, 1, 3, 4]
            ],
        'goal': [
            [4, 3, 2, 1, 0], 
            [4, 3, 2, 1, 0]
            ]
    }
}


def get_problem_list():
    return list(problems.keys())

def get_problem_instance(problem_instance):
    start = copy.deepcopy(problems[problem_instance]['start'])
    goal = copy.deepcopy(problems[problem_instance]['goal'])
    return start, goal