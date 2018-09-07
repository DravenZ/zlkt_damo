# encoding: utf-8

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# 数据库的配置
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_test'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_TEARDOWN = True
