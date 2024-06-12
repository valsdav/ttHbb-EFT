from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'tHbb_p1j_EFT_signal_EFTcenter_bquark_madspin'
config.General.workArea = 'crab_tasks'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ttHbb-p1j-EFT-full-EFTcenter-5F-tbarqqtlnu-madspin.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 5000

config.Data.outputPrimaryDataset = 'ttHbb_p1j_EFT_signal_EFTcenter'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 6000
NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/dvalsecc/'
config.Data.publication = True
config.Data.outputDatasetTag = 'SMEFTsim_topU3l_EFT_5F_tbarqqtlnu_madspin_reweightall_v1'

config.Site.storageSite = 'T2_CH_CSCS'
