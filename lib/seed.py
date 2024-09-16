#!/usr/bin/env python3

from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dev.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create companies and devs
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Apple", founding_year=1976)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Give freebies
freebie1 = Freebie(item_name="Mug", value=5, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=15, dev=dev2, company=company2)

# Add and commit everything
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()

