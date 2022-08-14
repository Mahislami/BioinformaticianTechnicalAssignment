from http.client import HTTPResponse
import json
from django.http import JsonResponse
from django.shortcuts import render
from core.models.Protein import Protein
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models.serializers import FileUploadSerializer, ProteinSerializer
from rest_framework.response import Response

def home(request):
    return

class UploadFileView(generics.CreateAPIView):
    
    serializer_class = FileUploadSerializer
    
    def create(self, request, *args, **kwargs):
        proteins = []
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            protein = Protein(  ProteinID = row[0],
                                Accessoin = row[1],
                                AverageMass= row[2],
                                Description= row[3],
                                ZeroHrProteinAbundance = row[4],
                                HalfHrProteinAbundance = row[5],
                                OneHrProteinAbundance = row[6],
                                TwoHrProteinAbundance = row[7],
                                ThreeHrProteinAbundance = row[8],
                                FourHrProteinAbundance = row[9],
                                FiveHrProteinAbundance = row[10],
                                SixHrProteinAbundance = row[11],
                                NineHrProteinAbundance = row[12],
                                TwelveHrProteinAbundance = row[13],
                                TwentyFourHrProteinAbundance = row[14],
                                CellularProcesses = row[15],
                                ProteinFunctions = row[16],
                                ReactomePathways = row[17]
                    )
            proteins.append(protein)
            
        Protein.objects.bulk_create(proteins)
        return JsonResponse({'status':'success', 'code':'200'})


class TU(generics.ListAPIView):

    serializer_class = ProteinSerializer
    #queryset = Protein.objects.all()

    def get_queryset(self):

        timePoint = int(self.request.query_params.get('timePoint'))
        abundanceThreshold = int(self.request.query_params.get('thresh'))

        if timePoint == 1:
            self.queryset = Protein.objects.filter(OneHrProteinAbundance__gte=abundanceThreshold)
            return (self.queryset)
        elif timePoint == 2:
            self.queryset = Protein.objects.filter(TwoHrProteinAbundance__gte=abundanceThreshold)
            return (self.queryset)

        #return JsonResponse(request.query_params.get('thresh'))
