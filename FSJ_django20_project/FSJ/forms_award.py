from django.forms import *
from django.utils.translation import gettext_lazy as _

class AddAwardForm(forms.Form):
		award_name = CharField(label = _("Award Name"))
		description = CharField(label = _("Description"), widget = Textarea)
		value = IntegerField(label = _("Value"))
		programs = CharField(label = _("Programs"), widget = Textarea)
		OPTIONS = (
			(1, "First"),
			(2, "Second"),
			(3, "Third"),
			(4, "Fourth"),
			(5, "Fifth"),
			)
		years_of_study = MultipleChoiceField(label = _("Years of Study"), widget=CheckboxSelectMultiple, choices=OPTIONS)
		deadline = DateField(label = _("Deadline"), widget=DateInput())
		TRUE_FALSE_CHOICES = (
			(True, 'Yes'),
			(False, 'No')
			)
		documents_needed = ChoiceField(label = _("Documents Needed"), widget = Select(), choices = TRUE_FALSE_CHOICES)
		is_active = ChoiceField(label = _("Is Active"), widget = Select(), choices = TRUE_FALSE_CHOICES)