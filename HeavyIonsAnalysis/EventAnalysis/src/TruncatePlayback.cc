// -*- C++ -*-
//
// Package:    HeavyIonsAnalysis/TruncatePlayback
// Class:      TruncatePlayback
// 
/**\class TruncatePlayback TruncatePlayback.cc HeavyIonsAnalysis/TruncatePlayback/plugins/TruncatePlayback.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Yetkin Yilmaz
//         Created:  Tue, 23 Feb 2016 15:16:47 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "SimDataFormats/CrossingFrame/interface/CrossingFramePlaybackInfoNew.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"


//
// class declaration
//

class TruncatePlayback : public edm::stream::EDProducer<> {
   public:
      explicit TruncatePlayback(const edm::ParameterSet&);
      ~TruncatePlayback();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginStream(edm::StreamID) override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endStream() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------

  int nPU_;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
TruncatePlayback::TruncatePlayback(const edm::ParameterSet& iConfig)
{
   //register your products

  nPU_ = iConfig.getParameter<int>("nPU");

   produces<CrossingFramePlaybackInfoNew>();
   //now do what ever other initialization is needed
  
}


TruncatePlayback::~TruncatePlayback()
{
 
   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TruncatePlayback::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   //Read 'ExampleData' from the Event
   Handle<CrossingFramePlaybackInfoNew> pIn;
   iEvent.getByLabel("mix",pIn);


   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::unique_ptr<CrossingFramePlaybackInfoNew> pOut(new CrossingFramePlaybackInfoNew(0,0,1));

   for(int i = 0; i < nPU_ && i < pIn->eventInfo_.size(); ++i){
     pOut->eventInfo_.push_back(pIn->eventInfo_[i]);
   }

   iEvent.put(std::move(pOut));

}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void
TruncatePlayback::beginStream(edm::StreamID)
{
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void
TruncatePlayback::endStream() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
TruncatePlayback::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
TruncatePlayback::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
TruncatePlayback::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
TruncatePlayback::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TruncatePlayback::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TruncatePlayback);
