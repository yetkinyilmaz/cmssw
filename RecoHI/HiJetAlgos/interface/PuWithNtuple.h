#ifndef __PuWithNtuple_h_
#define __PuWithNtuple_h_

#include "RecoJets/JetProducers/interface/PileUpSubtractor.h"

class PuWithNtuple : public PileUpSubtractor {
 public:
  PuWithNtuple(const edm::ParameterSet& iConfig, edm::ConsumesCollector && iC);
    virtual void offsetCorrectJets();
    void rescaleRMS(double s);
    double getEt(const reco::CandidatePtr & in) const;
    double getEta(const reco::CandidatePtr & in) const;
    virtual void calculatePedestal(std::vector<fastjet::PseudoJet> const & coll);
    virtual void subtractPedestal(std::vector<fastjet::PseudoJet> & coll);
    virtual void calculateOrphanInput(std::vector<fastjet::PseudoJet> & orphanInput);

    bool sumRecHits_;
    bool dropZeroTowers_;

    double minimumTowersFraction_;

    ~PuWithNtuple(){;}

    edm::Service<TFileService> fs_;
    TTree* tree_;

    int Neta_;

    int nref;
    float jteta[100],jtphi[100],jtpt[100],jtpu[100],jtex[100];

    int vn[82],vnex[82];
    float veta[82],vmean[82],vrms[82];
    
};


#endif
