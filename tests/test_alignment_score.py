import unittest

from src import alignment


class TestAlignmentScore(unittest.TestCase):
    def test_alignment_0_0(self):
        self.assertEqual(alignment.align_score('', ''), 0)

    def test_alignment_0_1(self):
        self.assertEqual(alignment.align_score('', 'a'), -1)

    def test_alignment_1_0(self):
        self.assertEqual(alignment.align_score('a', ''), -1)

    def test_alignment_1_0_gex2(self):
        self.assertEqual(alignment.align_score('a', '', gap_extend=-2), -1)

    def test_alignment_1_0_gop5(self):
        self.assertEqual(alignment.align_score('a', '', gap_open=-5), -5)

    def test_alignment_0_1_gop5(self):
        self.assertEqual(alignment.align_score('', 'a', gap_open=-5), -5)

    def test_alignment_0_1_gex2(self):
        self.assertEqual(alignment.align_score('', 'a', gap_extend=-2), -1)

    def test_alignment_2_2_id(self):
        self.assertEqual(alignment.align_score('aa', 'aa'), 2)

    def test_alignment_2_2_1sub(self):
        self.assertEqual(alignment.align_score('ab', 'aa'), 0)

    def test_alignment_2_3_1del_1sub(self):
        self.assertEqual(alignment.align_score('abb', 'aa'), -1)

    def test_alignment_3_2_1ins_1sub(self):
        self.assertEqual(alignment.align_score('aa', 'abb'), -1)

    def test_alignment_3_3_1ins_1del(self):
        self.assertEqual(alignment.align_score('aab', 'aba'), 0)

    def test_alignment_7_3_4del(self):
        self.assertEqual(alignment.align_score('abbabba', 'aaa'), -1)

    def test_alignment_3_7_4ins(self):
        self.assertEqual(alignment.align_score('aaa', 'abbabba'), -1)

    def test_alignment_7_3_4del_1sub_gop5_gex2(self):
        self.assertEqual(alignment.align_score('abbabba', 'aaa', gap_extend=-2, gap_open=-5), -10)

    def test_alignment_7_3_4ins_1sub_gop5_gex2(self):
        self.assertEqual(alignment.align_score('aaa', 'abbabba', gap_extend=-2, gap_open=-5), -10)


if __name__ == '__main__':
    unittest.main()
