from http.client import BAD_REQUEST, HTTPResponse
import json
from pickle import TRUE
from re import T
from telnetlib import STATUS
from django.http import JsonResponse
from django.shortcuts import render
from core.models.Protein import Protein
from rest_framework import generics
from rest_framework.views import APIView
import io, csv, pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models.serializers import FileUploadSerializer, ProteinSerializer, ProteinInfoSerializer, ProteinTimePointSerializer, ProteinSingleTimePointSerizlizer
from rest_framework.response import Response
from django.core import serializers
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_200_OK)

def home(request):
    return

class UploadFileView(generics.CreateAPIView):
    
    serializer_class = FileUploadSerializer
    
    def create(self, request, *args, **kwargs):
        try:
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

        except AttributeError:
            return JsonResponse({'status':'Bad Request', 'code':'400'})
    

class ProteinAbbsorbanceTimePointThresholdFilter(APIView):

    ALLOWED_TIME_POINTS = [0, 0.5, 1, 2, 3, 4, 5, 6, 9, 12, 24]

    def get(self, request):
        try:
            timePoint = request.query_params.get('timePoint')
            abundanceThreshold = request.query_params.get('thresh')

            if not timePoint or not abundanceThreshold:
                return JsonResponse({'body':'timePoint or abundanceThreshold not specified'},status=HTTP_400_BAD_REQUEST)

            if float(timePoint) not in self.ALLOWED_TIME_POINTS:
                return JsonResponse({'body':'Time point not defined'},status=HTTP_400_BAD_REQUEST)

            timePoint = float(timePoint)
            abundanceThreshold = float(abundanceThreshold)

            if timePoint == 0:
                queryset = Protein.objects.filter(ZeroHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 0.5:
                queryset = Protein.objects.filter(HalfHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 1:
                queryset = Protein.objects.filter(OneHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 2:
                queryset = Protein.objects.filter(TwoHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 3:
                queryset = Protein.objects.filter(ThreeHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 4:
                queryset = Protein.objects.filter(FourHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 5:
                queryset = Protein.objects.filter(FiveHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 6:
                queryset = Protein.objects.filter(SixHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 9:
                queryset = Protein.objects.filter(NineHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 12:
                queryset = Protein.objects.filter(TwelveHrProteinAbundance__gte=abundanceThreshold)
            elif timePoint == 24:
                queryset = Protein.objects.filter(TwentyFourHrProteinAbundance__gte=abundanceThreshold)

            if not queryset:
                return JsonResponse({'body':'No Protein exists'}, status=HTTP_400_BAD_REQUEST)

            serializer = ProteinSerializer(queryset, many=True)
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)
            

        except AttributeError:
            return JsonResponse({'status':'Bad Request', 'code':HTTP_400_BAD_REQUEST})


class ProteinAbbsorbanceTimePointFilter(generics.ListAPIView):

        ALLOWED_TIME_POINTS = [0, 0.5, 1, 2, 3, 4, 5, 6, 9, 12, 24]
        
        def list(self, request, *args, **kwargs):

            try:
                proteinID = request.query_params.get('proteinID')
                timePoint = request.query_params.get('timePoint')

                if not proteinID or not timePoint:
                    return JsonResponse({'body':'proteinID or timePoint not specified'},status=HTTP_400_BAD_REQUEST)
                
                if float(timePoint) not in self.ALLOWED_TIME_POINTS:
                    return JsonResponse({'body':'Time point not defined'},status=HTTP_400_BAD_REQUEST)

                if float(timePoint) == 0:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','ZeroHrProteinAbundance').first()
                elif float(timePoint) == 0.5:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','HalfHrProteinAbundance').first()
                elif float(timePoint) == 1:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','OneHrProteinAbundance').first()
                elif float(timePoint) == 2:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','TwoHrProteinAbundance').first()
                elif float(timePoint) == 3:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','ThreeHrProteinAbundance').first()
                elif float(timePoint) == 4:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','FourHrProteinAbundance').first()
                elif float(timePoint) == 5:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','FiveHrProteinAbundance').first()
                elif float(timePoint) == 6:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','SixHrProteinAbundance').first()
                elif float(timePoint) == 9:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','NineHrProteinAbundance').first()
                elif float(timePoint) == 12:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','TwelveHrProteinAbundance').first()
                elif float(timePoint) == 24:
                    queryset = Protein.objects.filter(ProteinID=proteinID).values('ProteinID','TwentyFourHrProteinAbundance').first()
                
                if not queryset:
                     return JsonResponse({'body':'Protein not found'}, status=HTTP_400_BAD_REQUEST)

                return JsonResponse({'body':queryset},status=HTTP_200_OK)
                
            except AttributeError:
                return JsonResponse({'body':'Bad Request'},status=HTTP_400_BAD_REQUEST)


class ProteinInfo(APIView):
    
    def get(self, request):

        try:
            proteinID = (request.query_params.get('proteinID'))
            if proteinID == None:
                return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
            queryset = Protein.objects.filter(ProteinID=int(proteinID))
            if not queryset:
                return JsonResponse({'body':'Protein ID does not exist'}, status=HTTP_400_BAD_REQUEST)
            serializer = ProteinInfoSerializer(queryset[0])
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)
        except ValueError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
        except AttributeError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)


class ProteinTimePointAbsorbance(APIView):
    
    def get(self, request):
        
        try:
            proteinID = (request.query_params.get('proteinID'))
            if not proteinID:
                return JsonResponse({'body':'proteinID not specified'}, status=HTTP_400_BAD_REQUEST)
            queryset = Protein.objects.filter(ProteinID=proteinID)
            if not queryset:
                 return JsonResponse({'body':'Protein not found'}, status=HTTP_400_BAD_REQUEST)
            serializer = ProteinTimePointSerializer(queryset[0])
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)
        except ValueError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
        except AttributeError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)


class ProteinWithSpecificProcessFunciton(APIView):
    
    def get(self, request):
        try:
            process = (request.query_params.get('process'))
            if not process:
                return JsonResponse({'body':'process not specified'},status=HTTP_400_BAD_REQUEST)
            queryset = Protein.objects.filter(CellularProcesses__icontains=process)
            if not queryset:
                return JsonResponse({'body':'No item found'}, status=HTTP_400_BAD_REQUEST)
            serializer = ProteinInfoSerializer(queryset, many=True)
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)
        except ValueError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
        except AttributeError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
        