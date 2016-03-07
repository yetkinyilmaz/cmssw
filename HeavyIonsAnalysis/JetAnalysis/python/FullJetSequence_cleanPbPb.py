import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_HI_cff import *
from RecoHI.HiJetAlgos.HiGenJets_cff import *
from RecoJets.Configuration.GenJetParticles_cff import *
from Configuration.StandardSequences.ReconstructionHeavyIons_cff import voronoiBackgroundPF, voronoiBackgroundCalo


ak3HiGenJets.signalOnly = False
ak4HiGenJets.signalOnly = False

from RecoHI.HiJetAlgos.HiGenCleaner_cff import heavyIonCleanedGenJets

ak3HiCleanedGenJets = heavyIonCleanedGenJets.clone(src = "ak3HiGenJets")
ak4HiCleanedGenJets = heavyIonCleanedGenJets.clone(src = "ak4HiGenJets")

akHiGenJets = cms.Sequence(
    genParticlesForJets +
    ak3HiGenJets +
    ak4HiGenJets +
    ak3HiCleanedGenJets +
    ak4HiCleanedGenJets     
)





#from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akVs2CaloJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akVs2PFJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_PbPb_mc_cff import *
#from HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.makePartons_cff import *
from RecoHI.HiJetAlgos.HiGenCleaner_cff import hiPartons

highPurityTracks = cms.EDFilter("TrackSelector",
                                src = cms.InputTag("hiGeneralTracks"),
                                cut = cms.string('quality("highPurity")'))

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
offlinePrimaryVertices.TrackLabel = 'highPurityTracks'

jetSequences = cms.Sequence(
    akHiGenJets +

    voronoiBackgroundPF+
    voronoiBackgroundCalo+

    #akPu2CaloJets +
    #akPu2PFJets +
    #akVs2CaloJets +
    #akVs2PFJets +

    #akPu3CaloJets +
    #akPu3PFJets +
    akVs3CaloJets +
    akVs3PFJets +

    #akPu4CaloJets +
    #akPu4PFJets +
    akVs4CaloJets +
    akVs4PFJets +

    #akPu5CaloJets +
    #akPu5PFJets +
    #akVs5CaloJets +
    #akVs5PFJets +

    makePartons +
    hiPartons +
    highPurityTracks +
    offlinePrimaryVertices +

    #akPu2CaloJetSequence +
    #akVs2CaloJetSequence +
    #akVs2PFJetSequence +
    #akPu2PFJetSequence +

    akPu3CaloJetSequence +
    akVs3CaloJetSequence +
    akPu3PFJetSequence +
    akVs3PFJetSequence +

    akPu4CaloJetSequence +
    akVs4CaloJetSequence +
    akPu4PFJetSequence +
    akVs4PFJetSequence #+

    #akPu5CaloJetSequence +
    #akVs5CaloJetSequence +
    #akVs5PFJetSequence +
    #akPu5PFJetSequence
)
