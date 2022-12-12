# test_lexing.py
#
# ICS 33 Fall 2022
# Project 3: Why Not Smile?
#
# Unit tests for the provided grin.excuting module.
#
from grin.excuting import *
import sys
import io
import unittest



class TestGrinExcuting(unittest.TestCase):

    def stub_stdin(self, inputs):
        stdin = sys.stdin

        def cleanup():
            sys.stdin = stdin

        self.addCleanup(cleanup)
        sys.stdin = io.StringIO(inputs)


    def stub_stdout(self):
        stderr = sys.stderr
        stdout = sys.stdout

        def cleanup():
            sys.stderr = stderr
            sys.stdout = stdout

        self.addCleanup(cleanup)
        sys.stderr = io.StringIO()
        sys.stdout = io.StringIO()


    def test_LET(self):
        command = ["LET A 1", "LET B A", "LET C \"ok\""]

        excute(command)
        self.assertEqual(ASSIGN, {'A': 1, 'B': 1, 'C': 'ok'})

    def test_PRINT(self):
        command = ["PRINT \"Hello World\"",
                  "LET A 1",
                  "LET B \"good\"",
                  "LET C A",
                  "PRINT A",
                  "PRINT C",
                  "PRINT B"]
        self.stub_stdout()
        excute(command)
        expect = "Hello World\n" \
                 "1\n" \
                 "1\n" \
                 "good\n" \
                 ""
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_INNUM(self):
        command = ["INNUM A", "PRINT A"]
        self.stub_stdin('15')
        self.stub_stdout()
        excute(command)
        expect = '15\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_INSTR(self):
        command = ["INSTR A", "PRINT A", "LET B A", "PRINT B"]
        self.stub_stdin('hello')
        self.stub_stdout()
        excute(command)
        expect = 'hello\nhello\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_ADD1(self):
        command = ["LET A 5", "ADD A 5", "PRINT A"]
        self.stub_stdout()
        excute(command)
        expect = '10\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_ADD2(self):
        command = ["LET A \"hell\"", "ADD A \"o\"", "PRINT A"]
        self.stub_stdout()
        excute(command)
        expect = 'hello\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_example1(self):
        command = ["LET MESSAGE \"Hello Boo!\"", "PRINT MESSAGE", "."]
        self.stub_stdout()
        excute(command)
        expect = 'Hello Boo!\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_example2(self):
        command = ["LET A 3",
                   "PRINT A",
                   "GOSUB \"CHUNK\"",
                   "PRINT A",
                   "PRINT B",
                   "GOTO \"FINAL\"",
                   "CHUNK: LET A 4",
                   "LET B 6",
                   "RETURN",
                   "FINAL: PRINT A",
                   "."
                   ]
        self.stub_stdout()
        excute(command)
        expect = '3\n4\n6\n4\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_example3(self):
        command = ["LET NAME \"Boo\"",
                   "LET AGE 13.015625",
                   "PRINT NAME",
                   "PRINT AGE",
                   "."
                   ]
        self.stub_stdout()
        excute(command)
        expect = 'Boo\n13.015625\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_example4(self):
        command = ["LET Z 5",
                   "GOTO 5",
                   "LET C 4",
                   "PRINT C",
                   "PRINT Z",
                   "END",
                   "PRINT C",
                   "PRINT Z",
                   "GOTO -6",
                   "."
                   ]
        self.stub_stdout()
        excute(command)
        expect = '1\n5\n4\n5\n'
        self.assertEqual(sys.stdout.getvalue(), expect)

    def test_example5(self):
        command = ["LET A 1",
                   "GOSUB 5",
                   "PRINT A",
                   "END",
                   "LET A 3",
                   "RETURN",
                   "PRINT A",
                   "LET A 2",
                   "GOSUB -4",
                   "PRINT A",
                   "RETURN",
                   "."
                   ]
        self.stub_stdout()
        excute(command)
        expect = '1\n3\n3\n'
        self.assertEqual(sys.stdout.getvalue(), expect)


if __name__ == '__main__':
    unittest.main()
