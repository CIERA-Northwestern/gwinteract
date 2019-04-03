from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

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
                    Column('lisa_sources', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Convergence",
                Row(
                    Column('lisa_convergence', css_class='form-group col-md-4 mb-0'),
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
                    Column('cekickflag', css_class='form-group col-md-4 mb-0'),
                    Column('cemergeflag', css_class='form-group col-md-4 mb-0'),
                    Column('cehestarflag', css_class='form-group col-md-4 mb-0'),
                    Column('tflag', css_class='form-group col-md-4 mb-0'),
                    Column('ifflag', css_class='form-group col-md-4 mb-0'),
                    Column('wdflag', css_class='form-group col-md-4 mb-0'),
                    Column('bhflag', css_class='form-group col-md-4 mb-0'),
                    Column('nsflag', css_class='form-group col-md-4 mb-0'),
                    Column('mxns', css_class='form-group col-md-4 mb-0'),
                    Column('pts1', css_class='form-group col-md-4 mb-0'),
                    Column('pts2', css_class='form-group col-md-4 mb-0'),
                    Column('pts3', css_class='form-group col-md-4 mb-0'),
                    Column('ecsnp', css_class='form-group col-md-4 mb-0'),
                    Column('ecsn_mlow', css_class='form-group col-md-4 mb-0'),
                    Column('aic', css_class='form-group col-md-4 mb-0'),
                    Column('sigma', css_class='form-group col-md-4 mb-0'),
                    Column('sigmadiv', css_class='form-group col-md-4 mb-0'),
                    Column('bhsigmafrac', css_class='form-group col-md-4 mb-0'),
                    Column('polar_kick_angle', css_class='form-group col-md-4 mb-0'),
                    Column('beta', css_class='form-group col-md-4 mb-0'),
                    Column('xi', css_class='form-group col-md-4 mb-0'),
                    Column('acc2', css_class='form-group col-md-4 mb-0'),
                    Column('epsnov', css_class='form-group col-md-4 mb-0'),
                    Column('eddfac', css_class='form-group col-md-4 mb-0'),
                    Column('gamma', css_class='form-group col-md-4 mb-0'),
                    Column('bconst', css_class='form-group col-md-4 mb-0'),
                    Column('ck', css_class='form-group col-md-4 mb-0'),
                    Column('merger', css_class='form-group col-md-4 mb-0'),
                    Column('windflag', css_class='form-group col-md-4 mb-0'),
                    Column('ppsn', css_class='form-group col-md-4 mb-0'),
                    Column('natal_kick_array', css_class='form-group col-md-4 mb-0'),
                    Column('qcrit_array', css_class='form-group col-md-4 mb-0'),
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
                  'lisa_sources',
                  'lisa_convergence',
                  'seed','neta', 'bwind',
                  'hewind', 'alpha1', 'lambdaf',
                  'ceflag', 'cekickflag', 'cemergeflag', 'cehestarflag',
                  'tflag', 'ifflag', 'wdflag',
                  'bhflag', 'nsflag', 'mxns',
                  'pts1', 'pts2', 'pts3',
                  'ecsnp', 'ecsn_mlow', 'aic',
                  'sigma', 'sigmadiv',
                  'bhsigmafrac', 'polar_kick_angle',
                  'beta', 'xi', 'acc2', 'epsnov',
                  'eddfac', 'gamma', 'bconst', 'ck', 'merger',
                  'windflag', 'ppsn', 'natal_kick_array',
                  'qcrit_array',
                 ]

        labels = {
            'final_kstar1' : _(mark_safe("<b>FINAL_KSTAR1</b>: Input a range of final states you are interested in for one of the objects of the system, see <a href=\"https://cosmic-popsynth.github.io/runpop/index.html#independent\">details</a> for information about possible values")),
            'final_kstar2' : _(mark_safe("<b>FINAL_KSTAR2</b>: Input a range of final states you are interested in for the other object, see <a href=\"https://cosmic-popsynth.github.io/runpop/index.html#independent\">details</a> for information about possible values")),
            'convergence_params' : _(mark_safe("<b>CONVERGENCE_PARAMS</b>: A comma separated list of parameters you would like to "
                                     "verify have converged to a single distribution shape")),
            'initial_samp' : _(mark_safe("<b>INITIAL_SAMP</b>: Type of sampling of the initial conditions to use")),
            'galaxy_component' : _(mark_safe("<b>Star Formation History</b>: SFH can be Fire, DeltaBurst, ThinDisk, ThickDisk, or Bulge, see <a href=\"https://cosmic-popsynth.github.io/fixedpop/index.html#inputs\">details</a> for information about possible values")),
            'metallicity' : _(mark_safe("<b>METALLICITY</b>: The metallicity of the galaxy")),
            'Niter' : _(mark_safe("<b>NITER</b>: Total nuber of initial conditions to sample before exiting")),
            'Nstep' : _(mark_safe("<b>NSTEP</b>: Number of initial conditions to sample each time through loop")),
            'mass_transfer_white_dwarf_to_co': _(mark_safe("<b>MASS TRANSFER OF WHITE DWARFS ONTO COMPACT OBJECTS</b>: Keep or discard systems that include mass transferring of "
                                                 "white dwarfs onto compact objects")),
            'select_final_state': _(mark_safe("<b>FINAL STATE</b>: (DONT TOUCH) True to only retain the final entry of the bcm array")),
            'binary_state': _(mark_safe("<b>STATE OF BINARY</b>: 0 The binary is still alive today, 1 the binary has coalesced, 2 the binary system was disrupted")),
            'lisa_sources': _(mark_safe("<b>LISA SOURCES</b>: True - throw out binaries w/ porb > 1e5 sec; False - retain all binaries regardless of porb")),
            'lisa_convergence': _(mark_safe("<b>TRACK CONVERGENCE FOR LISA SOURCES</b>: Designed to converge on systems that are still alive today with porb < 4")),
            'seed': _("random seed"),
            'neta': _(mark_safe("<b>NETA</b>: neta is the Reimers mass-loss coefficent (neta;4x10^-13: 0.5 normally).")),
            'bwind': _(mark_safe("<b>BWIND</b>: bwind is the binary enhanced mass loss parameter (inactive for single).")),
            'hewind': _(mark_safe("<b>HEWIND</b>: hewind is a helium star mass loss factor (1.0 normally).")),
            'alpha1': _(mark_safe("<b>ALPHA1</b>: alpha1 is the common-envelope efficiency parameter (1.0).")),
            'lambdaf': _(mark_safe("<b>LAMBDA</b>: lambda is the binding energy factor for common envelope evolution (0.5).")),
            'ceflag': _(mark_safe("<b>CEFLAG</b>: ceflag > 0 activates spin-energy correction in common-envelope (0).")),
            'cekickflag': _(mark_safe("<b>CEKICKFLAG</b>: prescription for calling kick.f in comenv.f ( 0: default BSE or 1: uses pre-CE mass and sep values or 2: uses post-CE mass and sep).")),
            'cemergeflag': _(mark_safe("<b>CEMERGEFLAG</b>: cemergeflag: whether stars without core-envelope boundary automatiically lead to merger in CE (0 off, 1 on).")),
            'cehestarflag': _(mark_safe("<b>CEHESTARFLAG</b>: cehestarflag: uses fitting formulae from TLP, 2015, MNRAS, 451 for evolving systems involving a mass-transferring He-star witha compact object (0: off, 1: fits for final period only, 2: fits for both final mass and final period).")),
            'tflag': _(mark_safe("<b>TFLAG</b>: tflag > 0 activates tidal circularisation (1).")),
            'ifflag': _(mark_safe("<b>IFFLAG</b>: ifflag > 0 uses WD IFMR of HPE, 1995, MNRAS, 272, 800 (0).")),
            'wdflag': _(mark_safe("<b>WDFLAG</b>: wdflag > 0 uses modified-Mestel cooling for WDs (0).")),
            'bhflag': _(mark_safe("<b>BHFLAG</b>: bhflag > 0 allows velocity kick at BH formation (0).")),
            'nsflag': _(mark_safe("<b>NSFLAG</b>: nsflag > 0 takes NS/BH mass from Belczynski et al. 2002, ApJ, 572, 407 (1).")),
            'mxns': _(mark_safe("<b>MXNS</b>: mxns is the maximum NS mass (1.8, nsflag=0; 3.0, nsflag=1).")),
            'pts1': _(mark_safe("<b>PTS1</b>: pts1 - MS (0.001)")),
            'pts2': _(mark_safe("<b>PTS2</b>: pts2 - GB, CHeB, AGB, HeGB (0.01)")),
            'pts3': _(mark_safe("<b>PTS3</b>: pts3 - HG, HeMS (0.02)")),
            'ecsnp': _(mark_safe("<b>ECSNP</b>: ecsnp>0 turns on ECSN and also sets the maximum ECSN mass range (mass at the time of the SN; BSE=st=2.25, Pod=2.5)")),
            'ecsn_mlow': _(mark_safe("<b>ECSN_MLOW</b>: ecsn_mlow sets the low end of the ECSN mass range (BSE=1.6, Pod=1.4, StarTrack=1.85)")),
            'aic': _(mark_safe("<b>AIC</b>: aic is set to 1 for the inclusion of AIC low kicks (even if ecsnp=0), set to 0 if off")),
            'sigma': _(mark_safe("<b>SIGMA</b>: sigma is the dispersion in the Maxwellian for the SN kick speed (265 km/s).")),
            'sigmadiv': _(mark_safe("<b>SIGMADIV</b> :sigmadiv sets the ECSN kick, negative sets the ECSN sigma value to sigmadiv and positive divides sigmadiv into the above sigma (-20.0)")),
            'bhsigmafrac': _(mark_safe("<b>BHSIGMAFRAC</b>:  fraction of NS kick sigma for Black Holes (default: 1.0, can be between [0.0 and 1.0]).")),
            'polar_kick_angle': _(mark_safe("<b>POLAR_ANGLE_KIck</b>: Angle from pole of star to restrict the maximum of the distribution to (90 degrees: uniform across all angles).")),
            'beta': _(mark_safe("<b>BETA1</b>: beta is wind velocity factor: proportional to vwind;;2 (1/8).")),
            'xi': _(mark_safe("<b>XI</b>: xi is the wind accretion efficiency factor (1.0).")),
            'acc2': _(mark_safe("<b>acc2</b>: acc2 is the Bondi-Hoyle wind accretion factor (3/2).")),
            'epsnov': _(mark_safe("<b>EPSNOV</b>: epsnov is the fraction of accreted matter retained in nova eruption (0.001).")),
            'eddfac': _(mark_safe("<b>EDDFAC</b>: eddfac is Eddington limit factor for mass transfer (1.0).")),
            'gamma': _(mark_safe("<b>GAMMA</b>: gamma is the angular momentum factor for mass lost during Roche (-1.0).")),
            'bconst': _(mark_safe("<b>BCONST</b>: bconst pertains to neutron star (pulsar) evolution. Implemented by Paul Kiel -- see Section 3 of Kiel et al. 2008.")),
            'ck': _(mark_safe("<b>CK</b>:  both pertains to neutron star (pulsar) evolution. Implemented by Paul Kiel -- see Section 3 of Kiel et al. 2008.")),
            'merger': _(mark_safe("<b>MERGER</b>: merger ???")),
            'windflag': _(mark_safe("<b>WINDFLAG</b>: windflag sets which wind prescription is to be used. 0=bse (as outlined in SSE paper), 1=StarTrack (Belczynski et al. 2010), 2=Vink (Vink et al 2001)")),
            'ppsn': _(mark_safe("<b>PPSN</b>: Pair Instability supernova flag")),
            'natal_kick_array': _(mark_safe("<b>NATAL_KICK_ARRAY</b>: 6-length array for user-input values for the SN natal kick of format: (vk1, vk2, phi1, phi2, theta1, theta2) vk is valid on the range [0, inf], phi are the co-lateral polar angles valid from [-pi/2, pi/2], and theta are azimuthal angles [0, 2*pi]; any number outside of these ranges will be sampled in the standard way in kick.f")),
            'qcrit_array': _(mark_safe("<b>QCRIT_ARRAY</b>: ; 16-length array for user-input values for the critical mass ratios that govern the onset of unstable mass transfer and a common envelope. Each item is set individually for its associated kstar, and a value of 0.0 will apply the standard BSE prescription for that kstar")),
        }
