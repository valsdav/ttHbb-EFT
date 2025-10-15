from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'dvalsecc_ttHbb_p1j_tbarlnutqq_madspin_EFTcenter_v1_ext1'
config.General.workArea        = 'crab_jobs'
config.General.transferOutputs = True
config.General.transferLogs    = False

config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'nanoAOD_step_fake.py'
config.JobType.inputFiles  = ['scriptExe.sh', 'genSim_step.py','digiRaw_noHLT_step.py', 'HLT_step.py','recoMiniAOD_step.py','nanoAOD_step.py','pileup.py']
config.JobType.scriptExe   ='scriptExe.sh'
config.JobType.allowUndistributedCMSSW = True

config.JobType.numCores    = 2
config.JobType.maxMemoryMB = 5000

config.JobType.outputFiles = ["nanoAOD_step.root"]
config.JobType.disableAutomaticOutputCollection = True

config.Data.splitting   = 'EventBased'

NEVENTS = 8000
NJOBS = 800
config.JobType.scriptArgs = ["nEvents="+str(NEVENTS)]
config.Data.unitsPerJob = NEVENTS
config.Data.totalUnits  = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/dvalsecc/PrivateMC/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'ttHbb_p1j_tbarlnutqq_madspin_EFTcenter_v1_ext1'
config.Data.outputDatasetTag     = 'RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-NANOAODSIM'

config.Site.storageSite = 'T2_CH_CSCS'
