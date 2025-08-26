from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models

# Sample models for demonstration (should be replaced with actual app models)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass'),
        ]

        # Create activities
        Activity.objects.create(user_email='spiderman@marvel.com', type='run', duration=30)
        Activity.objects.create(user_email='ironman@marvel.com', type='cycle', duration=45)
        Activity.objects.create(user_email='batman@dc.com', type='swim', duration=25)
        Activity.objects.create(user_email='wonderwoman@dc.com', type='yoga', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=85)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', difficulty='Medium')
        Workout.objects.create(name='Speed Run', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
