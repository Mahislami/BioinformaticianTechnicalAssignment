
import pandas as pd
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from core.models.Protein import Protein
from core.models.serializers import FileUploadSerializer, ProteinSerializer, \
                                    ProteinInfoSerializer, ProteinTimePointSerializer


# A Calss-based view for uploading the csv file
class UploadFileView(generics.CreateAPIView):
    
    serializer_class = FileUploadSerializer
    
    '''
    Description: Takes the file from the POST request, create Protein instances and fill the objects with data.

    Input: Post Requets with file field

    Output: Json object including a message and the status code
    '''

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
            return JsonResponse({'body':'success'},status=HTTP_200_OK)

        except AttributeError:
            return JsonResponse({'body':'Bad Request'}, status=HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return JsonResponse({'body':'Data ALready Exists'}, status=HTTP_400_BAD_REQUEST)

# A Calss-based view for applying threshold filters on the proteins
class ProteinAbbsorbanceTimePointThresholdFilter(APIView):

    ALLOWED_TIME_POINTS = [0, 0.5, 1, 2, 3, 4, 5, 6, 9, 12, 24]

    '''
    Description: Takes a time point and a threshold from the GET request, return Protein whose abundance is 
    above the threshold in the time point .

    Input: GET Requets with time point and threshold as prameters

    Output: Json object including a message and the status code
    '''

    def get(self, request):
        try:

            # Parse the GET request
            timePoint = request.query_params.get('timePoint')
            abundanceThreshold = request.query_params.get('thresh')

            # Validations
            if not timePoint or not abundanceThreshold:
                return JsonResponse({'body':'timePoint or abundanceThreshold not specified'},status=HTTP_400_BAD_REQUEST)

            if float(timePoint) not in self.ALLOWED_TIME_POINTS:
                return JsonResponse({'body':'Time point not defined'},status=HTTP_400_BAD_REQUEST)

            timePoint = float(timePoint)
            abundanceThreshold = float(abundanceThreshold)

            # Switchcase based on timePoint to find those above thershold in the relevant column and making query
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


# A Calss-based view for retrieving single abundance values 
class ProteinAbbsorbanceTimePointFilter(generics.ListAPIView):

        ALLOWED_TIME_POINTS = [0, 0.5, 1, 2, 3, 4, 5, 6, 9, 12, 24]
        
        '''
        Description: Takes a time point and a proteinID from the GET request, return the abundance of the protein for the given time point

        Input: GET Requets with time point and proteinID as prameters

        Output: Json object including a message and the status code
        '''

        def list(self, request, *args, **kwargs):

            try:

                # Parse the GET request
                proteinID = request.query_params.get('proteinID')
                timePoint = request.query_params.get('timePoint')

                # Validations
                if not proteinID or not timePoint:
                    return JsonResponse({'body':'proteinID or timePoint not specified'},status=HTTP_400_BAD_REQUEST)
                
                if float(timePoint) not in self.ALLOWED_TIME_POINTS:
                    return JsonResponse({'body':'Time point not defined'},status=HTTP_400_BAD_REQUEST)

                # Switchcase based on given time point and making the query    
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


# A Calss-based view for retrieving a protein's info without the numeric values
class ProteinInfo(APIView):

    '''
    Description: Takes a proteinID from the GET request, return its information excluding the numeric values

    Input: GET Requets with proteinID as prameters

    Output: Json object including a message and the status code
    '''
    
    def get(self, request):

        try:

            # Parse the GET request
            proteinID = (request.query_params.get('proteinID'))

            # Validations
            if proteinID == None:
                return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
            
            # Making the query    
            queryset = Protein.objects.filter(ProteinID=int(proteinID))
            if not queryset:
                return JsonResponse({'body':'Protein ID does not exist'}, status=HTTP_400_BAD_REQUEST)
            
            # Serializing the Protein Object 
            serializer = ProteinInfoSerializer(queryset[0])
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)
        
        except ValueError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)

        except AttributeError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)


# A Calss-based view for retrieving a protein's info only the numeric values
class ProteinTimePointAbsorbance(APIView):
    
    '''
    Description: Takes a proteinID from the GET request, return only the numeric values of the timepoints

    Input: GET Requets with proteinID as prameters

    Output: Json object including a message and the status code
    '''

    def get(self, request):
        
        try:
            
            # Parse the GET request
            proteinID = (request.query_params.get('proteinID'))

            # Validations
            if not proteinID:
                return JsonResponse({'body':'proteinID not specified'}, status=HTTP_400_BAD_REQUEST)

            # Making the query    
            queryset = Protein.objects.filter(ProteinID=proteinID)
            if not queryset:
                 return JsonResponse({'body':'Protein not found'}, status=HTTP_400_BAD_REQUEST)

            # Serializing the Protein Object        
            serializer = ProteinTimePointSerializer(queryset[0])
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)

        except ValueError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)

        except AttributeError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)


# A Calss-based view for retrieving a proteins which contain a specific cellular process
class ProteinWithSpecificProcessFunciton(APIView):

    '''
    Description: Takes a cellular processe from the GET request, return only proteins which contain this process.

    Input: GET Requets with process as prameter

    Output: Json object including a message and the status code
    '''
    
    def get(self, request):
        try:
           # Parse the GET request
            process = (request.query_params.get('process'))

            # Validations
            if not process:
                return JsonResponse({'body':'process not specified'},status=HTTP_400_BAD_REQUEST)
            
            # Making the query    
            queryset = Protein.objects.filter(CellularProcesses__icontains=process)
            if not queryset:
                return JsonResponse({'body':'No item found'}, status=HTTP_400_BAD_REQUEST)

            # Serializing the Protein Object            
            serializer = ProteinInfoSerializer(queryset, many=True)
            return JsonResponse({'body':serializer.data}, status=HTTP_200_OK)
        
        except ValueError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)

        except AttributeError:
            return JsonResponse({'status':'Bad Request'},status=HTTP_400_BAD_REQUEST)
        