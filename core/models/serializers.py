from dataclasses import fields
from core.models.Protein import Protein
from rest_framework import serializers


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class ProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ('ProteinID','Accessoin','AverageMass', 
                  'Description','ZeroHrProteinAbundance','HalfHrProteinAbundance',
                  'OneHrProteinAbundance','TwoHrProteinAbundance','ThreeHrProteinAbundance',
                  'FourHrProteinAbundance','FiveHrProteinAbundance','SixHrProteinAbundance',
                  'NineHrProteinAbundance','TwelveHrProteinAbundance','TwentyFourHrProteinAbundance',
                  'CellularProcesses','ProteinFunctions','ReactomePathways'
                )

class ProteinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ('ProteinID','Accessoin','AverageMass', 
                  'Description', 'CellularProcesses','ProteinFunctions','ReactomePathways'
                )

class ProteinTimePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ('ProteinID','ZeroHrProteinAbundance','HalfHrProteinAbundance',
                  'OneHrProteinAbundance','TwoHrProteinAbundance','ThreeHrProteinAbundance',
                  'FourHrProteinAbundance','FiveHrProteinAbundance','SixHrProteinAbundance',
                  'NineHrProteinAbundance','TwelveHrProteinAbundance','TwentyFourHrProteinAbundance'
                )

class ProteinSingleTimePointSerizlizer(serializers.ModelSerializer):

    class Meta:
        model = Protein
        fields = ('ProteinID','ZeroHrProteinAbundance','HalfHrProteinAbundance',
                  'OneHrProteinAbundance','TwoHrProteinAbundance','ThreeHrProteinAbundance',
                  'FourHrProteinAbundance','FiveHrProteinAbundance','SixHrProteinAbundance',
                  'NineHrProteinAbundance','TwelveHrProteinAbundance','TwentyFourHrProteinAbundance'
                )

