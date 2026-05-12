from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import sys
import os
from dotenv import load_dotenv

load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ml')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../etl')))

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from ml.train import train


def run_etl():

    print("ETL started..")
    df=extract_data()
    df=transform_data(df)
    load_data(df)
    print("ETL completed")


def run_training():

    print("Training started..")
    train()
    print("Training completed")



def run_pipeline():
    print("Pipeline started ")
    train()
    print("Pipeline completed")

if __name__=="__main__":

    scheduler=BlockingScheduler()
    scheduler.add_job(
        run_pipeline,
        CronTrigger(hour=2,minute=0),
        id='retrain_job',
        name='ETL + Retrain Job',
        replace_existing=True

    ) 
    print("Scheduler started = pipeline will run daily at 2:00 AM")

    try:
        scheduler.start()
    except(KeyboardInterrupt,SystemExit):
        print("Scheduler stopped")      

        