from django.core.exceptions import ValidationError
from django.forms import RadioSelect
from ja.models import JA
from multipageform.forms import MultipageForm, ChildForm


class JAForm(MultipageForm):
    model = JA
    starting_form = "Stage1Form"

    class Stage1Form(ChildForm):
        display_name = "Personal Info"
        required_fields = ["first_name", "last_name"]
        next_form_class = "Stage2Form"
        template_name = "ja/form_page.html"

        class Meta:
            fields = ["first_name", "middle_name", "last_name"]


    class Stage2Form(ChildForm):
        display_name = "Education"
        required_fields = "__all__"
        next_form_class = "Stage3Form"
        template_name = "ja/form_page.html"

        class Meta:
            fields = ["education_level", "year_graduated"]
            help_text = {
                "education_level": "Indicate the highest level of education you have attained"
            }

        def clean_year_graduated(self):
            year = self.cleaned_data.get("year_graduated")
            if not year.isnumeric() or len(year) < 4:
                raise ValidationError("Enter a four-digit number indicating the year in which you graduated.")
            return year


    class Stage3Form(ChildForm):
        display_name = "Experience"
        required_fields = ["prior_company", "prior_experience"]
        template_name = "ja/form_page.html"

        class Meta:
            fields = ["prior_company", "prior_experience", "anything_more"]
            help_texts = {
                "anything_more": "Indicate if you would like to add a personal statement"
            }
            labels = {
                "prior_experience": "Describe your duties",
                "anything_more": "Anything more?"
            }
            widgets = { "anything_more": RadioSelect(choices=[(True, "Yes"), (False, "No")]) }

        def get_next_form_class(self):
            if self.instance.anything_more:
                return "Stage3bForm"
            return "Stage4Form"


    class Stage3bForm(ChildForm):
        display_name = "Personal Statement"
        next_form_class = "Stage4Form"
        template_name = "ja/form_page.html"

        class Meta:
            fields = ["personal_statement"]


    class Stage4Form(ChildForm):
        required_fields = "__all__"
        template_name = "ja/form_page_w_summary.html"

        class Meta:
            fields = ["all_is_accurate"]
            labels = {"all_is_accurate": "Ready to submit to MegaCorp?"}