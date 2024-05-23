from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (
    EmbeddedDocumentField,
    ListField, 
    StringField,
    ReferenceField,
    BooleanField
    )


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)

class Contact(Document):
    fullname = StringField()
    email = StringField()
    is_sent = BooleanField()