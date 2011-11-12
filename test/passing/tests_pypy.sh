#!/bin/bash

the_python='./pypy'

$the_python test.py Connection && $the_python test.py uConnection && $the_python test.py Cursor && $the_python test.py uCursor && $the_python test.py StringVar && $the_python test.py uStringVar && $the_python test.py NumberVar && $the_python test.py uNumberVar && $the_python test.py LongVar && $the_python test.py uLongVar && $the_python test.py DateTimeVar && $the_python test.py uDateTimeVar && $the_python test.py LobVar && $the_python test.py uLobVar && $the_python test.py TimestampVar && $the_python test.py uTimestampVar && $the_python test.py UnicodeVar.py &&
 $the_python test.py IntervalVar && $the_python test.py uIntervalVar
