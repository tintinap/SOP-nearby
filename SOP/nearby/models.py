# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Place(models.Model):
    idplace = models.AutoField(db_column='idPlace', primary_key=True)  # Field name made lowercase.
    place_name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True,null=True)
    class Meta:
        # managed = False
        db_table = 'Place'


class PlaceUser(models.Model):
    placeuser_id = models.AutoField(db_column='placeuser_id', primary_key=True)
    place_idplace = models.ForeignKey(Place, models.DO_NOTHING, db_column='Place_idPlace')  # Field name made lowercase.
    user_iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.
    avg_spending_time = models.FloatField(blank=True, null=True)
    visit_count = models.IntegerField(blank=True, null=True)
    ranking = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Place_User'
        unique_together = (('place_idplace', 'user_iduser'),)


class Tag(models.Model):
    idtag = models.AutoField(db_column='idTag', primary_key=True)  # Field name made lowercase.
    tag_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Tag'


class TagPlace(models.Model):
    tag_idtag = models.ForeignKey(Tag, models.DO_NOTHING, db_column='Tag_idTag', primary_key=True)  # Field name made lowercase.
    place_idplace = models.ForeignKey(Place, models.DO_NOTHING, db_column='Place_idPlace')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Tag_place'
        unique_together = (('tag_idtag', 'place_idplace'),)


class User(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'User'