from django import forms
from django.contrib import messages
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from .. import models, tasks


class SolutionCreateForm(forms.ModelForm):
    """Represent solution form."""

    language = forms.ChoiceField(
        choices=models.constants.Languages.choices,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "language-select",
                "data-placeholder": "Select a tag",
            },
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "code-input",
                "rows": "10",
            },
        ),
    )

    class Meta:
        model = models.Solution
        fields = (
            "language",
            "content",
        )

    def __init__(
        self,
        issue: models.Issue,
        request: HttpRequest,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.issue = issue
        self.request = request

    def save(self, commit: bool = True) -> models.Solution:
        """Save this form's self.instance or return old one.

        Old instance will returned if it exists and has
        `PENDING` or `IN_PROGRESS` status, if there is no one, a new one will
        be created with started celery task that performs tests.

        """
        old_instance = models.Solution.objects.filter(
            user=self.request.user,
            issue=self.issue,
        ).first()
        if old_instance and old_instance.testing_status in (
            models.constants.SolutionStatus.PENDING,
            models.constants.SolutionStatus.IN_PROGRESS,
        ):
            messages.error(
                self.request,
                _(
                    "You have already submitted your solution for review. "
                    "Please wait for the test results.",
                ),
            )
            return old_instance
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.issue = self.issue
        if commit:
            instance.save()
            tasks.run_solution_tests.delay(solution_id=instance.id)
            messages.success(
                self.request,
                _("Your solution is sent successfully."),
            )
        return instance
