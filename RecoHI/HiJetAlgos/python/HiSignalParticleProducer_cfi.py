import FWCore.ParameterSet.Config as cms


signalGenParticles = cms.EDProducer('HiSignalParticleProducer',
                                    src    = cms.InputTag('genParticles')
                                    )

