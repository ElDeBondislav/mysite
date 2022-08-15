from sqlalchemy import *
from database import *
import json


def updateData(session, dbType, obj):
    session.query(dbType).delete()
    db = dbType()
    db.data = obj.toJSON()
    session.add(db)
    session.commit()


class AllowedContainerDB(Base):
    __tablename__ = 'allowedusers_v1'
    id = Column('id', Integer, primary_key=True)
    data = Column('data', String)


class InstaContainerDB(Base):
    __tablename__ = 'instaContainer_v1'
    id = Column('id', Integer, primary_key=True)
    data = Column('data', String)


class AllowedUser(object):
    def __init__(self, id='', currentPage=1):
        self.id = id
        self.currentPage = currentPage


class InstModel(object):
    __tablename__ = 'instModels_v1'

    def __init__(self, name='', wrongPass=[], correctPass=[]):
        self.wrongPass = []
        self.correctPass = []

    def toStr(self):
        reply = list()
        reply.append('Вірні паролі (%d): ' % len(self.correctPass))
        reply.append('[')
        for password in self.correctPass:
            reply.append("      %s" % password)
        reply.append(']')
        reply.append('Ймовірні паролі (%d): ' % len(self.wrongPass))
        reply.append('[')
        for password in self.wrongPass:
            reply.append("      %s" % password)
        reply.append(']')
        return "\n".join(reply)+"\n"


class InstContainer(object):
    def __init__(self, *args, models={}):
        self.models = models

    def add(self, model):
        self.models.append(model)

    def findByName(self, name):
        counter = 0
        for model in self.models:
            if model['name'] == name:
                return counter
            counter = counter + 1
        return -1

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class AllowedContainer(object):
    def __init__(self, *args, models={}):
        self.models = models

    def findById(self, id):
        counter = 0
        for model in self.models:
            if model['id'] == id:
                return counter
            counter = counter + 1
        return -1

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# session.query(InstaContainerDB).delete()
# session.commit()
instaContainerData = session.query(InstaContainerDB).all()
if len(instaContainerData) == 0:
    instContainerDB = InstaContainerDB()
    instContainerDB.data = InstContainer().toJSON()
    session.add(instContainerDB)
    session.commit()
    instaContainerData = session.query(InstaContainerDB).all()

instaContainer = InstContainer()
instaContainer.models = json.loads(instaContainerData[0].data)['models']
for model in instaContainer.models:
    instModel = InstModel(model)
    instModel.wrongPass = instaContainer.models[model]['wrongPass']
    instModel.correctPass = instaContainer.models[model]['correctPass']
    instaContainer.models[model] = instModel

allowedUsersContainerData = session.query(AllowedContainerDB).all()
if len(allowedUsersContainerData) == 0:
    allowedContainerDB = AllowedContainerDB()
    allowedContainerDB.data = AllowedContainer().toJSON()
    session.add(allowedContainerDB)
    session.commit()
    allowedUsersContainerData = session.query(AllowedContainerDB).all()

allowedContainer = AllowedContainer()
allowedContainer.models = json.loads(allowedUsersContainerData[0].data)['models']
# allowedContainer.models['1395337113'] = AllowedUser('1395337113')

for model in allowedContainer.models:
    allowedContainer.models[model] = AllowedUser(allowedContainer.models[model]['id'],
                                                 allowedContainer.models[model]['currentPage'])

session.close()
