from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ttbb_EFT_full_SMcenter'
config.General.workArea = 'crab_tasks'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ttbb-EFT-full-SMcenter.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 2

config.Data.outputPrimaryDataset = ''
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/dvalsecc/'
config.Data.publication = True
config.Data.outputDatasetTag = 'SMEFTsim_topU3l_SM_reweight1p0_v2'
config.Data.outputPrimaryDataset = 'ttbb_EFT_full_SMcenter'

config.Site.storageSite = 'T2_CH_CSCS'
