# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
def return_list(x):
    return list(x)

class NewPopSynthModel(models.Model):

    # command line arguments
    final_kstar1 = ArrayField(models.IntegerField(), default=return_list((13,14)))
    final_kstar2 = ArrayField(models.IntegerField(), default=return_list((13,14)))
    convergence_params = ArrayField(models.CharField(max_length=20), default=return_list(('mass_1', 'mass_2', 'porb', 'ecc')))

    SAMPLER_CHOICES = (
        ('independent', 'independent'),
        ('multidim', 'multidim'),
    )
    initial_samp = models.CharField(max_length=20, choices=SAMPLER_CHOICES)

    GALAXY_COMPONENT_CHOICES = (
        ('ThinDisk', 'ThinDisk'),
        ('Bulge', 'Bulge'),
        ('ThickDisk', 'ThickDisk'),
        ('DeltaBurst', 'DeltaBurst'),
    )
    galaxy_component = models.CharField(max_length=20, choices=GALAXY_COMPONENT_CHOICES)

    metallicity = models.FloatField(default=0.002)
    Niter = models.IntegerField(default=100000000)
    Nstep = models.IntegerField(default=100000)

    # Filters
    mass_transfer_white_dwarf_to_co = models.BooleanField(default=False)
    select_final_state = models.BooleanField(default=True)
    binary_state = ArrayField(models.IntegerField(), default=return_list((0,1,2)))
    lisa_sources = models.BooleanField(default=False)

    # convergence
    lisa_convergence = models.BooleanField(default=False)

    # rand_seed
    seed = models.IntegerField(default=21)

    # bse params
    # neta is the Reimers mass-loss coefficent (neta;4x10^-13: 0.5 normally).
    neta = models.FloatField(default=0.5)
    # bwind is the binary enhanced mass loss parameter (inactive for single).
    bwind = models.FloatField(default=0.0)
    # hewind is a helium star mass loss factor (1.0 normally).
    hewind = models.FloatField(default=1.0)
    # alpha1 is the common-envelope efficiency parameter (1.0).
    alpha1 = models.FloatField(default=1.0)
    # lambda is the binding energy factor for common envelope evolution (0.5).
    lambdaf = models.FloatField(default=1.0)
    # ceflag > 0 activates spin-energy correction in common-envelope (0).
    ceflag = models.FloatField(default=0)
    cekickflag = models.IntegerField(default=0)
    cemergeflag = models.IntegerField(default=0)
    cehestarflag = models.IntegerField(default=0)
    # tflag > 0 activates tidal circularisation (1).
    tflag = models.FloatField(default=1)
    # ifflag > 0 uses WD IFMR of HPE, 1995, MNRAS, 272, 800 (0).
    ifflag = models.FloatField(default=0)
    # wdflag > 0 uses modified-Mestel cooling for WDs (0).
    wdflag = models.FloatField(default=0)
    # bhflag > 0 allows velocity kick at BH formation (0).
    bhflag = models.FloatField(default=1)
    # nsflag > 0 takes NS/BH mass from Belczynski et al. 2002, ApJ, 572, 407 (1).
    nsflag = models.FloatField(default=3)
    # mxns is the maximum NS mass (1.8, nsflag=0; 3.0, nsflag=1).
    mxns = models.FloatField(default=3.0)
    # idum is the random number seed used by the kick routine.
    # Next come the parameters that determine the timesteps chosen in each
    # evolution phase as decimal fractions of the time taken in that phase.:
    #                 pts1 - MS                  (0.001)
    pts1 = models.FloatField(default=0.001)
    #                 pts2 - GB, CHeB, AGB, HeGB (0.01)
    pts2 = models.FloatField(default=0.01)
    #                 pts3 - HG, HeMS            (0.02)
    pts3 = models.FloatField(default=0.02)
    # ecsnp>0 turns on ECSN and also sets the maximum ECSN mass range (mass at the time of the SN; BSE=st=2.25, Pod=2.5)
    ecsnp = models.FloatField(default=2.5)
    # ecsn_mlow sets the low end of the ECSN mass range (BSE=1.6, Pod=1.4, StarTrack=1.85)
    ecsn_mlow = models.FloatField(default=1.6)
    # aic is set to 1 for the inclusion of AIC low kicks (even if ecsnp=0), set to 0 if off
    aic = models.FloatField(default=1.0)
    # sigma is the dispersion in the Maxwellian for the SN kick speed (190 km/s).
    sigma = models.FloatField(default=265.0)
    # sigmadiv sets the ECSN kick, negative sets the ECSN sigma value to sigmadiv and positive divides sigmadiv into the above sigma
    sigmadiv=models.FloatField(default=-20.0)
    # Fraction of full NS kicks for BH bhsgmafrac, default is full NS kicks
    bhsigmafrac = models.FloatField(default=1.0)
    # Distribution from pole of star from which to draw the kick angle (Default set to 90: uniform)
    polar_kick_angle = models.FloatField(default=90.0)
    # beta is wind velocity factor: proportional to vwind;;2 (1/8).
    beta = models.FloatField(default=-1.0)
    # xi is the wind accretion efficiency factor (1.0).
    xi = models.FloatField(default=0.5)
    # acc2 is the Bondi-Hoyle wind accretion factor (3/2).
    acc2 = models.FloatField(default=1.5)
    # epsnov is the fraction of accreted matter retained in nova eruption (0.001).
    epsnov = models.FloatField(default=0.001)
    # eddfac is Eddington limit factor for mass transfer (1.0).
    eddfac = models.FloatField(default=1.0)
    # gamma is the angular momentum factor for mass lost during Roche (-1.0).
    gamma = models.FloatField(default=-2.0)
    bconst = models.FloatField(default=-3000)
    ck = models.FloatField(default=-1000)
    merger = models.FloatField(default=0)
    windflag = models.FloatField(default=3)
    natal_kick_array = ArrayField(models.FloatField(),
                       default=return_list((-100.0,-100.0,-100.0,-100.0,-100.0,-100.0)))
    qcrit_array = ArrayField(models.FloatField(),
                       default=return_list((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
    ppsn = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
