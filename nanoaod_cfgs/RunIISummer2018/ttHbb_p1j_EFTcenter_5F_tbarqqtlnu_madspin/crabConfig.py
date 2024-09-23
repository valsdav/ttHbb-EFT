from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'dvalsecc_ttHbb_p1j_tbarqqtlnu_madspin_EFTcenter'
config.General.workArea        = 'crab_jobs'
config.General.transferOutputs = True
config.General.transferLogs    = False

config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'nanoAOD_step_fake.py'
config.JobType.inputFiles  = ['scriptExe.sh', 'genSim_step.py','digiRaw_noHLT_step.py', 'HLT_step.py','recoAOD_step.py','miniAOD_step.py','nanoAOD_step.py','pileup.py']
config.JobType.scriptExe   ='scriptExe.sh'
config.JobType.numCores    = 2
config.JobType.maxMemoryMB = 5000


config.Data.splitting   = 'EventBased'
config.Data.unitsPerJob = 2000
NJOBS = 500
config.Data.totalUnits  = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/dvalsecc/PrivateMC/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'ttHbb_p1j_tbarqqtlnu_madspin_EFTcenter_v1'
config.Data.outputDatasetTag     = 'RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-NANOAODSIM'

config.Site.storageSite = 'T2_CH_CSCS'
