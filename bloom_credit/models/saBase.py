# # -*- coding: utf-8 -*-

#################
#### imports ####
#################

from ..extensions import db

#################
#### models ####
#################


class Base(db.Model):

    __abstract__ = True

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    @classmethod
    def get_where_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_where(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    # We will also proxy Flask-SqlAlchemy's get_or_44
    # for symmetry
    @classmethod
    def get_or_404(cls, id):
        return cls.query.get_or_404(id)

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        db.session.flush()
        if commit:
            db.session.commit()
        return self

    def __str__(self):

        dictOfAttributes = self.__dict__

        return "<%s %r>" % (self.__class__.__name__, dictOfAttributes)

    def __repr__(self):
        return self.__str__()
