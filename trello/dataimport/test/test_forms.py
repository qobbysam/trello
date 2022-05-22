from django.test import TestCase

from ..forms import UserHandInputForm

class UserHandInputFormTest(TestCase):

    def test_age_field_label(self):
        form = UserHandInputForm()

        self.assertTrue(form.fields['age'].label is None or form.fields['age'].label == 'age')
