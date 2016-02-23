import FWCore.ParameterSet.Config as cms

truncatePileUp = cms.EDProducer('TruncatePlayback',
                                nPU = cms.int32(1)
                                )



