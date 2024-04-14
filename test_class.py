import pytest
from .nw import nw_align

g = -1
mm = -1
m = 1

def test_init():
    nw_obj = nw_align(g,mm,m)
    assert nw_obj.gap == g
    assert nw_obj.mism == mm
    assert nw_obj.mats == m

def test_pass_strings():
    nw_obj = nw_align(g,mm,m)

    s1 = "AWD"
    s2 = "AWDWADAWDAWWDA"

    nw_obj.align(s1, s2)

    assert nw_obj.read == s1
    assert nw_obj.reference == s2


class Test_score():
    def test_empty_score(self):
        nw_obj = nw_align(g,mm,m)

        s1 = ""
        s2 = ""

        nw_obj.align(s1, s2)
        assert nw_obj.score_mat == [[0]]

    def test_score_1(self):
        nw_obj = nw_align(g,mm,m)
    
        s1 = "ACTG"
        s2 = "ACTG"
    
        nw_obj.align(s1, s2)
    
        score_mat = [
                [ 0, -1, -2, -3, -4],
                [-1,  1,  0, -1, -2],
                [-2,  0,  2,  1,  0],
                [-3, -1,  1,  3,  2],
                [-4, -2,  0,  2,  4],
                ]
        
        assert nw_obj.score_mat == score_mat
    
    def test_score_2(self):
        nw_obj = nw_align(g,mm,m)
    
        s1 = "ACTG"
        s2 = "ACT"
    
        nw_obj.align(s1, s2)
    
        score_mat = [
                [ 0, -1, -2, -3, -4],
                [-1,  1,  0, -1, -2],
                [-2,  0,  2,  1,  0],
                [-3, -1,  1,  3,  2],
                ]
        
        assert nw_obj.score_mat == score_mat
    
    def test_score_3(self):
        nw_obj = nw_align(g,mm,m)
    
        s1 = "AAC"
        s2 = "CTCA"
    
        nw_obj.align(s1, s2)
    
        score_mat = [
                [  0, -1, -2, -3],
                [ -1, -1, -2, -1],
                [ -2, -2, -2, -2],
                [ -3, -3, -3, -1],
                [ -4, -2, -2, -2],
                ]
        
        assert nw_obj.score_mat == score_mat
    
class Test_path():
    def test_empty_path(self):
        nw_obj = nw_align(g,mm,m)

        s1 = ""
        s2 = ""

        nw_obj.align(s1, s2)
        assert nw_obj.path_mat == [[[-1,-1]]]

    def test_path_1(self):
        nw_obj = nw_align(g,mm,m)
    
        s1 = "ACTG"
        s2 = "ACTG"
    
        nw_obj.align(s1, s2)
    
        path_mat = [
                [[-1, -1 ], [ 0, 0 ], [ 0, 1 ], [ 0, 2 ], [ 0, 3 ]],
                [[ 0,  0 ], [ 0, 0 ], [ 1, 1 ], [ 1, 2 ], [ 1, 3 ]],
                [[ 1,  0 ], [ 1, 1 ], [ 1, 1 ], [ 2, 2 ], [ 2, 3 ]],
                [[ 2,  0 ], [ 2, 1 ], [ 2, 2 ], [ 2, 2 ], [ 3, 3 ]],
                [[ 3,  0 ], [ 3, 1 ], [ 3, 2 ], [ 3, 3 ], [ 3, 3 ]],
                ]
        
        assert nw_obj.path_mat == path_mat

    @pytest.mark.skip(reason="it's temp")
    def test_path_2(self):
        nw_obj = nw_align(g,mm,m)
    
        s1 = "ACTG"
        s2 = "ACT"
    
        nw_obj.align(s1, s2)
    
        path_mat = [
                [[ -1, -1 ], [  0,  0 ],  [  0,  1 ],  [  0,  2 ],  [  0,  3 ]],
                [[  0,  0 ], [  0,  0 ],  [  0,  0 ],  [  0,  0 ],  [  0,  0 ]],
                [[  1,  0 ], [  0,  0 ],  [  0,  0 ],  [  0,  0 ],  [  0,  0 ]],
                [[  2,  0 ], [  0,  0 ],  [  0,  0 ],  [  0,  0 ],  [  0,  0 ]],
                ]
        
        assert nw_obj.path_mat == path_mat
