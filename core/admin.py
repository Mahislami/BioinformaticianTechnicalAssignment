from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from core.models.Protein import Protein
from django.http import JsonResponse
from django import forms
import io, csv, pandas as pd

class CsvImportForm(forms.Form):
    csvUpload = forms.FileField()


class coreAdmin(admin.ModelAdmin):

    def get_urls(self):
        url = super().get_urls()
        new_urls = [path('upload-csv/',self.upload_csv)]
        return new_urls + url
    
    def upload_csv(self, request):

        if request.method == 'POST':
            
            csvFile = request.FILES['csvUpload']
            csvData = pd.read_csv(csvFile)
        

            proteins = []
            for _, row in csvData.iterrows():
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

        form = CsvImportForm()
        data = {"form":form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(Protein, coreAdmin)

