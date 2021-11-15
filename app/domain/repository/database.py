
import os
import boto3
import logging

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_paginator import Paginator

logger = logging.getLogger()

aws_session = boto3.session.Session()
region = aws_session.region_name

db_url = 'postgresql://{u}:{p}@{host}/{dbName}'
username_path = ''
password_path = ''
host_path = ''
db_name = 'db_name'

username_path = os.environ.get('username_path')
password_path = os.environ.get('password_path')
host_path = os.environ.get('host_path')
db_name = os.environ.get('db_name', '')

def get_ssm_value(obj):
    try:
        ssm = boto3.client('ssm', region_name=region)
        return ssm.get_parameter(Name=obj, WithDecryption=True)['Parameter']['Value']
    except Exception as err:
        logger.error(err)

user_name = get_ssm_value(username_path)
user_name = '' if user_name is None else user_name
password = get_ssm_value(password_path)
password = '' if password is None else password
db_host = get_ssm_value(host_path)
db_host = '' if db_host is None else db_host

db_url = db_url.replace('{u}', user_name).replace('{p}', password).replace('{host}', db_host).replace('{dbName}', db_name)

Base = declarative_base()


class Database():
    def __init__(self):
        try:
            logger.info('*** connecting to DB ***')
            self.engine = db.create_engine(db_url, pool_size=5, max_overflow=2, pool_pre_ping=True, pool_recycle=900)
            # create a configured "Session" class
            self.Session = sessionmaker(bind=self.engine)
            self.connection = self.engine.connect()
            logger.info("### DB Instance created ###")    
        except Exception as ex:
            logger.error(ex)
            raise Exception("Failed to connect DB: {0}".format(ex))

    def get_connection(self):
        return self.connection

    def get_session(self):
        self.validate_connection()
        logger.info("*** Session created ***")    
        return self.Session()

    def get_paginator(self, query, limit): 
        return Paginator(query, limit)

    def validate_connection(self):
        logger.info('*** connection.closed: ', self.connection.closed)
        if self.connection.closed:
            logging.info('*** DB connection closed. Recreating it ***')
            self.engine = db.create_engine(db_url, pool_size=5, max_overflow=2, pool_pre_ping=True, pool_recycle=900)
            self.connection = self.engine.connect()
            self.Session = sessionmaker(bind=self.engine)

