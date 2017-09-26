# -*- coding: utf-8 -*-
import unittest
from  rome import add

class AdditionTest(unittest.TestCase):

    def test_add_Is(self):
        result = add('I', 'I')
        # assert result == 'II', 'add did not return II, it returned %s' % result
        self.assertEqual(add('I', 'I'), 'II', 'assert fail, it returned %s' % result)

    def test_inputs_out_of_scope_raise_exception(self):
        for bad_input in (2, None, 'C', 'D', 'L', 'M'):
            with self.assertRaises(ValueError) as m:
                add('I', bad_input)
                if not hasattr(m, 'exception'):
                    self.fail('%s as augend did not raise exception' % bad_input)
            with self.assertRaises(ValueError) as m:
                add(bad_input, 'I')
                if not hasattr(m, 'exception'):
                    self.fail('%s as addend did not raise exception' % bad_input)

    def test_IV_and_V(self):
        self.assertEqual(add('II', 'II'), 'IV')
        self.assertEqual(add('III', 'II'), 'V')
        self.assertEqual(add('IV', 'I'), 'V')
        self.assertEqual(add('I', 'V'), 'VI')

    def test_IX_and_X(self):
        self.assertEqual(add('V', 'V'), 'X')
        self.assertEqual(add('V', 'IV'), 'IX')
        self.assertEqual(add('VIII', 'I'), 'IX')
        self.assertEqual(add('IX', 'I'), 'X')
        self.assertEqual(add('X', 'I'), 'XI')
        self.assertEqual(add('I', 'X'), 'XI')
        self.assertEqual(add('X', 'V'), 'XV')
        self.assertEqual(add('V', 'X'), 'XV')
        self.assertEqual(add('X', 'X'), 'XX')


if __name__ == '__main__':
    unittest.main()
