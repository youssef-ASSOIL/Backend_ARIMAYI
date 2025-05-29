from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CandidateProfile
from .serializers import CandidateProfileSerializer
from .permissions import IsCandidate, IsRecruiter

class CandidateProfileViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CandidateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'CANDIDATE':
            return CandidateProfile.objects.filter(user=self.request.user)
        return CandidateProfile.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticated(), IsCandidate()]
        elif self.action in ['list', 'retrieve']:
            return [IsAuthenticated(), IsRecruiter()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
