import json
from django.http import JsonResponse
from django.db import transaction
from django.shortcuts import render
from core.models.Protein import Protein
from rest_framework import generics
import io, csv, pandas as pd
from core.models.serializers import FileUploadSerializer

def home(request):
    return

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
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