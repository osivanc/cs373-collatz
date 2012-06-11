#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 200)

    def test_read_2 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  201)
        self.assert_(a[1] == 210)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(10, 20)
        self.assert_(v == 21)

    def test_eval_3 (self) :
        v = collatz_eval(500, 1000)
        self.assert_(v == 179)



    # --------------------
    # collatz_cycle_length
    # --------------------

    def test_cycle_length_1 (self) :
        v = collatz_cycle_length(5)
        self.assert_(v == 6)

    def test_cycle_length_2 (self) :
        v = collatz_cycle_length(10)
        self.assert_(v == 7)

    def test_cycle_length_3 (self) :
        v = collatz_cycle_length(100)
        self.assert_(v == 26)
    
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 1000, 179)
        self.assert_(w.getvalue() == "100 1000 179\n")


    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

#    def test_solve_2 (self) :
#        r = StringIO.StringIO("59 10\n776 830\n0136 210\n1 1000\n")
#        w = StringIO.StringIO()
#        collatz_solve(r, w)
#        self.assert_(w.getvalue() == "59 10 113\n776 830 135\n0136 210 125\n1 1000 179\n")

#    def test_solve_3 (self) :
#        r = StringIO.StringIO("512 777\n7777 007\n210 210\n80085 10\n")
#        w = StringIO.StringIO()
#        collatz_solve(r, w)
#        self.assert_(w.getvalue() == "512 777 171\n7777 007 262\n210 210 40\n80085 10 351\n")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
