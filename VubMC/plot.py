import ROOT as r

tfs = []
trees = []

tfs.append( r.TFile("BcDmunu_tree.root") )
tfs.append( r.TFile("BuDmunu_tree.root") )
tfs.append( r.TFile("BuKpipi_tree.root") )
tfs.append( r.TFile("BdKpipipi_tree.root") )
tfs.append( r.TFile("BsKpipipi_tree.root") )

for f in tfs:
  trees.append( f.Get("DecayTree") )

hists = []
hists.append( r.TH1F("h1","",100,1,7) )
hists.append( r.TH1F("h2","",100,4,7) )
hists.append( r.TH1F("h3","",100,1,7) )
hists.append( r.TH1F("h4","",100,4,7) )
hists.append( r.TH1F("h5","",100,1,7) )
hists.append( r.TH1F("h6","",100,4,7) )
hists.append( r.TH1F("h7","",100,1,7) )
hists.append( r.TH1F("h8","",100,4,7) )
hists.append( r.TH1F("h9","",100,1,7) )
hists.append( r.TH1F("h10","",100,4,7) )

trees[0].Draw( "Bcp_M>>h1", "", "goff")
trees[1].Draw( "Bp_M>>h3", "", "goff")
trees[2].Draw( "Bp_0_M>>h5", "", "goff" )
trees[3].Draw( "B0_0_M_pip_12mup>>h7", "", "goff")
trees[4].Draw( "Bs0_0_M_pip_12mup>>h9", "", "goff")
trees[0].Draw( "MCorr>>h2", "", "goff")
trees[1].Draw( "MCorr>>h4", "", "goff")
trees[2].Draw( "Bp_0_M_pip_12mup>>h6", "", "goff")
trees[3].Draw( "MCorr_pip_12mup>>h8", "", "goff")
trees[4].Draw( "MCorr_pip_12mup>>h10", "", "goff")

hists[0].SetLineColor(r.kRed)
hists[1].SetLineColor(r.kRed)
hists[4].SetLineColor(r.kGreen+3)
hists[5].SetLineColor(r.kGreen+3)
hists[6].SetLineColor(r.kMagenta+1)
hists[7].SetLineColor(r.kMagenta+1)
hists[8].SetLineColor(r.kBlue)
hists[9].SetLineColor(r.kBlue)

canv = r.TCanvas("c","c",1600,600)
canv.Divide(2,1)

canv.cd(1)
hists[2].Draw("HIST")
hists[0].Draw("HISTsame")
hists[4].Draw("HISTsame")
hists[6].Draw("HISTsame")
hists[8].Draw("HISTsame")

canv.cd(2)
hists[3].Draw("HIST")
hists[1].Draw("HISTsame")
hists[5].Draw("HISTsame")
hists[7].Draw("HISTsame")
hists[9].Draw("HISTsame")

canv.Update()
canv.Modified()
raw_input()


