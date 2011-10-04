#!/usr/bin/env python
'''
$Id: test_gadfly_dbapi20.py,v 1.9 2005/05/18 04:07:44 zenzen Exp $
'''

__rcs_id__  = '$Id: test_gadfly_dbapi20.py,v 1.9 2005/05/18 04:07:44 zenzen Exp $'
__version__ = '$Revision: 1.9 $'[11:-2]
__author__ = 'Stuart Bishop <zen@shangri-la.dropbear.id.au>'

import unittest
import shutil
import os
import os.path
import gadfly.dbapi20
import dbapi20

#dbdir = os.path.abspath(os.path.join(os.path.dirname(__file__),'_db_dir'))
dbdir = os.path.abspath(os.path.join(".",'_db_dir'))

class test_GadflyDBAPI20(dbapi20.DatabaseAPI20Test):
    driver = gadfly.dbapi20
    connect_kw_args = {'databasename': 'test', 'directory': dbdir}

    def setUp(self):
        if os.path.exists(dbdir):
            shutil.rmtree(dbdir)
        os.makedirs(dbdir)
        g = gadfly.gadfly()
        g.startup(self.connect_kw_args['databasename'],
                  self.connect_kw_args['directory'])
        c = g.cursor()
        c.execute("select * from __table_names__")
        c.execute("create table ph (nm varchar, ph varchar)")
        g.commit()

    def tearDown(self):
        if os.path.exists(dbdir):
            shutil.rmtree(dbdir)

    def test_None(self):
        # gadfly parser does'nt understand NULL
        pass

    def test_description(self):
        # only when the select-execute return an result, the types of the 
        # description can determinat (see: gadfly/database.py line 390 ...)
        pass
            
    def test_callproc(self): pass
    def test_nextset(self): pass
    def test_setoutputsize(self): pass

    def test_ISO8601(self):
        self.failUnlessEqual(str(gadfly.Date(1234,12,21)), '1234-12-21')
        self.failUnlessEqual(str(gadfly.Date(34,2,4)), '0034-02-04')
        self.failUnlessEqual(str(gadfly.Time(00,01,02)), '00:01:02')
        self.failUnlessEqual(str(gadfly.Time(24,01,02)), '24:01:02')
        self.failUnlessEqual(
                str(gadfly.Timestamp(1234,12,21,00,01,02)),
                '1234-12-21 00:01:02'
                )
        self.failUnlessEqual(
            str(gadfly.Timestamp(34,2,4,24,01,02)),
            '0034-02-04 24:01:02'
            )

        # Add 8 hours, 21 mins and 2 secs as midnight isn't a good test
        groundhog_day = 1044144000 + 8*60*60 + 21*60 + 2
        self.failUnlessEqual(
                str(gadfly.DateFromTicks(groundhog_day)), '2003-02-02'
                )
        self.failUnlessEqual(
                str(gadfly.TimeFromTicks(groundhog_day)), '08:21:02'
                )
        self.failUnlessEqual(
                str(gadfly.TimestampFromTicks(groundhog_day)),
                '2003-02-02 08:21:02'
                )

def suite():
    return unittest.makeSuite(test_GadflyDBAPI20)

if __name__ == '__main__':
    unittest.main()
