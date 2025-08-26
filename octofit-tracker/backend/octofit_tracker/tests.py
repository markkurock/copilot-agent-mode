from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')

class TeamTestCase(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityTestCase(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', type='run', duration=30)
        self.assertEqual(activity.type, 'run')

class LeaderboardTestCase(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutTestCase(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
