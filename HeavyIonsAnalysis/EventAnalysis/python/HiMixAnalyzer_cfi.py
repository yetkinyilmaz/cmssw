import FWCore.ParameterSet.Config as cms

mixAnalyzer = cms.EDAnalyzer('HiMixValidation',
                             doHIST = cms.untracked.bool(True),
                             doMIX = cms.untracked.bool(True),
                             doGEN = cms.untracked.bool(True),
                             doSIM = cms.untracked.bool(True),
                             doRAW = cms.untracked.bool(False),
                             doRECO = cms.untracked.bool(False),
                             playbackSrc = cms.untracked.InputTag('mix'),
                             genpSrc = cms.untracked.InputTag('genParticles'),
                             jetSrc = cms.untracked.InputTag('akPu4CaloJets')
)



