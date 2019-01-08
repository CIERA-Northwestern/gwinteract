from django.utils.translation import gettext_lazy as _

from django import forms
from .models import NewPopSynthModel

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

# Create your models here.
class NewPopSynthForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewPopSynthForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/popsynth-generation/population-synthesis-form/'
        self.helper.layout = Layout(
            Fieldset("Command Line Arguments",
                Row(
                    Column('final_kstar1', css_class='form-group col-md-6 mb-0'),
                    Column('final_kstar2', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('initial_samp', css_class='form-group col-md-6 mb-0'),
                    Column('galaxy_component', css_class='form-group col-md-6 mb-0'),
                    Column('metallicity', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                'convergence_params',
                Row(
                    Column('Niter', css_class='form-group col-md-6 mb-0'),
                    Column('Nstep', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Filters",
                Row(
                    Column('mass_transfer_white_dwarf_to_co', css_class='form-group col-md-4 mb-0'),
                    Column('select_final_state', css_class='form-group col-md-4 mb-0'),
                    Column('binary_state', css_class='form-group col-md-4 mb-0'),
                    Column('merger_type', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Convergence",
                Row(
                    Column('LISA_convergence', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Random Seed",
                Row(
                    Column('seed', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("BSE (Binary Stellar Evolution) Flags",
                Row(
                    Column('neta', css_class='form-group col-md-4 mb-0'),
                    Column('bwind', css_class='form-group col-md-4 mb-0'),
                    Column('hewind', css_class='form-group col-md-4 mb-0'),
                    Column('alpha1', css_class='form-group col-md-4 mb-0'),
                    Column('lambdaf', css_class='form-group col-md-4 mb-0'),
                    Column('ceflag', css_class='form-group col-md-4 mb-0'),
                    Column('tflag', css_class='form-group col-md-4 mb-0'),
                    Column('ifflag', css_class='form-group col-md-4 mb-0'),
                    Column('wdflag', css_class='form-group col-md-4 mb-0'),
                    Column('bhflag', css_class='form-group col-md-4 mb-0'),
                    Column('nsflag', css_class='form-group col-md-4 mb-0'),
                    Column('mxns', css_class='form-group col-md-4 mb-0'),
                    Column('pts1', css_class='form-group col-md-4 mb-0'),
                    Column('pts2', css_class='form-group col-md-4 mb-0'),
                    Column('pts3', css_class='form-group col-md-4 mb-0'),
                    Column('sigma', css_class='form-group col-md-4 mb-0'),
                    Column('beta', css_class='form-group col-md-4 mb-0'),
                    Column('xi', css_class='form-group col-md-4 mb-0'),
                    Column('acc2', css_class='form-group col-md-4 mb-0'),
                    Column('epsnov', css_class='form-group col-md-4 mb-0'),
                    Column('eddfac', css_class='form-group col-md-4 mb-0'),
                    Column('gamma', css_class='form-group col-md-4 mb-0'),
                    Column('bconst', css_class='form-group col-md-4 mb-0'),
                    Column('CK', css_class='form-group col-md-4 mb-0'),
                    Column('merger', css_class='form-group col-md-4 mb-0'),
                    Column('windflag', css_class='form-group col-md-4 mb-0'),
                    Column('ppsn', css_class='form-group col-md-4 mb-0'),
                    Column('B_0', css_class='form-group col-md-4 mb-0'),
                    Column('bacc', css_class='form-group col-md-4 mb-0'),
                    Column('tacc', css_class='form-group col-md-4 mb-0'),
                    Column('bkick', css_class='form-group col-md-4 mb-0'),
                    Column('massc', css_class='form-group col-md-4 mb-0'),
                    Column('opsin', css_class='form-group col-md-4 mb-0'),
                    Column('epoch', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                ),
            Submit('submit', 'Generate Population')
        )

    class Meta:
        model = NewPopSynthModel
        fields = ['final_kstar1', 'final_kstar2',
                  'convergence_params', 'initial_samp',
                  'galaxy_component', 'metallicity',
                  'Niter', 'Nstep',
                  'mass_transfer_white_dwarf_to_co',
                  'select_final_state', 'binary_state',
                  'merger_type', 'LISA_convergence',
                  'seed','neta', 'bwind',
                  'hewind', 'alpha1', 'lambdaf',
                  'ceflag', 'tflag', 'ifflag', 'wdflag',
                  'bhflag', 'nsflag', 'mxns',
                  'pts1', 'pts2', 'pts3', 'sigma',
                  'beta', 'xi', 'acc2', 'epsnov',
                  'eddfac', 'gamma', 'bconst', 'CK', 'merger',
                  'windflag', 'ppsn', 'B_0', 'bacc', 'tacc', 'bkick',
                  'massc', 'opsin', 'epoch',
                 ]

        labels = {
            'final_kstar1' : _("Input a range of final states of object 1 for your systems, "
                               "(for instance 13 is NS, 14 is BH)"),
            'final_kstar2' : _("Input a range of final states of object 2 for your systems, "
                               "(for instance 13 is NS, 14 is BH)"),
            'convergence_params' : _("A comma separated list of parameters you would like to "
                                     "verify have converged to a single distribution shape"),
            'initial_samp' : _("Type of sampling of the initial conditions to use"),
            'galaxy_component' : _("Galaxy component can be Fire, DeltaBurst, ThinDisk, ThickDisk, or Bulge"),
            'metallicity' : _("The metallicity of the galaxy"),
            'Niter' : _("Total nuber of initial conditions to sample before exiting"),
            'Nstep' : _("Number of initial conditions to sample each time through loop"),
            'mass_transfer_white_dwarf_to_co': _("Keep or discard systems that include mass transferring of "
                                                 "white swarfs onto compact objects"),
            'select_final_state': _("True to only retain the final entry of the bcm array"),
            'binary_state': _("0 alive today, 1 merged, 2 disrupted"),
            'merger_type': _("type of mergers you want. it goes by the logic "
                             "kstar1kstar2 so like 1313 for NSNS or 1414 for BHBH "
                             "value of -1 is default for alive today or disrupted"),
            'LISA_convergence': _("LISA_convergence: Designed to converge on systems that are still alive today with porb < 4"),
            'seed': _("random seed"),
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
            'bconst': _("bconst pertains to neutron star (pulsar) evolution. Implemented by Paul Kiel -- see Section 3 of Kiel et al. 2008."),
            'CK': _("CK both pertains to neutron star (pulsar) evolution. Implemented by Paul Kiel -- see Section 3 of Kiel et al. 2008."),
            'merger': _("merger ???"),
            'windflag': _("windflag sets which wind prescription is to be used. 0=bse (as outlined in SSE paper), 1=StarTrack (Belczynski et al. 2010), 2=Vink (Vink et al 2001)"),
            'ppsn': _("ppsn ?"),
            'B_0': _("B_0 Not sure if does anything"),
            'bacc': _("bacc Not sure if does anything"),
            'tacc': _("tacc Not sure if does anything"),
            'bkick': _("bkick Not sure if does anything"),
            'massc': _("massc Not sure if does anything"),
            'opsin': _("opsin Not sure if does anything"),
            'epoch': _("epocj Not sure if does anything"),
        }
