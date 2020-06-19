import os
import itertools

from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''
    Configuration variables for server application.
    '''
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class AutoDatabase(object):

    def __init__(self, search_variables):
        '''
        :param search_variables: The variables to be searched in the database.
        :type search_variables: **list**
        '''
        self.search_variables = search_variables


    def get_database_info(self):
        '''
        Get the information from a PostgreSQL database, from an URI: postgresql://user:password@ip-address:port/table-name.
        And returns a dict with the result of the searched variables.
        
        :return: A dict containing a list for each searched column in the database.
        :rtype: **dict**
        '''
        Session = sessionmaker(create_engine(Config.SQLALCHEMY_DATABASE_URI))
        session = Session()
        data = {}
        try:
            # pylint: disable=maybe-no-member
            if 'acceleration' in self.search_variables:
                data['acceleration'] = list(itertools.chain.from_iterable(session.query(Auto.acceleration))) 
    
            if 'cilinders' in self.search_variables:
                data['cilinders'] = list(itertools.chain.from_iterable(session.query(Auto.cilinders)))

            if 'displacement' in self.search_variables:
                data['displacement'] = list(itertools.chain.from_iterable(session.query(Auto.displacement)))

            if 'horsepower' in self.search_variables:
                data['horsepower'] = list(itertools.chain.from_iterable(session.query(Auto.horsepower)))

            if 'model_year' in self.search_variables:
                data['model_year'] = list(itertools.chain.from_iterable(session.query(Auto.model_year)))

            if 'weight' in self.search_variables:
                data['weight'] = list(itertools.chain.from_iterable(session.query(Auto.weight)))

            if 'mpg' in self.search_variables:
                data['mpg'] = list(itertools.chain.from_iterable(session.query(Auto.mpg)))
 
        except TypeError:
            raise 'Error. Not able to get information from the database.'

        return data

class Auto(declarative_base()):
    '''
    Table model for the auto table in the database. Because there is no primary key,
    it was seted one as a workaround for sqlalchemy lib.
    '''
    __tablename__ = 'auto'
    
    acceleration = Column(Float, primary_key=True)
    cilinders = Column(Integer)
    displacement = Column(Float)
    horsepower = Column(Integer)
    model_year = Column(Integer)
    weight = Column(Integer)
    mpg = Column(Float)
