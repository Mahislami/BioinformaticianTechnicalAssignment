from django.test import TestCase
from core.models.Protein import Protein
from rest_framework.test import APIRequestFactory
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from core.views import ProteinInfo


class TestProteinInfo(TestCase):
    
    # Sample valid and invalid requests body
    requestProperBody = {'proteinID': 26}
    requestNonExistingProtein = {'proteinID':27}
    requestMissingFieldBody = {}
    
    # Creating dummy record in test db
    def setUp(self):
        Protein.objects.create(
                    ProteinID = 26,
                      Accessoin = 'P26039|TLN1_MOUSE',
                      AverageMass= '269819',
                      Description= 'Talin-1 OS=Mus musculus GN=Tln1 PE=1 SV=2',
                      ZeroHrProteinAbundance = 1752600000,
                      HalfHrProteinAbundance = 2531600000,
                      OneHrProteinAbundance = 2478000000,
                      TwoHrProteinAbundance = 2255400000,
                      ThreeHrProteinAbundance = 2485300000,
                      FourHrProteinAbundance = 2449800000,
                      FiveHrProteinAbundance = 2428100000,
                      SixHrProteinAbundance = 23288000000,
                      NineHrProteinAbundance = 2512400000,
                      TwelveHrProteinAbundance = 2631900000,
                      TwentyFourHrProteinAbundance = 2175000000,
                      CellularProcesses = 'cell adhesion',
                      ProteinFunctions = 'actin filament binding',
                      ReactomePathways = 'Platelet degranulation'
                    )

    # Test Cases
    def testRequestProperBody(self):
        factory = APIRequestFactory()
        request = factory.get('/info/', self.requestProperBody)
        response = ProteinInfo.as_view()(request)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def testRequestMisingField(self):
        factory = APIRequestFactory()
        request = factory.get('/info/', self.requestMissingFieldBody)
        response = ProteinInfo.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def testRequestNonExistingProtein(self):
        factory = APIRequestFactory()
        request = factory.get('/info/', self.requestNonExistingProtein)
        response = ProteinInfo.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)