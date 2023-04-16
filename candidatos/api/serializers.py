from rest_framework.serializers import ModelSerializer
from ..models import Candidate

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id','number','name')

class ReportSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('number','name','votes')