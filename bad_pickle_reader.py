#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# December 2016
"""Read an exploited pickle."""

import pickle

with open("output.pickle", "rb") as f:
    pickle.load(f)
    f.close()
