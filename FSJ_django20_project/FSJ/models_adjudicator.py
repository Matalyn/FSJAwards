from django.db import modelsfrom .models_FSJUser import FSJUserclass Adjudicator(FSJUser):    def user_class(self):        return "Adjudicator"    