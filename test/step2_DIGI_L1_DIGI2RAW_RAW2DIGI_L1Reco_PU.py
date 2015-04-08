# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run2_mc_hi -s DIGI:pdigi_valid,L1,DIGI2RAW,RAW2DIGI,L1Reco --scenario HeavyIons --datatier GEN-SIM-DIGI-RAW --pileup HiMix --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV/HiFall14-START71_V1-v2/GEN-SIM --eventcontent RAWDEBUG --filein file:step1_GEN_SIM_PU.root --fileout step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU.root --no_exec --beamspot RealisticHI2011Collision --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --magField 38T_PostLS1 --customise L1Trigger/Configuration/L1Trigger_custom.customiseL1Menu_HI --customise_commands process.simCaloStage1Digis.FirmwareVersion = cms.uint32(1)
import FWCore.ParameterSet.Config as cms

process = cms.Process('L1Reco')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:./step1_GEN_SIM_PU.root'),
                            #fileNames = cms.untracked.vstring('/store/user/mnguyen/PyquenUnquenched_Dijet_pthat80_740pre6_GEN-SIM/PyquenUnquenched_Dijet_pthat80_740pre6_GEN-SIM/776d2c5e1be5ffd960f66d45fd25cdfd/step1_GEN_SIM_PU_1_1_e57.root'),
                            #fileNames = cms.untracked.vstring('/store/user/mnguyen/PyquenUnquenched_BjetLO_pthat80_740pre6_GEN-SIM/PyquenUnquenched_BjetLO_pthat80_740pre6_GEN-SIM/392c6331356dcb3e8244ab29a8dcef3f/step1_GEN_SIM_PU_1_1_YvL.root'),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU.root'),
    outputCommands = process.RAWDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from test.fileLists.hydjetMBFileList_Full_cff import myFileList
process.mix.input.fileNames = myFileList

process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_hi', '')

from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('BeamSpotObjectsRcd'),
                                                            tag= cms.string('RealisticHICollisions2011_STARTHI50_mc')
                                                            )),
                                connect =cms.string('frontier://FrontierProd/CMS_COND_31X_BEAMSPOT')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")


# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWDEBUGoutput_step = cms.EndPath(process.RAWDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.RAWDEBUGoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.L1Trigger_custom
from L1Trigger.Configuration.customise_overwriteL1Menu import L1Menu_CollisionsHeavyIons2015_v0 

#call to customisation function customiseL1Menu_HI imported from L1Trigger.Configuration.L1Trigger_custom
process = L1Menu_CollisionsHeavyIons2015_v0(process)

# End of customisation functions

# Customisation from command line
process.simCaloStage1Digis.FirmwareVersion = cms.uint32(1)

