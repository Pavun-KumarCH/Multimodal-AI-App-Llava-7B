import datetime

def writehistory(text):
    tstamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    logfile = f"log_{tstamp}.txt"
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(text + "\n")
