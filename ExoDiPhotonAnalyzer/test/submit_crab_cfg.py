#!/usr/bin/env python
"""Submit a set of crab jobs, passing the total number
of events in the sample as a parameter to CRAB so that
the event weight can be computed."""

import subprocess
import json
import os
diphoton_analysis = __import__("diphoton-analysis.CommonClasses.das_utils")
submission = __import__("diphoton-analysis.CommonClasses.submit_utils")

#process-2018
do2018signalADD = False
do2018signalRSG = False
do2018signalHeavyHiggs = False
do2017signalADD = False
do2017signalRSG = False
do2017signalHeavyHiggs = False
# Data
do2018data = False
do2018datarereco = False
do2018Ddatarereco = False
do2018dataJetHT = False
do2017dataprompt = False
do2017data = False
do2017dataUL = False
do2017dataJetHT = False
do2016data = False
do2016data03FEB2017rereco = False
do2015data = False
# Background MC
do2018mc = False
do2017mc = False
do2017mcv1 = False
do2016mc = False
do2016mc_80X = False
dospring2016ggmc = False
do2016ggmc = False
do2015mc = False
# Signal MC
do2015signal = False
do2015signalint = False
do2016signal = False
do2016signalint = False
do2017signal = False
do2017signalint = False

DATASETS = [[]]
# each entry contains a list of datasets, including extensions
# the extensions should be included so that the weight is calculated properly
# datasets with extensions should be added following this example:
#   datasets.append(["/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM",
#                   "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-Asympt25ns_74X_mcRun2_asymptotic_v2_ext1-v1/MINIAODSIM"])

if do2018signalADD:
    DATASETS.extend(submission.CommonClasses.submit_utils.get_dataset_list("2018_ADD"))
if do2018signalRSG:
    DATASETS.extend(submission.CommonClasses.submit_utils.get_dataset_list("2018_RSG"))
if do2018signalHeavyHiggs:
    DATASETS.extend(submission.CommonClasses.submit_utils.get_dataset_list("2018_HeavyHiggs"))

