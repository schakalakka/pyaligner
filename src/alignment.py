import numpy as np


class Alignment:
    def __init__(self, a: str, b: str, match=1, mismatch=-1, gap_open=-1, gap_extend=-1, top=False, left=False,
                 right=False, bottom=False, lower_diagonal=None, upper_diagonal=None, local=False,
                 print_alignment=False):
        """

        :param a: first string
        :param b: second string
        :param match: match score
        :param mismatch: mismatch score
        :param gap_open: opening gap penalty
        :param gap_extend: extending gap penalty
        :param top: if True no leading gap costs for the second string b
        :param left: if True no leading gap costs for the first string a
        :param right: if True no trailing gap costs for b
        :param bottom: if True no trailing gap costs for a
        :param lower_diagonal: lower diagonal limit for banded alignment
        :param upper_diagonal: upper diagonal limit for banded alignment
        :param local: if True compute local alignment
        :param print_alignment: if True print alignment with score
        """
        self.a = a
        self.b = b

        self.match = match
        self.mismatch = mismatch
        self.gap_open = gap_open
        self.gap_extend = gap_extend
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom
        self.lower_diagonal = lower_diagonal
        self.upper_diagonal = upper_diagonal
        self.local = local
        self.print = print_alignment

        self.score = None
        self.result_row = None
        self.result_col = None
        self.result_spec = None
        self.score_matrix = None
        self.trace_matrix = None
        self.aligned_a = None
        self.aligned_b = None
        self.middle_string = None

    def align(self):
        """
        Computes the alignment score of two strings. A traceback matrix is also computed for an optional output of the
        aligned strings.
        """
        a = self.a
        b = self.b
        numpy_type = np.int32
        min_val = np.iinfo(numpy_type).min  # like -infinity
        # m[][][0] alignment matrix
        # m[][][1] deletion matrix
        # m[][][2] insertion matrix
        m = np.zeros((len(a) + 1, len(b) + 1, 3), dtype=numpy_type)
        self.trace_matrix = np.zeros((len(a) + 1, len(b) + 1, 3), dtype=np.int8)

        gap_open = self.gap_open
        gap_extend = self.gap_extend
        match = self.match
        mismatch = self.mismatch

        # initialize first row and column
        for i in range(1, len(a) + 1):
            m[i][0][0] = m[i][0][2] = min_val
            m[i][0][1] = gap_open + (i - 1) * gap_extend if not self.left else 0
            self.trace_matrix[i][0] = [1, 1, 1]

        for j in range(1, len(b) + 1):
            m[0][j][0] = m[0][j][1] = min_val
            m[0][j][2] = gap_open + (j - 1) * gap_extend if not self.top else 0
            self.trace_matrix[0][j] = [2, 2, 2]

        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                current_score = match if a[i - 1] == b[j - 1] else mismatch
                m[i, j, 0] = m[i - 1, j - 1].max() + current_score
                m[i, j, 1] = max(m[i - 1, j][0] + gap_open, m[i - 1, j][1] + gap_extend, m[i - 1, j][2] + gap_open)
                m[i, j, 2] = max(m[i, j - 1][0] + gap_open, m[i, j - 1][1] + gap_open, m[i, j - 1][2] + gap_extend)
                self.trace_matrix[i, j][0] = m[i - 1, j - 1].argmax()
                self.trace_matrix[i, j][1] = np.array(
                    [m[i - 1, j][0] + gap_open, m[i - 1, j][1] + gap_extend, m[i - 1, j][2] + gap_open]).argmax()
                self.trace_matrix[i, j][2] = np.array(
                    [m[i, j - 1][0] + gap_open, m[i, j - 1][1] + gap_open, m[i, j - 1][2] + gap_extend]).argmax()
        self.score = m[len(a), len(b)].max()
        self.result_row = len(a)
        self.result_col = len(b)
        if self.right:
            max_elem_in_last_col = m.max(axis=2).max(axis=0)[len(b)]
            if self.score < max_elem_in_last_col:
                self.score = max_elem_in_last_col
                self.result_row = m.max(axis=2).argmax(axis=0)[len(b)]
                self.result_col = len(b)
        if self.bottom:
            max_elem_in_last_row = m.max(axis=2).max(axis=1)[len(a)]
            if self.score < max_elem_in_last_row:
                self.score = max_elem_in_last_row
                self.result_col = m.max(axis=2).argmax(axis=1)[len(a)]
                self.result_row = len(a)
        self.result_spec = m[self.result_row, self.result_col].argmax()

        self.score_matrix = m

    def get_score(self) -> int:
        """
        Returns the alignment score if the alignment is already computed.
        :return: alignment score
        """
        return self.score

    def traceback(self) -> None:
        """
        Traceback step for obtaining the alignments.
        :return:
        """
        a = self.a
        b = self.b
        row = self.result_row
        col = self.result_col
        spec = self.result_spec
        trace = self.trace_matrix
        aligned_a = aligned_b = middle_string = ''  # aligned strings of a nd b
        if row < len(a):
            aligned_a = a[row:]
            middle_string = (len(a) - row) * ' '
            aligned_b = (len(a) - row) * '-'
        if col < len(b):
            aligned_b = b[col:]
            aligned_a = (len(b) - col) * '-'
            middle_string = (len(b) - col) * ' '
        while row > 0 or col > 0:
            new_spec = trace[row][col][spec]
            if spec == 0:
                row -= 1
                col -= 1
                aligned_a = a[row] + aligned_a
                aligned_b = b[col] + aligned_b
                middle_string = '|' + middle_string if a[row] == b[col] else ' ' + middle_string
            elif spec == 1:
                row -= 1
                aligned_a = a[row] + aligned_a
                aligned_b = '-' + aligned_b
                middle_string = ' ' + middle_string
            elif spec == 2:
                col -= 1
                aligned_a = '-' + aligned_a
                aligned_b = b[col] + aligned_b
                middle_string = ' ' + middle_string
            spec = new_spec
        self.aligned_a = aligned_a
        self.aligned_b = aligned_b
        self.middle_string = middle_string

    def print_alignment(self) -> None:
        """
        Prints the alignment to the console.
        :return:
        """
        print('Score: {}'.format(self.score))
        print(self.aligned_a)
        print(self.middle_string)
        print(self.aligned_b)

    def align_score(self):
        a = self.a
        b = self.b
        m = np.zeros((len(b) + 1, 2), dtype=np.int32)

        g = self.gap_open
        h = self.gap_extend
        match = self.match
        mismatch = self.mismatch

        t = g

        for j in range(1, len(b) + 1):
            t += h
            m[j][0] = t
            m[j][1] = t + g

        t = g
        for i in range(1, len(a) + 1):
            s = m[0][0]
            t += h
            c = t
            m[0][0] = c
            e = t + g
            for j in range(1, len(b) + 1):
                e = max(e, c + g) + h
                m[j][1] = max(m[j][1], m[j][0] + g) + h
                w = match if a[i - 1] == b[j - 1] else mismatch
                c = max(m[j][1], e, s + w)
                s = m[j][0]
                m[j][0] = c

        self.score = m[len(b)][0]


def align(a: str, b: str, match=1, mismatch=-1, gap_open=-1, gap_extend=-1, top=False, left=False,
          right=False, bottom=False, lower_diagonal=None, upper_diagonal=None, local=False,
          print_alignment=False):
    align_obj = Alignment(a, b, match, mismatch, gap_open, gap_extend, top, left, right, bottom, lower_diagonal,
                          upper_diagonal, local, print_alignment)
    align_obj.align()
    if align_obj.print:
        align_obj.traceback()
        align_obj.print_alignment()
    return align_obj.get_score()


def align_score(a: str, b: str, match=1, mismatch=-1, gap_open=-1, gap_extend=-1, top=False, left=False,
                right=False, bottom=False, lower_diagonal=None, upper_diagonal=None, local=False,
                print_alignment=False):
    align_obj = Alignment(a, b, match, mismatch, gap_open, gap_extend, top, left, right, bottom, lower_diagonal,
                          upper_diagonal, local, print_alignment)
    align_obj.align_score()
    if align_obj.print:
        print(f'Score: {align_obj.score}')
    return align_obj.get_score()
