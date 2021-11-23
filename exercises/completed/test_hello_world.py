import unittest, sys, io

class HelloWorldTests(unittest.TestCase):
    def setUp(self):
        self.real_stdout = sys.stdout
        self.fake_stdout = io.StringIO()
        sys.stdout = self.fake_stdout


    def test_print(self):
        import hello_world

        try:
            self.assertEqual("Hello, World!\n", self.fake_stdout.getvalue(), 'Program did not print "Hello, World!"')
        except AssertionError as err:
            test_result = self.defaultTestResult()
            test_result.__setattr__("friendly_messages", [ "what?" ])
            raise err


    def tearDown(self):
        sys.stdout = self.real_stdout


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromName(__name__)
    silent_runner = unittest.TextTestRunner(stream=io.StringIO())
    result = silent_runner.run(test_suite)

    if result.wasSuccessful():
        print("Yay! Everything works!")
    else:
        failure_messages = '\n'.join(msg for _, msg in result.failures + result.errors)
        message = f"Oh, no! Something isn't quite right:\n{failure_messages}"
        print(message)
        print(result.friendly_messages)





