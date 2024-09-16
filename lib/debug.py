#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    session = sessionmaker(bind=engine)
    session = session()
    import ipdb; ipdb.set_trace()
