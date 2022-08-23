from django.test import TestCase
from core.models.Protein import Protein
from rest_framework.test import APIRequestFactory
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from core.views import ProteinAbbsorbanceTimePointThresholdFilter

class TestProteinAbbsorbanceTimePointThresholdFilter(TestCase):

    # Sample valid and invalid requests body    
    requestProperBodyLowThresh = {'timePoint': 12, 'thresh':2631899999}
    requestProperBodyHighThresh = {'timePoint': 12, 'thresh':2631900001}
    requestMissingThresholdBody = {'timePoint': 12}
    requestInvaildTimePointBody = {'timePoint': 8, 'thresh':2631899999}
    requestMissingTimepointBody = {'thresh':1000000}
    requestMissingFieldsBody = {}
    
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
    def testRequestProperBodyLowThresh(self):
        factory = APIRequestFactory()
        request = factory.get('/list/', self.requestProperBodyLowThresh)
        response = ProteinAbbsorbanceTimePointThresholdFilter.as_view()(request)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def testRequestProperBodyHighThresh(self):
        factory = APIRequestFactory()
        request = factory.get('/list/', self.requestProperBodyHighThresh)
        response = ProteinAbbsorbanceTimePointThresholdFilter.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def testRequestMissingThresholdBody(self):
        factory = APIRequestFactory()
        request = factory.get('/list/', self.requestMissingThresholdBody)
        response = ProteinAbbsorbanceTimePointThresholdFilter.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def testRequestMissingTimepointBody(self):
        factory = APIRequestFactory()
        request = factory.get('/list/', self.requestMissingTimepointBody)
        response = ProteinAbbsorbanceTimePointThresholdFilter.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def testRequestMissingFieldsBody2(self):
        factory = APIRequestFactory()
        request = factory.get('/list/', self.requestMissingFieldsBody)
        response = ProteinAbbsorbanceTimePointThresholdFilter.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def testRequestInvaildTimePointBody(self):
        factory = APIRequestFactory()
        request = factory.get('/list/', self.requestInvaildTimePointBody)
        response = ProteinAbbsorbanceTimePointThresholdFilter.as_view()(request)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)