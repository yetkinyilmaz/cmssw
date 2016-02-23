import FWCore.ParameterSet.Config as cms

truncatePileUp = cms.EDProducer('truncatePileUp',
                                nPU = cms.int32(1)
                                )



