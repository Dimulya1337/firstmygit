from django.test import TestCase
from myapp.models import Animals








class AnimalsTestCase(TestCase):
    def setUp(self):
        Animals.objects.create(name="bird", action = "fly")
        Animals.objects.create(name="cat", action = "sleep")
    def test_animals_can_actions(self):
        bird = Animals.objects.get(name="bird")    
        cat = Animals.objects.get(name="cat")    
        self.assertEqual(bird.action('fly'))
        self.assertEqual(cat.action('sleep'))
# Create your tests here.
