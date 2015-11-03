import FWCore.ParameterSet.Config as cms

genParticles = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    mix = cms.string("mix"), # inactive unless useCF == True
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)


