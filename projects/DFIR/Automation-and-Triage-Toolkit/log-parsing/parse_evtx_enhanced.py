"""
==============================================================================
PARSING FAILED LOGON SECURITY EVENT SCRIPT
==============================================================================
PURPOSE: Parses a Windows Security.evtx file for Event ID 4625 (Failed Logon).
REQUIREMENTS: pip install python-evtx lxml
==============================================================================
"""

from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET

LOG_FILE = "Security.evtx"
TARGET_EVENT = "4625"

def parse_evtx(file_path):
    with Evtx(file_path) as log:
        # Header for console output
        print(f"{'Timestamp (UTC)':<30} | {'EventID':<8} | {'Target User'}")
        print("-" * 75)

        for record in log.records():
            # Convert record to XML and define namespace
            root = ET.fromstring(record.xml())
            ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}
            
            # Extract core metadata
            event_id = root.find('.//ns:EventID', ns).text
            
            if event_id == TARGET_EVENT:
                time_created = root.find('.//ns:TimeCreated', ns).get('SystemTime')
                
                # Extract specific logon data
                user_node = root.find(".//ns:Data[@Name='TargetUserName']", ns)
                username = user_node.text if user_node is not None else "N/A"
                
                print(f"{time_created:<30} | {event_id:<8} | {username}")

if __name__ == "__main__":
    parse_evtx(LOG_FILE)
