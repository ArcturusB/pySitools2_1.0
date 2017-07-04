#! /usr/bin/env python3

from datetime import datetime, timedelta
import sys

import sitools2.clients.sdo_client_medoc as md

class nostdout(object):
    ''' Context manager to silent output. '''
    class DummyFile(object):
        def write(self, x): pass
        def flush(self, x): pass
    def __enter__(self):
        sys.stdout = nostdout.DummyFile()
    def __exit__(self, type, value, traceback):
        sys.stdout = sys.__stdout__

d1 = datetime(2016, 6, 1, 5, 0, 0)
d2 = datetime(2016, 6, 1, 10, 12, 0)

with nostdout():
    sdo_data_list = md.media_search(
        DATES=[d1, d2],
        WAVES=['335', '304'],
        CADENCE=['1m'],
        nb_res_max=10,
        server='http://idoc-medoc-test.ias.u-psud.fr')
