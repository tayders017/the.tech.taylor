from Evtx.Evtx import Evtx

with Evtx("Security.evtx") as log:
    for record in log.records():
        if "4625" in record.xml():
            print(record.xml())
