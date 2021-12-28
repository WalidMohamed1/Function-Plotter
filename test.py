import function_Plotter
import unittest

class Test(unittest.TestCase):
    def testFunction(self):
        try:
            result = function_Plotter.Window.string2func(self,"x")
            print('Correct function!')
        except ValueError as e:
            print('Incorrect function!')

        try:
            result = function_Plotter.Window.string2func(self,"y")
            print('Correct function!')
        except ValueError as e:
            print('Incorrect function!')

        try:
            result = function_Plotter.Window.string2func(self,"5*x^3 + 2*x")
            print('Correct function!')
        except ValueError as e:
            print('Incorrect function!')

        try:
            result = function_Plotter.Window.string2func(self,"x^2+3-1")
            print('Correct function!')
        except ValueError as e:
            print('Incorrect function!')

        try:
            result = function_Plotter.Window.string2func(self,"sin(x)*cos(x)")
            print('Correct function!')
        except ValueError as e:
            print('Incorrect function!')

        try:
            result = function_Plotter.Window.string2func(self,"bla bla")
            print('Correct function!')
        except ValueError as e:
            print('Incorrect function!')
                                    


if __name__ == '__main__':
    unittest.main()       