if do2017signalint:
  DATASETS.append(['/GG_M-200To500_Pt-70_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-500To1000_Pt-70_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-1000To2000_Pt-70_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-2000To4000_Pt-70_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'])
  DATASETS.append(['/GG_M-4000To6000_Pt-70_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-6000To8000_Pt-70_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  
if do2017signalADD:
    DATASETS.extend(submission.CommonClasses.submit_utils.get_dataset_list("2017_ADD"))
if do2017signalRSG:
    DATASETS.extend(submission.CommonClasses.submit_utils.get_dataset_list("2017_RSG"))
if do2017signalHeavyHiggs:
    DATASETS.extend(submission.CommonClasses.submit_utils.get_dataset_list("2017_HeavyHiggs"))

if do2018datarereco:
  DATASETS.append(["/EGamma/Run2018A-17Sep2018-v2/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018B-17Sep2018-v1/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018C-17Sep2018-v1/MINIAOD"])
if do2018Ddatarereco:
  DATASETS.append(["/EGamma/Run2018D-22Jan2019-v2/MINIAOD"])
if do2018data:
  DATASETS.append(["/EGamma/Run2018A-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018A-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018A-PromptReco-v3/MINIAOD"])
  # note that the 06JUL2018 re-reco should not be used; it is a special purpose re-reco:
  # https://hypernews.cern.ch/HyperNews/CMS/get/dataopsrequests/24681.html
  DATASETS.append(["/EGamma/Run2018B-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018B-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018C-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018C-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018C-PromptReco-v3/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018D-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018D-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/EGamma/Run2018E-PromptReco-v1/MINIAOD"])
if do2018dataJetHT:
  DATASETS.append(["/JetHT/Run2018A-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018A-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018A-PromptReco-v3/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018B-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018B-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018C-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018C-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018C-PromptReco-v3/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018D-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018D-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/JetHT/Run2018E-PromptReco-v1/MINIAOD"])
# diphoton samples (2017 data)
if do2017dataprompt:
### no good lumisections are present in Run2017A
##  DATASETS.append(["/DoubleEG/Run2017A-PromptReco-v2/MINIAOD"])
##  DATASETS.append(["/DoubleEG/Run2017A-PromptReco-v3/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017B-PromptReco-v1/MINIAOD"])
### re-recos overlap with prompt; do not use for now
##  DATASETS.append(["/DoubleEG/Run2017B-23Jun2017-v1/MINIAOD"])
##  DATASETS.append(["/DoubleEG/Run2017B-22Jun2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017B-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017C-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017C-PromptReco-v2/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017C-PromptReco-v3/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017D-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017E-PromptReco-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017F-PromptReco-v1/MINIAOD"])
if do2017data:
  DATASETS.append(["/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD"])
if do2017dataUL:
  DATASETS.append(["/DoubleEG/Run2017B-09Aug2019_UL2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017C-09Aug2019_UL2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017D-09Aug2019_UL2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017E-09Aug2019_UL2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2017F-09Aug2019_UL2017-v1/MINIAOD"])
if do2017dataJetHT:
  DATASETS.append(["/JetHT/Run2017B-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2017C-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2017D-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2017E-31Mar2018-v1/MINIAOD"])
  DATASETS.append(["/JetHT/Run2017F-31Mar2018-v1/MINIAOD"])
# diphoton samples (2016 data)
if do2016data03FEB2017rereco:
# The /DoubleEG/Run2016B-03Feb2017_ver1-v1 dataset does not contain any lumisections
# passing the good run JSON
#  DATASETS.append(["/DoubleEG/Run2016B-03Feb2017_ver1-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016B-03Feb2017_ver2-v2/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016D-03Feb2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016E-03Feb2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016F-03Feb2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016G-03Feb2017-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016H-03Feb2017_ver3-v1/MINIAOD"])
# the following datasets are only for the pre-re-miniaod data
#  DATASETS.append(["/DoubleEG/Run2016B-23Sep2016-v3/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016C-23Sep2016-v1/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016D-23Sep2016-v1/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016E-23Sep2016-v1/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016F-23Sep2016-v1/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016G-23Sep2016-v1/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016H-PromptReco-v2/MINIAOD"])
#  DATASETS.append(["/DoubleEG/Run2016H-PromptReco-v3/MINIAOD"])
if do2016data:
# The /DoubleEG/Run2016B-17Jul2018_ver1-v1 dataset does not contain any lumisections
# passing the good run JSON
#  DATASETS.append(["/DoubleEG/Run2016B-17Jul2018_ver1-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016B-17Jul2018_ver2-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016C-17Jul2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016D-17Jul2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016E-17Jul2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016F-17Jul2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016G-17Jul2018-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2016H-17Jul2018-v1/MINIAOD"])

if do2018mc:
  DATASETS.append(["/GGJets_M-60To200_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-200To500_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-500To1000_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])

  DATASETS.append(["/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-4cores5k_102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])
  DATASETS.append(["/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM"])
  DATASETS.append(["/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"])

  DATASETS.append(['/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'])
  DATASETS.append(['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'])

if do2017mc:
  DATASETS.append(["/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-200To500_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-500To1000_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-60To200_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_1core_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(['/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM'])
  DATASETS.append(['/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', '/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'])
  DATASETS.append(["/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"])
  DATASETS.append(["/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"])
  DATASETS.append(["/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM"])
  DATASETS.append(['/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM','/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM','/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM','/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM','/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_old_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM','/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM','/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'])
  DATASETS.append(['/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM', '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM'])

if do2017mcv1:
  DATASETS.append(["/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-200To500_Pt-50_13TeV-sherpa/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-500To1000_Pt-50_13TeV-sherpa/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-60To200_Pt-50_13TeV-sherpa/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM","/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-1core_94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM"])

# 8_0_X MC
if dospring2016ggmc:
  DATASETS.append(["/GGJets_M-60To200_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-200To500_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-500To1000_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])

if do2016ggmc:
  DATASETS.append(["/GGJets_M-60To200_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-200To500_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-500To1000_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])

if do2016mc:
  DATASETS.append(["/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM"])
  DATASETS.append(["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM","/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM"])
  DATASETS.append(["/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"])
  DATASETS.append(["/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"])
  DATASETS.append(['/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM','/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM','/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM','/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', '/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', '/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM','/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM','/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'])
  DATASETS.append(['/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'])

if do2016mc_80X:
#  DATASETS.append(["/GGGJets_13TeV-sherpa/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"])
  DATASETS.append(["/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"])

  DATASETS.append(["/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"])

  DATASETS.append(['/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM','/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', '/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM'])

  # minor backgrounds (true photon)
  DATASETS.append(["/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM"])
  DATASETS.append(["/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  DATASETS.append(["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  # minor backgrounds (fake photon)
  DATASETS.append(["/WToLNu_0J_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  # not sure what "backup" means below
  DATASETS.append(["/WToLNu_1J_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"])
  DATASETS.append(["/WToLNu_2J_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"])
  # should check that this is a sensible set of conditions
  DATASETS.append(["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-BS2016_BSandPUSummer16_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM"])


# diphoton samples (2015 data)
if do2015data:
  DATASETS.append(["/DoubleEG/Run2015C_25ns-16Dec2015-v1/MINIAOD"])
  DATASETS.append(["/DoubleEG/Run2015D-16Dec2015-v2/MINIAOD"])

# diphoton samples (2015 MC)
if do2015mc:
  DATASETS.append(["/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-60To200_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-200To500_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-500To1000_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v3/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])

  DATASETS.append(['/QCD_Pt_5to10_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_10to15_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])

  # minor backgrounds (true photon)
  DATASETS.append(["/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  # minor backgrounds (fake photon)
  DATASETS.append(["/WToLNu_0J_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/WToLNu_1J_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/WToLNu_2J_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])

# ADD samples
if do2015signal:
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-1_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-4_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-1_M-2000To3500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-4_M-2000To3500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-2000To3500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-4_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-3000To4500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-3000To4500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-3000To4500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-3000To5000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(["/ADDGravToGG_MS-5000_NED-2_KK-4_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-3000To5000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-3000To5000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-4000To5500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-4000To5500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-4000To5500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-4000To6000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-4000To6000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-4000To6000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])

# SM diphoton background, needed to take into account interference between ADDGravToGG and SM background
if do2015signalint:
  DATASETS.append(['/GG_M-200To500_Pt-70_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-500To1000_Pt-70_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-1000To2000_Pt-70_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-2000To4000_Pt-70_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-4000To8000_Pt-70_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-8000To13000_Pt-70_13TeV-sherpa/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'])

if do2016signal:
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-4_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-1_M-2000To3500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-4_M-2000To3500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-2000To3500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-3500_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-4_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-3000To4500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-3000To4500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-3000To4500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-4500_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-3000To5000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-3000To5000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-3000To5000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-4000To5500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-4000To5500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-4000To5500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-5500_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-4000To6000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-4000To6000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-2_KK-4_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-200To500_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-4000To6000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-6000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-7000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-7000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-7000_NED-2_KK-1_M-4000To7000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-7000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-7000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-7000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-7000_NED-4_KK-1_M-4000To7000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-7000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-8000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-8000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-8000_NED-2_KK-1_M-4000To8000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-8000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-8000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-8000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-8000_NED-4_KK-1_M-4000To8000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-8000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-9000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-9000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-9000_NED-2_KK-1_M-4000To9000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-9000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-9000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-9000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-9000_NED-4_KK-1_M-4000To9000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-9000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-10000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-10000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-10000_NED-2_KK-1_M-4000To10000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-10000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-10000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-10000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-10000_NED-4_KK-1_M-4000To10000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-10000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-11000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-11000_NED-2_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-11000_NED-2_KK-1_M-4000To11000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  # DATASETS.append(['/ADDGravToGG_MS-11000_NED-2_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-11000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-11000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-11000_NED-4_KK-1_M-4000To11000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/ADDGravToGG_MS-11000_NED-4_KK-1_M-500To1000_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])

if do2016signalint:
  DATASETS.append(['/GG_M-1000To2000_Pt-70_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-2000To4000_Pt-70_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-200To500_Pt-70_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-4000To8000_Pt-70_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-500To1000_Pt-70_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])
  DATASETS.append(['/GG_M-8000To13000_Pt-70_13TeV-sherpa/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'])


for ilist in DATASETS:
  nevents = 0
  print ""
  for ids in ilist:
    nevents += diphoton_analysis.CommonClasses.das_utils.get_number_of_events(ids)
    print "running nevents is " + str(nevents)

  for ids in ilist:
    cmssw_base = os.getenv("CMSSW_BASE")
    datasetID = ids.replace('/', '', 1).replace('/', '_', 1)
    datasetID = datasetID[0:datasetID.find('/')]
    inputfile = cmssw_base + "/src/diphoton-analysis/ExoDiPhotonAnalyzer/test/crab_cfg_template.py"
    outputfile = "crab_cfg_" + datasetID + ".py"

    s = open(inputfile).read()
    s = s.replace('DATASETNAME', ids)
    s = s.replace('NEVENTS', str(nevents))
    f = open(outputfile, 'w')
    f.write(s)
    f.close()
    print "Wrote crab configuration file " + outputfile

    cmd = "crab submit -c " + outputfile
    os.system(cmd)
    print "Submitted ", ids
