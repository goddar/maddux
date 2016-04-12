from arm_test import arm_test
from animation_test import animation_test
from plot_arm_test import plot_arm_test
from plot_test import plot_test

tests = {
    'arm': arm_test,
    'animation': animation_test,
    'plot_arm': plot_arm_test,
    'plot': plot_test,
}

def run_test(test):
    if test in tests:
        tests[test]()
        return True
    return False
    
