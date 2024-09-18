import sys
import os
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler,FunctionTransformer


from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass
@dataclass
class DataTransformationConfig:
    artifact_dir=os.path.join(artifact_folder)
    transform_train_file_path=os.path.join(artifact_dir,'train.npy')
    transform_test_file_path=os.path.join(artifact_dir,'test.npy')
    transform_object_file_path=os.path.join(artifact_dir,'preprocessor.pkl')


class DataTransformation:
    def __init__(self,feature_store_file_path):
        self.feature_store_file_path= feature_store_file_path

        self.data_transformation_config=DataTransformationConfig()

        self.utils=MainUtils()
    

    @staticmethod
    def get_data(feature_store_file_path:str)->pd.DataFrame:
        try:

            data=pd.read_csv(feature_store_file_path)

            data.rename(columns={"Good/Bad":TARGET_COLUMN},inplace=True)

            return data
        except Exception as e:
            raise CustomException(e,sys)
        

    def get_data_transformer_objects(self):

        try:

             imputer_step=('imputer',SimpleImputer(strategy='const',fill_value=0))

             scaler_step=('scaler',RobustScaler())

             preprocessor=Pipeline(
                 steps=[
                     imputer_step,
                     scaler_step
                 ]
             )

             return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    

    def initiated_data_transformation(self):
        logging.info("Entered initiated data transformation method of data transformation class")

        try:
            dataframe=self.get_data(feature_store_file_path=self.feature_store_file_path)

            x=dataframe.drop(columns=TARGET_COLUMN)
          #  y=np.where(dataframe[TARGET_COLUMN]=-1,0,1)
            y = np.where(dataframe[TARGET_COLUMN] == -1, 0, 1)
            
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

            preprocessor=self.get_data_transformer_object()

            x_train_scaled=preprocessor.fit_transform(x_train)
            x_test_scaled=preprocessor.transform(x_test)

            preprocessor_path=self.data_transformation_config.transformed_object_file_path
            os.makedirs(os.path.dirname(preprocessor_path),exist_ok=True)

            self.utils.save_object(file_path=preprocessor_path,obj=preprocessor)

            train_arr=np.c[x_train_scaled,np.array(y_train)]
            test_arr=np.c[x_test_scaled,np.array(y_test)]

            return (train_arr,test_arr,preprocessor_path)
        

        except Exception as e:
            raise CustomException(e,sys) from e