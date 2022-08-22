from django.db import models

class Protein(models.Model):

    ProteinID = models.IntegerField(unique=True, null=False)
    Accessoin = models.TextField(null=False)
    AverageMass = models.TextField(null=True)
    Description = models.TextField()
    ZeroHrProteinAbundance = models.BigIntegerField()
    HalfHrProteinAbundance = models.BigIntegerField()
    OneHrProteinAbundance = models.BigIntegerField()
    TwoHrProteinAbundance = models.BigIntegerField()
    ThreeHrProteinAbundance = models.BigIntegerField()
    FourHrProteinAbundance = models.BigIntegerField()
    FiveHrProteinAbundance = models.BigIntegerField()
    SixHrProteinAbundance = models.BigIntegerField()
    NineHrProteinAbundance = models.BigIntegerField()
    TwelveHrProteinAbundance = models.BigIntegerField()
    TwentyFourHrProteinAbundance = models.BigIntegerField()
    CellularProcesses = models.TextField()
    ProteinFunctions = models.TextField()
    ReactomePathways = models.TextField()

    def __str__(self):
        return str(self.ProteinID)