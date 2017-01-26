import unittest

from src import alignment


class TestAlignment(unittest.TestCase):
    def test_alignment_0_0(self):
        self.assertEqual(alignment.align('', '', local=True), 0)

    def test_alignment_0_1(self):
        self.assertEqual(alignment.align('', 'a', local=True), 0)

    def test_alignment_1_0(self):
        self.assertEqual(alignment.align('a', '', local=True), 0)

    def test_alignment_1_0_gex2(self):
        self.assertEqual(alignment.align('a', '', local=True, gap_extend=-2), 0)

    def test_alignment_1_0_gop5(self):
        self.assertEqual(alignment.align('a', '', local=True, gap_open=-5), 0)

    def test_alignment_0_1_gop5(self):
        self.assertEqual(alignment.align('', 'a', local=True, gap_open=-5), 0)

    def test_alignment_0_1_gex2(self):
        self.assertEqual(alignment.align('', 'a', local=True, gap_extend=-2), 0)

    def test_alignment_2_2_id(self):
        self.assertEqual(alignment.align('aa', 'aa', local=True), 2)

    def test_alignment_2_2_1sub(self):
        self.assertEqual(alignment.align('ab', 'aa', local=True), 1)

    def test_alignment_2_3_1del_1sub(self):
        self.assertEqual(alignment.align('abb', 'aa', local=True), 1)

    def test_alignment_3_2_1ins_1sub(self):
        self.assertEqual(alignment.align('aa', 'abb', local=True), 1)

    def test_alignment_3_3_1ins_1del(self):
        self.assertEqual(alignment.align('aab', 'aba', local=True), 2)

    def test_alignment_7_3_4del(self):
        self.assertEqual(alignment.align('abbabba', 'aaa', local=True), 1)

    def test_alignment_3_7_4ins(self):
        self.assertEqual(alignment.align('aaa', 'abbabba', local=True), 1)

    def test_alignment_7_3_4del_1sub_gop5_gex2(self):
        self.assertEqual(alignment.align('abbabba', 'aaa', local=True, gap_extend=-2, gap_open=-5), 1)

    def test_alignment_7_3_4ins_1sub_gop5_gex2(self):
        self.assertEqual(alignment.align('aaa', 'abbabba', local=True, gap_extend=-2, gap_open=-5), 1)


if __name__ == '__main__':
    unittest.main()
