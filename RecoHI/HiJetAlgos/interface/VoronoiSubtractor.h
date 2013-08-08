#ifndef __VoronoiSubtractor_h_
#define __VoronoiSubtractor_h_

#include "RecoJets/JetProducers/interface/PileUpSubtractor.h"
#include "DataFormats/HeavyIonEvent/interface/VoronoiBackground.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class VoronoiSubtractor : public PileUpSubtractor {
 public:
   VoronoiSubtractor(const edm::ParameterSet& iConfig);
/*: PileUpSubtractor(iConfig),
     sumRecHits_(iConfig.getParameter<bool>("sumRecHits")),
      dropZeroTowers_(iConfig.getUntrackedParameter<bool>("dropZeroTowers",true)){;}*/

/*    virtual void reset(std::vector<edm::Ptr<reco::Candidate> >& input,
		       std::vector<fastjet::PseudoJet>& towers,
		       std::vector<fastjet::PseudoJet>& output);
*/
    virtual void setupGeometryMap(edm::Event& iEvent,const edm::EventSetup& iSetup);
    virtual void calculatePedestal(std::vector<fastjet::PseudoJet> const & coll);
    virtual void subtractPedestal(std::vector<fastjet::PseudoJet> & coll);
    virtual void calculateOrphanInput(std::vector<fastjet::PseudoJet> & orphanInput);
    virtual void offsetCorrectJets();

    bool match(fastjet::PseudoJet, fastjet::PseudoJet);

    ~VoronoiSubtractor(){;}

 private:
    edm::Handle<reco::CandidateView> candidates_;
    edm::Handle<reco::VoronoiMap> backgrounds_;
    edm::InputTag srcCand_;
    edm::InputTag srcVor_;
    std::vector<int> droppedCandidates_;
    bool dropZeroTowers_;
    double rParam_;

};


#endif
