#!/bin/bash
BASE=$PWD
NEVENTS=10
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh


echo "================= CMSRUN starting GEN-SIM step ====================" | tee -a job.log
cmsRun -j genSim_step.log genSim_step.py jobNum=$1 nEvents=${NEVENTS}

echo "================= CMSRUN starting DIGI-RAW step ====================" | tee -a job.log

cmsRun -j digiRaw_noHLT_step.log digiRaw_noHLT_step.py 

echo "================= CMSRUN starting HLT step =========================" | tee -a job.log

# We need this specific release for the menu
if [ -r CMSSW_10_2_16_UL/src ] ; then
  echo release CMSSW_10_2_16_UL already exists
else
  scram p CMSSW CMSSW_10_2_16_UL
fi
cd CMSSW_10_2_16_UL/src
eval `scram runtime -sh`
cd $BASE

cmsRun -j HLT_step.log HLT_step.py

echo "================= CMSRUN starting RECO-AOD-MINIAOD step ====================" | tee -a job.log

# back to base cmssw
cd $BASE
eval `scram runtime -sh`
cmsRun -j recoMiniAOD_step.log recoMiniAOD_step.py


echo "================= CMSRUN starting NanoAOD step  ====================" | tee -a job.log
cmsRun -e -j FrameworkJobReport.xml nanoAOD_step.py

echo "================= CMSRUN finished ====================" | tee -a job.log
