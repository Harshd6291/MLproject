import os
import sys
from src.expcetion import CustomException 
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts', "tain.csv")
    test_data_path:str=os.path.join('artifacts', "test.csv")
    raw_data_path:str=os.path.join('artifacts', "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_cofig= DataIngestionConfig()
    def intiate_data_ingestion(self):
        logging.info("enter the data ingestion method or component ")
        try:
            df= pd.read_csv(r'notebook\data\StudentsPerformance.csv')
            logging.info('read the dataset as dataframe')    #can use api key  tooo
            os.makedirs(os.path.dirname(self.ingestion_cofig.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_cofig.raw_data_path,index=False,header=True)

            logging.info('train test split initiates')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_cofig.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_cofig.test_data_path, index=False, header= True)

            logging.info('ingestion of data is completed')

            return(
                self.ingestion_cofig.train_data_path,
                self.ingestion_cofig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

# Initiate all these 
if __name__=="__main__":
    obj= DataIngestion()
    obj.intiate_data_ingestion()