problems = {
    '0': {
        'start': [['red'], ['green'], ['blue'], ['purple'], ['yellow']],
        'goal': [['yellow'], ['red'], ['purple'], ['blue'], ['green']]
    },
    '1': {
        'start': [['red', 'green'], ['blue'], ['purple'], ['yellow'], []],
        'goal': [['purple'], ['yellow'], ['green'], ['red'], ['blue']]
    },
    '2': {
        'start': [['red'], ['green', 'blue'], ['purple'], ['yellow'], []],
        'goal': [['yellow'], ['purple'], ['blue'], ['green'], ['red']]
    },
    '3': {
        'start': [['red', 'green'], ['blue', 'purple'], ['yellow'], [], []],
        'goal': [['yellow', 'purple'], ['red'], ['blue'], ['green'], []]
    },
    '4': {
        'start': [['red', 'green'], ['blue'], ['purple'], ['yellow'], []],
        'goal': [['blue'], ['purple'], ['yellow'], ['red'], ['green']]
    },
    '5': {
        'start': [['red'], ['green', 'blue'], ['purple'], ['yellow'], ['grey']],
        'goal': [['grey'], ['yellow'], ['green'], ['blue'], ['red', 'purple']]
    },
    '6': {
        'start': [['red', 'green'], ['blue', 'purple'], ['yellow'], ['grey'], []],
        'goal': [['grey'], ['yellow'], ['blue'], ['green', 'red'], ['purple']]
    },
    '7': {
        'start': [['red'], ['green'], ['blue'], ['purple'], ['yellow', 'grey']],
        'goal': [['grey'], ['yellow'], ['green'], ['red'], ['blue', 'purple']]
    },
}

def get_num_problems():
    return len(problems)

def get_problem_instance(problem_id):
    return problems[str(problem_id)]['start'], problems[str(problem_id)]['goal']