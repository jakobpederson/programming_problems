from unittest import TestCase

from problems.problem_8.solution.solution_problem_8 import encode_this_string


class Problem8Tests(TestCase):
    def test_encode_this_string_1(self):
        result = encode_this_string('aa')
        self.assertEqual(result, '2a')

    def test_encode_this_string_2(self):
        result = encode_this_string('aab')
        self.assertEqual(result, '2a1b')

    def test_encode_this_string_3(self):
        result = encode_this_string('aabc')
        self.assertEqual(result, '2a1b1c')

    def test_encode_this_string_4(self):
        result = encode_this_string('aabccccccabbc')
        self.assertEqual(result, '2a1b6c1a2b1c')
