import unittest

from src import alignment


class TestAlignment(unittest.TestCase):
    def test_alignment_0_0(self):
        self.assertEqual(alignment.align('', ''), 0)

    def test_alignment_0_1(self):
        self.assertEqual(alignment.align('', 'a'), -1)

    def test_alignment_1_0(self):
        self.assertEqual(alignment.align('a', ''), -1)

    def test_alignment_1_0_gex2(self):
        self.assertEqual(alignment.align('a', '', gap_extend=-2), -1)

    def test_alignment_1_0_gop5(self):
        self.assertEqual(alignment.align('a', '', gap_open=-5), -5)

    def test_alignment_0_1_gop5(self):
        self.assertEqual(alignment.align('', 'a', gap_open=-5), -5)

    def test_alignment_0_1_gex2(self):
        self.assertEqual(alignment.align('', 'a', gap_extend=-2), -1)

    def test_alignment_2_2_id(self):
        self.assertEqual(alignment.align('aa', 'aa'), 2)

    def test_alignment_2_2_1sub(self):
        self.assertEqual(alignment.align('ab', 'aa'), 0)

    def test_alignment_2_3_1del_1sub(self):
        self.assertEqual(alignment.align('abb', 'aa'), -1)

    def test_alignment_3_2_1ins_1sub(self):
        self.assertEqual(alignment.align('aa', 'abb'), -1)

    def test_alignment_3_3_1ins_1del(self):
        self.assertEqual(alignment.align('aab', 'aba'), 0)

    def test_alignment_7_3_4del(self):
        self.assertEqual(alignment.align('abbabba', 'aaa'), -1)

    def test_alignment_3_7_4ins(self):
        self.assertEqual(alignment.align('aaa', 'abbabba'), -1)

    def test_alignment_7_3_4del_1sub_gop5_gex2(self):
        self.assertEqual(alignment.align('abbabba', 'aaa', gap_extend=-2, gap_open=-5), -10)

    def test_alignment_7_3_4ins_1sub_gop5_gex2(self):
        self.assertEqual(alignment.align('aaa', 'abbabba', gap_extend=-2, gap_open=-5), -10)


if __name__ == '__main__':
    unittest.main()
