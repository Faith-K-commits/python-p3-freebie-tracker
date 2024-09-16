from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    dev = relationship('Dev', backref=backref('freebies', lazy=True))
    company = relationship('Company', backref=backref('freebies', lazy=True))

    def __repr__(self):
        return f'<Freebie {self.item_name}>'

# Update Company class
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def give_freebie(self, dev, item_name, value):
        '''Creates a new Freebie for the company'''
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        return new_freebie

    @classmethod
    def oldest_company(cls, session):
        '''Returns the Company instance with the earliest founding year'''
        return session.query(cls).order_by(cls.founding_year).first()

    def __repr__(self):
        return f'<Company {self.name}>'

# Update Dev class
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def received_one(self, item_name):
        '''Returns True if the dev has a Freebie with the given item_name'''
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        '''Transfers ownership of a freebie to another dev if the freebie belongs to this dev'''
        if freebie in self.freebies:
            freebie.dev = dev
            return True
        return False

    def __repr__(self):
        return f'<Dev {self.name}>'
