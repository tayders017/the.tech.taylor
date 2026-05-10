"""
==============================================================================
PARSING FAILED LOGON SECURITY EVENT SCRIPT
==============================================================================
PURPOSE: Parses a Windows Security.evtx file for Event ID 4625 (Failed Logon).
REQUIREMENTS: pip install python-evtx lxml
==============================================================================
"""

from Evtx.Evtx import Evtx

with Evtx("Security.evtx") as log:
    for record in log.records():
        if "4625" in record.xml():
            print(record.xml())
