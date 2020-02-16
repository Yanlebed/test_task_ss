from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from charts.models import Rate
from charts.serializers import RateSerializer


class HomePageView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


class ChartData(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Rate.objects.all()

    def get(self, request):
        dates = self.queryset.values_list('date').order_by('date')
        amount = self.queryset.values_list('amount')
        data = {"dates": dates, "amount": amount}
        return Response(data)


class RateAdd(generics.CreateAPIView):
    # Create a new rate
    serializer_class = RateSerializer
    permission_classes = []

    def get(self, request):
        return Response('Please put your rate in the fields below')

    def post(self, request, *args, **kwargs):
        data = request.data
        if Rate.objects.filter(date=data['date']).exists():
            return Response("Rate with such date already exists",
                            status=status.HTTP_400_BAD_REQUEST)
        rate = Rate.objects.create(
            amount=data['amount'],
            date=data['date']
        )
        rate.save()
        return Response("Rate is successfully created", status=status.HTTP_201_CREATED)