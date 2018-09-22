
# Domain
from domain.models import Stamp, Member

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.custom_permissions import IsGetOrIsAuthenticated
from rest_framework import status

# Serializers
from api.serializers import StampSerializer


class StampAPIView(APIView):

    permission_classes = (IsGetOrIsAuthenticated,)

    def get_object(self, pk):
        try:
            return Stamp.objects.get(pk=pk)
        except Stamp.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """" GET /api/v1/stamps/<id>

        Retrieves a stamp by the specified id
        """
        stamp = self.get_object(pk=id)
        serializer = StampSerializer(stamp)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        """" POST /api/v1/stamps

        Creates a stamp with the specified body
        """
        serializer = StampSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        """" PUT /api/v1/stamps/<id>

        Edits an stamp information
        """
        stamp = self.get_object(pk=id)
        serializer = StampSerializer(stamp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id, format=None):
        """" DELETE /api/v1/stamps/<id>

            Deletes a specified stamp
        """
        stamp = self.get_object(pk=id)
        serializer = StampSerializer(stamp)
        serializer.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class StampMemberAPIView(APIView):

    permission_classes = (IsGetOrIsAuthenticated,)

    def get_member_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, member_id, format=None):
        """" GET /api/v1/stamps/member/<member_id>

             Returns stamps related to a specific member
        """
        member = self.get_member_object(pk=member_id)
        serializer = StampSerializer(member.stamps, many=True)
        return Response(serializer.data)
