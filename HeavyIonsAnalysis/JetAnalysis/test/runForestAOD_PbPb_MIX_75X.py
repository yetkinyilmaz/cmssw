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
        #                                "file:/afs/cern.ch/work/r/richard/public/PbPb_RECODEBUG.root",
        "/store/user/echapon/Ups1SMM_5p02TeV_TuneCUETP8M1_ptUps36/Ups1SMM_5p02TeV_TuneCUETP8M1_ptUps36_step3_20151208/151208_095635/0000/step3_RAW2DIGI_L1Reco_RECO_1.root",
                                )
                            )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_HIon', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v11', '') #for now track GT manually, since centrality tables updated ex post facto
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_PbPb5020
process = overrideJEC_PbPb5020(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
# process.centralityBin.Centrality = cms.InputTag("hiCentrality")
# process.centralityBin.centralityVariable = cms.string("HFtowers")
#process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################
process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_nominalPbPb')

# Use this one for JEC:
#process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_JECPbPb')

####################################################################################

#############################
# Gen Analyzer
#############################
process.load('HeavyIonsAnalysis.EventAnalysis.HiMixAnalyzerRECO_cff')
process.load('GeneratorInterface.HiGenCommon.HeavyIon_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.runanalyzer_cff')
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")

#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.hiEvtAnalyzer.doMC = cms.bool(False) #the gen info dataformat has changed in 73X, we need to update hiEvtAnalyzer code
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_MC_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")

process.anaTrack.qualityStrings = cms.untracked.vstring(['highPurity','tight','loose'])
process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity')
process.hiTracks.cut = cms.string('quality("highPurity")')
process.anaTrack.trackSrc = cms.InputTag("hiGeneralTracks")
process.anaTrack.doPFMatching = True
process.anaTrack.doSimVertex = True
process.anaTrack.doSimTrack = False

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cff")
process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("hiGeneralTracks")
process.quickTrackAssociatorByHits.ComponentName = cms.string('quickTrackAssociatorByHits')

#####################################################################################

#####################
# Photons
#####################

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotonsTmp'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
)

#####################################################################################

#########################
# Main analysis list
#########################

process.ana_step = cms.Path(process.heavyIon *
                            #process.mixAnalyzer *
                            process.runAnalyzer *
                            process.hltanalysis *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            process.quickTrackAssociatorByHits*
                            process.jetSequences +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            process.HiForest +
                            process.anaTrack
                            )

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pcollisionEventSelection = cms.Path(process.collisionEventSelectionAOD)
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )

process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
process.phfCoincFilter1 = cms.Path(process.hfCoincFilter)
process.phfCoincFilter2 = cms.Path(process.hfCoincFilter2)
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3)
process.phfCoincFilter4 = cms.Path(process.hfCoincFilter4)
process.phfCoincFilter5 = cms.Path(process.hfCoincFilter5)

process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization
