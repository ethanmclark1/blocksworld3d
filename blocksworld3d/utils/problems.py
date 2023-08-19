import copy

problems = {
    'gap': {
        'start': [
            [3, 0, 3, 0, 3],
            [0, 1, 0, 1, 0]
            ],
        'goal': [
            [0, 2, 0, 2, 0],
            [2, 0, 3, 0, 2]
            ]
    },
    'balance': {
        'start': [
            [1, 3, 0, 2, 2],
            [2, 1, 1, 0, 2]
            ],
        'goal': [
            [2, 1, 1, 1, 2],
            [2, 1, 1, 1, 2]
            ]
    },
    'exchange': {
        'start': [
            [2, 1, 2, 1, 2],
            [1, 0, 1, 0, 1]
            ],
        'goal': [
            [1, 0, 1, 0, 1],
            [2, 1, 2, 1, 2]
            ]
    },
    'stairs': {
        'start': [
            [1, 2, 3, 2, 1],
            [0, 1, 1, 1, 0]
            ],
        'goal': [
            [0, 0, 1, 0, 0],
            [3, 2, 1, 2, 3]
            ]
    },
    'bed': {
        'start': [
            [4, 2, 2, 0, 4],
            [3, 2, 1, 2, 0]
            ],
        'goal': [
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2]
            ]
    },
    'towers': {
        'start': [
            [4, 0, 4, 0, 4],
            [0, 1, 1, 1, 0]
            ],
        'goal': [
            [0, 0, 0, 0, 0],
            [3, 3, 3, 3, 3]
            ]
    },
    'foldable': {
        'start': [
            [1, 2, 3, 2, 1],
            [2, 0, 3, 0, 2]
            ],
        'goal': [
            [2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2]
            ]
    },
    'wave': {
        'start': [
            [3, 2, 3, 3, 3],
            [3, 0, 1, 2, 0]
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