from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ttHbb_p1j_EFT_signal_SMcenter_ext'
config.General.workArea = 'crab_tasks'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ttHbb-p1j-EFT-full-SMcenter.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 5000

config.Data.outputPrimaryDataset = 'ttHbb_p1j_EFT_signal_SMcenter'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 20000
NJOBS = 300  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/dvalsecc/'
config.Data.publication = True
config.Data.outputDatasetTag = 'SMEFTsim_topU3l_SM_reweight1p0_v3_ext'

config.Site.storageSite = 'T2_CH_CSCS'
