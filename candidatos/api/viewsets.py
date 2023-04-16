from rest_framework.viewsets import ModelViewSet
from .serializers import CandidateSerializer, ReportSerializer
from django.core.exceptions import ValidationError
from ..models import Candidate
from rest_framework.decorators import action
from rest_framework import generics, response, status

class CandidateViewSet(ModelViewSet):

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, url_path='vote/(?P<candidate_id>[^/.]+)')
    def vote(self, request, *args, **kwargs):
        try: 
            candidate = Candidate.objects.get(id=self.kwargs['candidate_id'])
            candidate.votes += 1
            candidate.save()
            return response.Response("Voto registrado", status=status.HTTP_200_OK, )
        except Candidate.DoesNotExist:
            return response.Response({"Error": "Candidate not found."}, status=status.HTTP_400_BAD_REQUEST)
        
class GenerateReport(generics.ListAPIView):
    serializer_class = ReportSerializer
    queryset = Candidate.objects.all()

