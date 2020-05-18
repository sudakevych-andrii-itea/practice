import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def setUp(self) -> None:
        self.args_results_list = (
            {
                'args': (1, 2, 3),
                'append_el': 10,
                'append_res': [1, 2, 3, 10],
                'pop_ind': None,
                'pop_res': [1, 2],
                'insert_ind_el': (1, 88),
                'insert_res': [1, 88, 2, 3],
                'remove_el': 3,
                'remove_res': [1, 2]
            },
            {
                'args': (5, 4, 3, 2, 1),
                'append_el': -33,
                'append_res': [5, 4, 3, 2, 1, -33],
                'pop_ind': 3,
                'pop_res': [5, 4, 3, 1],
                'insert_ind_el': (3, 55),
                'insert_res': [5, 4, 3, 55, 2, 1],
                'remove_el': 4,
                'remove_res': [5, 3, 2, 1]
            }

        )

    def test_append(self):
        for val in self.args_results_list:
            custom_list = CustomList(*val['args'])
            custom_list.append(val['append_el'])
            new_list = custom_list.get_list()
            self.assertEqual(new_list, val['append_res'])

    def test_pop(self):
        for val in self.args_results_list:
            custom_list = CustomList(*val['args'])
            custom_list.pop(val['pop_ind'])
            new_list = custom_list.get_list()
            self.assertEqual(new_list, val['pop_res'])

    def test_insert(self):
        for val in self.args_results_list:
            custom_list = CustomList(*val['args'])
            custom_list.insert(*val['insert_ind_el'])
            new_list = custom_list.get_list()
            self.assertEqual(new_list, val['insert_res'])

    def test_remove(self):
        for val in self.args_results_list:
            custom_list = CustomList(*val['args'])
            custom_list.remove(val['remove_el'])
            new_list = custom_list.get_list()
            self.assertEqual(new_list, val['remove_res'])

    def test_clear(self):
        custom_list = CustomList(1, 2, 3)
        custom_list.clear()
        new_list = custom_list.get_list()
        self.assertEqual(new_list, [])
