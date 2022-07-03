from typing import Sequence
import django_tables2 as tables
from .models import Interview

class InterviewTable(tables.Table):
    class Meta:
        model = Interview
        template_name = "django_tables2/bootstrap-responsive.html"
        attrs = {"class": "table table-hoverable table-bordered"}
        
        sequence = ("heading", "type", "branch", "start_time", "end_time")
        exclude = ("link", "id", "event_id", "complete", "participant_1", "participant_2")
