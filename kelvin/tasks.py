from apscheduler.schedulers.background import BackgroundScheduler

def writeToSheet():
    print("Interfacing with Google Sheets")
    ## TODO: Iterate through database
    ## TODO: Check if PID exists on sheet
    ## TODO: If PID does not exist, add to write queue, then delete from database

    ## TODO: After iterating through all in database, write all information to sheet


scheduler = BackgroundScheduler()
scheduler.add_job(writeToSheet, 'interval', seconds=30)
scheduler.start()