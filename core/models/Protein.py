from django.db import models

class Protein(models.Model):

    ProteinID = models.IntegerField(unique=True, null=False)
    Accessoin = models.TextField(null=False)
    AverageMass = models.TextField(null=True)
    Description = models.TextField()
    ZeroHrProteinAbundance = models.TextField()
    HalfHrProteinAbundance = models.TextField()
    OneHrProteinAbundance = models.BigIntegerField()
    TwoHrProteinAbundance = models.TextField()
    ThreeHrProteinAbundance = models.TextField()
    FourHrProteinAbundance = models.TextField()
    FiveHrProteinAbundance = models.TextField()
    SixHrProteinAbundance = models.TextField()
    NineHrProteinAbundance = models.TextField()
    TwelveHrProteinAbundance = models.TextField()
    TwentyFourHrProteinAbundance = models.TextField()
    CellularProcesses = models.TextField()
    ProteinFunctions = models.TextField()
    ReactomePathways = models.TextField()

    def __str__(self):
        return str(self.ProteinID)




