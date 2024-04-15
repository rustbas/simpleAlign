class nw_align():
    def __init__(self, g=-1, mm=-1, m=1):
        self.gap = g
        self.mism = mm
        self.mats = m

    def align(self, read, reference):
        self.read = read
        self.reference = reference

        self.read_len = len(self.read)
        self.reference_len = len(self.reference)


        if (self.read == "") and (self.reference == ""):
            self.score_mat = [[0]]
            self.path_mat = [[[-1,-1]]]
        else:
            self.score_mat = [[0 for j in range(self.read_len+1)] \
                    for i in range(self.reference_len+1)]
            self.path_mat = [[[0,0] for j in range(self.read_len+1)] \
                    for i in range(self.reference_len+1)]

        for i in range(self.reference_len + 1):
            self.score_mat[i][0] = -i

        for j in range(self.read_len + 1):
            self.score_mat[0][j] = -j

        self.path_mat[0][0] = [-1, -1]

        for i in range(1, self.reference_len + 1):
            self.path_mat[i][0] = [i-1, 0]

        for j in range(1, self.read_len + 1):
            self.path_mat[0][j] = [0, j-1]
        
        for i in range(1, self.reference_len + 1):
            for j in range(1, self.read_len + 1):
                d1 = self.score_mat[i-1][j-0] + self.gap
                d2 = self.score_mat[i-0][j-1] + self.gap
                
                if self.reference[i-1] == self.read[j-1]:
                    d4 = self.mats
                else:
                    d4 = self.mism

                d3 = self.score_mat[i-1][j-1] + d4

                if d1 > d2:
                    if d1 > d3:
                        self.score_mat[i][j] = d1
                        self.path_mat[i][j] = [i-1, j-0]
                    else:
                        self.score_mat[i][j] = d3
                        self.path_mat[i][j] = [i-1, j-1]
                else:
                    if d2 > d3:
                        self.score_mat[i][j] = d2
                        self.path_mat[i][j] = [i-0, j-1]
                    else:
                        self.score_mat[i][j] = d3
                        self.path_mat[i][j] = [i-1, j-1]

        self.curr_idx = [self.reference_len, self.read_len]
        self.alignment = self.restore_path()

    def restore_path(self):

        s1 = ""
        s2 = ""


        curr_idx = [self.reference_len, self.read_len]

        i = curr_idx[0]
        j = curr_idx[1]

        while curr_idx != [0, 0]:

            i = curr_idx[0]
            j = curr_idx[1]

            if (i - self.path_mat[i][j][0] == 1) and \
                    (j - self.path_mat[i][j][1] == 1):
                s1 += self.read[j-1]
                s2 += self.reference[i-1]
            elif (i - self.path_mat[i][j][0] == 0) and \
                    (j - self.path_mat[i][j][1] == 1):
                s1 += self.read[j-1]
                s2 += '-'
            elif (i - self.path_mat[i][j][0] == 1) and \
                    (j - self.path_mat[i][j][1] == 0):
                s1 += '-'
                s2 += self.reference[i-1]
            else:
                return s1 + "\n" + s2

            curr_idx = self.path_mat[i][j]

        return s1[::-1] + "\n" + s2[::-1]
