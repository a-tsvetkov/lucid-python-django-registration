from django.test import TestCase

import registration

from registration.tests.backends import *
from registration.tests.forms import *
from registration.tests.models import *
from registration.tests.views import *


class RegistrationVersionInfoTests(TestCase):
    """
    Test django-registration's internal version-reporting
    infrastructure.
    
    """
    def setUp(self):
        self.version = registration.VERSION

    def tearDown(self):
        registration.VERSION = self.version
    
