from django.db import models

class basketballPlayer(models.Model):
    # This lets us dictate that the field in the database willbe a string with a maximum length of 50 characters
    name = models.CharField(max_length=50)
    # This lets us dictate that the jersey_num field in our database will be an integer. (no floats allowed)
    jersey_num = models.IntegerField()
    # this lets us dictate that the height field in our database will be a decimal number.
    height = models.DecimalField(max_digits=3, decimal_places=2)
    # this lets us dictate that the retired field in our database will be a boolean (true or false)
    retired = models.BooleanField()
    # this lets us dictate that the first_game field in our database will be a datetime object
    first_game = models.DateField()
    # this lets us dictate that the bio field in our database will be a text field with however many characters we want
    bio = models.TextField()
    
    
    # THESE FIELDS SHOULD BE INCLUDED IN EVERY DATABASE MODEL THAT YOU CREATE
    #created_at is used to determine when something was actually first added to our database
    created_at = models.DateTimeField(auto_now_add = True)
    #updated_at is used to determine when something was last changed in the database
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"{self.id} - {self.name}"

