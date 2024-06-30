from django.db.models import *

class Artist(Model):
    name = CharField(
        max_length=100,
        blank=False,
        null=False
    )
    

    def __str__(self):
        return self.name


class Song(Model):
    name=CharField(
        blank=True,
        null=True,
        max_length=50
    )
    img=ImageField(
        upload_to='musics/', 
        blank=True, 
        null=True
        )
    description = TextField(
        blank=True, 
        null=True,
        max_length=10000
        )
    file = FileField(
        upload_to='music/'
        )
    artist = ForeignKey(
        Artist, 
        on_delete=CASCADE,

    )
    def __str__(self):
        return self.name