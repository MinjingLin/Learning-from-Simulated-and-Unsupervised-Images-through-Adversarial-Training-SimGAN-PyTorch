import sys

sys.path.insert(0, 'lib/')

# Import class and config file for training 
from simgan.lib.train_simgan import TrainSimGAN
import simgan.train_config

# Import class and config file for testing
from simgan.lib.test_simgan import TestSimGAN
import simgan.test_config

if __name__ == '__main__':
	# If you want to train, uncomment the following two line
	#trainer = TrainSimGAN(simgan.train_config)
	#trainer.train()
	
	# If you want to test, uncomment the following two lines
	tester = TestSimGAN(simgan.test_config)
	tester.refine()
