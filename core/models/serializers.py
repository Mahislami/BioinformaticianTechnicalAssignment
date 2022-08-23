from core.models.Protein import Protein
from rest_framework import serializers

# A serializer class view for uploading the csv file
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

# A serializer class for the Protein Object
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

# A serializer calss for retrieving a protein's info without the numeric values
class ProteinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ('ProteinID','Accessoin','AverageMass', 
                  'Description', 'CellularProcesses','ProteinFunctions','ReactomePathways'
                )

# A serializer calss or retrieving a protein's info only the numeric values
class ProteinTimePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ('ProteinID','ZeroHrProteinAbundance','HalfHrProteinAbundance',
                  'OneHrProteinAbundance','TwoHrProteinAbundance','ThreeHrProteinAbundance',
                  'FourHrProteinAbundance','FiveHrProteinAbundance','SixHrProteinAbundance',
                  'NineHrProteinAbundance','TwelveHrProteinAbundance','TwentyFourHrProteinAbundance'
                )

