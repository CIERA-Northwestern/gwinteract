from django.utils.translation import gettext_lazy as _

from django import forms
from .models import NewPopSynthModel

# Create your models here.
class NewPopSynthForm(forms.ModelForm):
    class Meta:
        model = NewPopSynthModel
        fields = ['mass_transfer_white_dwarf_to_co',
                  'select_final_state', 'binary_state',
                  'merger_type', 'LISA_convergence',
                  'seed','neta', 'bwind',
                  'hewind', 'alpha1', 'lambdaf',
                  'ceflag', 'tflag', 'ifflag', 'wdflag',
                  'bhflag', 'nsflag', 'mxns',
                  'pts1', 'pts2', 'pts3', 'sigma',
                  'beta', 'xi', 'acc2', 'epsnov',
                  'eddfac', 'gamma', 'bconst', 'CK', 'merger',
                  'windflag', 'B_0', 'bacc', 'tacc', 'bkick',
                  'massc', 'opsin', 'epoch', 'ppsn',
                 ]

        labels = {
            'mass_transfer_white_dwarf_to_co': _("Keep or discard systems that include mass transferring of "
                                                 "white swarfs onto compact objects"),
            'select_final_state': _("True to only retain the final entry of the bcm array"),
            'binary_state': _("0 alive today, 1 merged, 2 disrupted"),
            'merger_type': _("type of mergers you want. it goes by the logic "
                             "kstar1kstar2 so like 1313 for NSNS or 1414 for BHBH "
                             "value of -1 is default for alive today or disrupted"),
            'LISA_convergence': _("perform convergence over selected region"),
            'seed': _("random seed int"),
            'neta': _("neta is the Reimers mass-loss coefficent (neta;4x10^-13: 0.5 normally)."),
            'bwind': _("bwind is the binary enhanced mass loss parameter (inactive for single)."),
            'hewind': _("hewind is a helium star mass loss factor (1.0 normally)."),
            'alpha1': _("alpha1 is the common-envelope efficiency parameter (1.0)."),
            'lambdaf': _("lambda is the binding energy factor for common envelope evolution (0.5)."),
            'ceflag': _(" ceflag > 0 activates spin-energy correction in common-envelope (0)."),
            'tflag': _("tflag > 0 activates tidal circularisation (1)."),
            'ifflag': _("ifflag > 0 uses WD IFMR of HPE, 1995, MNRAS, 272, 800 (0)."),
            'wdflag': _("wdflag > 0 uses modified-Mestel cooling for WDs (0)."),
            'bhflag': _("bhflag > 0 allows velocity kick at BH formation (0)."),
            'nsflag': _("nsflag > 0 takes NS/BH mass from Belczynski et al. 2002, ApJ, 572, 407 (1)."),
            'mxns': _("mxns is the maximum NS mass (1.8, nsflag=0; 3.0, nsflag=1)."),
            'pts1': _("pts1 - MS                  (0.05)"),
            'pts2': _("pts2 - GB, CHeB, AGB, HeGB (0.01)"),
            'pts3': _("pts3 - HG, HeMS            (0.02)"),
            'sigma': _("sigma is the dispersion in the Maxwellian for the SN kick speed (190 km/s)."),
            'beta': _("beta is wind velocity factor: proportional to vwind;;2 (1/8)."),
            'xi': _("xi is the wind accretion efficiency factor (1.0)."),
            'acc2': _("acc2 is the Bondi-Hoyle wind accretion factor (3/2)."),
            'epsnov': _("epsnov is the fraction of accreted matter retained in nova eruption (0.001)."),
            'eddfac': _("eddfac is Eddington limit factor for mass transfer (1.0)."),
            'gamma': _("gamma is the angular momentum factor for mass lost during Roche (-1.0)."),
            'bconst': _("bconst"),
            'CK': _("CK"),
            'merger': _("merger"),
            'windflag': _("windflag"),
            'B_0': _("B_0 ?"),
            'bacc': _("bacc ?"),
            'tacc': _("tacc ?"),
            'bkick': _("bkick ?"),
            'massc': _("massc ?"),
            'opsin': _("opsin ?"),
            'epoch': _("epocj ?"),
            'ppsn': _("ppsn ?"),
        }
