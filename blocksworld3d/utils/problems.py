problems = {
    '0': {
        'start': [
            [['red'], ['green', 'blue'], [], ['purple'], ['yellow', 'red']],
            [['blue'], ['green'], ['blue'], ['red'], ['purple']]
        ],
        'goal': [
            [['blue'], ['red', 'green'], ['purple'], ['yellow'], ['red']],
            [['red'], ['green'], ['blue', 'purple'], ['purple'], ['yellow', 'blue']]
        ]
    },
    '1': {
        'start': [
            [['red', 'yellow'], ['green'], ['blue', 'purple'], ['purple'], []],
            [['yellow'], ['red'], ['green'], ['blue'], ['purple', 'red']]
        ],
        'goal': [
            [['purple', 'red'], ['yellow'], ['green'], ['red'], ['blue']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'blue']]
        ]
    },
    '2': {
        'start': [
            [['red'], ['green'], ['blue', 'yellow'], ['purple'], ['yellow']],
            [['green'], ['blue'], ['purple'], ['yellow'], ['red', 'purple']]
        ],
        'goal': [
            [['blue'], ['purple'], ['yellow'], ['red'], ['green', 'blue']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'red']]
        ]
    },
    '3': {
        'start': [
            [['red'], ['green', 'blue'], ['blue'], ['purple'], ['yellow', 'red']],
            [['green'], ['blue'], ['purple', 'yellow'], ['yellow'], ['red']]
        ],
        'goal': [
            [['yellow', 'red'], ['red'], ['green'], ['blue'], ['purple']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'blue']]
        ]
    },
    '4': {
        'start': [
            [['red'], ['green'], ['blue'], ['purple'], ['yellow']],
            [['blue'], ['purple'], ['red', 'yellow'], ['red'], ['green']]
        ],
        'goal': [
            [['green'], ['blue'], ['purple'], ['yellow'], ['red', 'blue']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'red']]
        ]
    },
    '5': {
        'start': [
            [['red'], ['green'], ['blue'], ['purple', 'yellow'], ['yellow']],
            [['green'], ['blue'], ['purple'], ['yellow'], ['red', 'green']]
        ],
        'goal': [
            [['red'], ['purple'], ['yellow'], ['green'], ['blue', 'red']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'blue']]
        ]
    },
    '6': {
        'start': [
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'red']],
            [['green'], ['blue'], ['purple'], ['yellow'], ['red']]
        ],
        'goal': [
            [['blue'], ['yellow'], ['red'], ['green'], ['purple', 'red']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'blue']]
        ]
    },
    '7': {
        'start': [
            [['red'], ['green'], ['blue'], ['purple'], ['yellow']],
            [['green'], ['blue'], ['purple'], ['yellow', 'red'], ['red']]
        ],
        'goal': [
            [['purple'], ['yellow'], ['red'], ['green'], ['blue']],
            [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'red']]
        ]
    }
}


def get_num_problems():
    return len(problems)

def get_problem_instance(problem_id):
    return problems[str(problem_id)]['start'], problems[str(problem_id)]['goal']