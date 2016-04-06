import FWCore.ParameterSet.Config as cms

HiGenParticleAna = cms.EDAnalyzer('HiGenAnalyzer',
				  doVertex = cms.untracked.bool(False),
				  etaMax = cms.untracked.double(2),
				  ptMin = cms.untracked.double(5),
				  chargedOnly = cms.untracked.bool(False),
				  stableOnly = cms.untracked.bool(True),
				  bOnly = cms.untracked.bool(False),
				  src = cms.untracked.InputTag("generator"),
				  genParticleSrc = cms.untracked.InputTag("hiGenParticles"),
				  genHIsrc = cms.untracked.InputTag("heavyIon"),
				  doParticles = cms.untracked.bool(True),
				  doHI = cms.untracked.bool(True),
                                  saveMothers = cms.untracked.bool(False),
                                  saveDaughters = cms.untracked.bool(False),
                          )
