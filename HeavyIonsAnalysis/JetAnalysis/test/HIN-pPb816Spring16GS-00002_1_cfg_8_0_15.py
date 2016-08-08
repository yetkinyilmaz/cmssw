# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/HIN-pPb816Spring16GS-00002-fragment.py --fileout file:./output.root --pileup_input dbs:/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/pPb816Spring16GS-80X_mcRun2_asymptotic_v12-v1/GEN-SIM --mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 80X_mcRun2_asymptotic_v15 --beamspot Match5TeVPPbBoost --step GEN,SIM --scenario HeavyIons --era Run2_2016 --python_filename HIN-pPb816Spring16GS-00002_1_cfg_8_0_15.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 200
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMixGEN_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedMatch5TeVPPbBoost_cff')
process.load('Configuration.StandardSequences.GeneratorMix_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('PYTHIA 8 (unquenched) dijets in NN (pt-hat > 15 GeV) at sqrt(s) = 8.16 TeV')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:./output.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/000259ED-823D-E611-868C-44A842CFD5CB.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/002D76F3-9D3D-E611-AEFA-20CF3027A594.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00C07CB1-733D-E611-BA6F-44A8423D7E31.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00C2832C-863D-E611-A7C2-000E1E878860.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00D790D1-A03D-E611-AA0D-7845C4F91495.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00E73359-A23D-E611-8684-1418774117C7.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00F66620-AD3D-E611-8E1B-6CC2173DC030.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/025D80F3-933D-E611-82AA-20CF3027A5C5.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/026B44B8-F73D-E611-8082-78E7D1217468.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/02BED953-9C3D-E611-AF5D-0025905AC878.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v15', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring('HardQCD:all = on', 
            'PhaseSpace:pTHatMin = 15.', 
            'PhaseSpace:pTHatMax = 9999.'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(8160.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

