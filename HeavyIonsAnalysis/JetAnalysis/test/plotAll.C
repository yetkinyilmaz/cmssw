
TLegend* makeLegend(double x1 = 0.3, double y1 = 0.3, double x2 = 0.9, double y2 = 0.4){

   TLegend *leg = new TLegend(x1,y1,x2,y2);

   leg->SetFillColor(0);
   leg->SetBorderSize(0);
   leg->SetFillStyle(0);
   leg->SetTextFont(43);
   leg->SetTextSize(18);

   return leg;
}



void plot(const char* file = "HiForestBKG_02.root", 
	  const char* printName = "bkg_eta_all.png", 
	  string var = "eta", 
	  TCut selection = ""){

   TCanvas* c1 = new TCanvas("c1","c1",600,600);

   TFile* inf = new TFile(file);
   TTree* hi  = (TTree*)inf->Get("HiGenParticleAna/hi");

   TH1D* h;
   if(var == "eta"){
      h = new TH1D("h",";#eta;particles",200,-20,20);
   }

   if(var == "npart"){
      h = new TH1D("h",";#eta;particles",50,0,50);
   }
   //   h->SetMarkerStyle(20);
   h->SetLineColor(1);

   hi->Draw(Form("%s>>h",var.data()),selection,"hist");


   TLegend* leg = makeLegend();

   leg->AddEntry(h,"mean","");
   leg->AddEntry(h,Form("%0.4f#pm%0.4f",h->GetMean(),h->GetMeanError()),"");

   leg->Draw();

   c1->Print(printName);

}


void plotAll(){

   TH1::SetDefaultSumw2();

   const char* bkgFile = "HiForestBKG_03.root";
   const char* signalFile = "HiForestMIXED.root";

   TCut noN("pdg != 2112 && pdg != 2212");

   if(0){
      plot(bkgFile,"bkg_npart_all.png","npart","");
      plot(bkgFile,"bkg_eta_npart2.png","eta","npart == 2");
      plot(bkgFile,"bkg_eta_npart5.png","eta","npart > 2 && npart < 10");
      plot(bkgFile,"bkg_eta_npart12.png","eta","npart >= 10");
      plot(bkgFile,"bkg_eta_all.png","eta","");
      
      plot(bkgFile,"bkg_eta_npart2_cut.png","eta",noN&&"npart == 2");
      plot(bkgFile,"bkg_eta_npart5_cut.png","eta",noN&&"npart > 2 && npart < 10");
      plot(bkgFile,"bkg_eta_npart12_cut.png","eta",noN&&"npart >= 10");
      plot(bkgFile,"bkg_eta_all_cut.png","eta",noN);
   }

   //   plot(signalFile,"signal_eta.png","eta","sube == 0");
   //   plot(signalFile,"bkg_eta.png","eta","sube != 0");
   plot(signalFile,"all_eta.png","eta","");

   //   plot(signalFile,"signal_eta_cut.png","eta",noN&&"sube == 0");
   //   plot(signalFile,"bkg_eta_cut.png","eta",noN&&"sube != 0");




}

