import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.EventAnalysis.HiMixAnalyzer_cfi import *

mixAnalyzer.doHIST = True
mixAnalyzer.doGEN = True
mixAnalyzer.doSIM = True
mixAnalyzer.doRAW = False
mixAnalyzer.doRECO = False

mixAnalyzer.jetSrc = cms.untracked.InputTag('akPu4CaloJets')



