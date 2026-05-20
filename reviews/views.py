from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from permissions import IsOwnerOrAdmin

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(ad=self.kwargs["ad_pk"])

    def get_permissions(self):
        if self.action == "list":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs["ad_pk"])
