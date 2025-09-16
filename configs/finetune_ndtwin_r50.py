from easydict import EasyDict as edict

config = edict()
config.margin_list = (1.0, 0.5, 0.0)
config.network = "r50"                 # must match the backbone used in your .pth
config.resume = False
config.output = "/abs/path/to/outputs/finetune_r50"  # will be created
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True

# Optimizer
config.optimizer = "sgd"
config.lr = 0.02
config.momentum = 0.9
config.weight_decay = 5e-4

config.batch_size = 32
config.verbose = 2000
config.dali = False
config.dali_aug = False

# Your dataset root (rec folder or ImageFolder root)
config.rec = "/kaggle/input/nd-twin-448-train"

# Set these for your dataset
config.num_classes = 1234              # number of identities (subfolders for ImageFolder)
config.num_image = 567890              # total training images
config.num_epoch = 10
config.warmup_epoch = 0
config.val_targets = ['lfw', 'cfp_fp', 'agedb_30']

# NEW: path to your pretrained backbone weights
config.pretrained_backbone = "/kaggle/input/nd-twin-448-train/ms1mv2_arcface_r50_fp16.pth"  # or model.pt