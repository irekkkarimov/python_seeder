import math
import random

from faker import Faker
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String, Boolean, Date, Numeric, Float


def seed_employers():
    engine = create_engine('postgresql://testuser:test@localhost/db_2_1')
    connection = engine.connect()
    metadata = MetaData()
    faker = Faker()

    employers = Table('employers', metadata,
                      Column('name', String(length=50)),
                      Column('activity_id', Integer),
                      Column('address', String()),
                      Column('phone_number', String(length=50)))

    for _ in range(1001):
        data = {
            'name': faker.company(),
            'activity_id': math.floor(random.random() * 4 + 1),
            'address': faker.address(),
            'phone_number': faker.phone_number()
        }

        connection.execute(employers.insert().values(**data))
        connection.commit()


def seed_job_seekers():
    engine = create_engine('postgresql://testuser:test@localhost/db_2_1')
    connection = engine.connect()
    metadata = MetaData()
    faker = Faker()

    jobseekers = Table('jobseekers', metadata,
                       Column('first_name', String(length=50)),
                       Column('second_name', String(length=50)),
                       Column('middle_name', String(length=50)),
                       Column('qualification_id', Integer),
                       Column('profession_id', Integer),
                       Column('other', String()),
                       Column('salary', Float))

    for _ in range(1001):
        gender = random.choice(['male', 'female'])
        data = {
            'first_name': faker.first_name_male() if gender == 'male' else faker.first_name_female(),
            'second_name': faker.last_name(),
            'middle_name': faker.first_name_male() if gender == 'male' else faker.first_name_female(),
            'qualification_id': math.floor(random.random() * 4 + 1),
            'profession_id': math.floor(random.random() * 3 + 1),
            'other': faker.text(),
            'salary': math.floor(random.random() * 500000)
        }

        connection.execute(jobseekers.insert().values(**data))
        connection.commit()


def seed_deals():
    engine = create_engine('postgresql://testuser:test@localhost/db_2_1')
    connection = engine.connect()
    metadata = MetaData()
    faker = Faker()

    deals = Table('deals', metadata,
                  Column('employer_id', Integer),
                  Column('jobseeker_id', Integer),
                  Column('position_id', Integer),
                  Column('commission', Float))

    for _ in range(2001):
        data = {
            'employer_id': math.floor(random.random() * 999 + 1),
            'jobseeker_id': math.floor(random.random() * 999 + 1),
            'position_id': math.floor(random.random() * 4 + 1),
            'commission': math.floor(random.random() * 10000 + 1),
        }

        connection.execute(deals.insert().values(**data))
        connection.commit()


seed_deals()
