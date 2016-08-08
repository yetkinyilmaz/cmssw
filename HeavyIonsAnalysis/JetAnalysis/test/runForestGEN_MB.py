### HiForest Configuration
# Collisions: PbPb
# Type: MonteCarlo
# Input: AOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet()

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
#                                "/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/000259ED-823D-E611-868C-44A842CFD5CB.root"
'/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/000259ED-823D-E611-868C-44A842CFD5CB.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/002D76F3-9D3D-E611-AEFA-20CF3027A594.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00C07CB1-733D-E611-BA6F-44A8423D7E31.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00C2832C-863D-E611-A7C2-000E1E878860.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00D790D1-A03D-E611-AA0D-7845C4F91495.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00E73359-A23D-E611-8684-1418774117C7.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/00F66620-AD3D-E611-8E1B-6CC2173DC030.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/025D80F3-933D-E611-82AA-20CF3027A5C5.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/026B44B8-F73D-E611-8082-78E7D1217468.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/GEN-SIM/80X_mcRun2_asymptotic_v12-v1/20000/02BED953-9C3D-E611-AF5D-0025905AC878.root'
                                )
                            )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestBKG_03.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################


#############################
# Gen Analyzer
#############################
process.load('HeavyIonsAnalysis.EventAnalysis.HiMixAnalyzerRECO_cff')
process.load('GeneratorInterface.HiGenCommon.HeavyIon_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.runanalyzer_cff')
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")
# Temporary disactivation - until we have DIGI & RECO in CMSSW_7_5_7_patch4
process.HiGenParticleAna.doHI = False


#####################################################################################


#########################
# Main analysis list
#########################

process.ana_step = cms.Path(
# process.mixAnalyzer *
    process.heavyIon*
                            process.HiGenParticleAna
                            )

#####################################################################################


##########################################UE##########################################


process.HiGenParticleAna.src = cms.untracked.InputTag("generatorSmeared")

process.HiGenParticleAna.ptMin = -999
process.HiGenParticleAna.etaMax = 999
process.HiGenParticleAna.doHI = True
