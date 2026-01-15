import os
import sys
import json

from dotenv import load_dotenv# for fetching env content here
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


#certify is used for telling mngodb that this is a valid certified http request 
import certifi
ca=certifi.where() #ca means certified authority for

import pandas as pd 
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():# for ETL pipeline 
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path): # to convert csv data into json
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)# droping index from dataset
            records=list(json.loads(data.T.to_json()).values())# converting data to json in form of list
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection): # for insrting json data  to mongodb 
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="ABHINAVAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH) 
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection) #inseerting in mognodb
    print(no_of_records)
        

