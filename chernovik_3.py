from apscheduler.schedulers.blocking import BlockingScheduler

def task():
    # Define the task you want to run here
    pass

scheduler = BlockingScheduler()
scheduler.add_job(task, 'interval', minutes=1)
scheduler.start()
