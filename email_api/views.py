from rest_framework import generics, status
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer


class EmailCreateView(generics.CreateAPIView):
    """
    A simple View for creating emails.
    """
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Hooray! Your email was created successfully!', 'email': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailListView(generics.ListAPIView):
    """
    A simple View for viewing all emails.
    """
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'message': 'Here are all the emails, enjoy!',
            'emails': response.data
        }
        return response
