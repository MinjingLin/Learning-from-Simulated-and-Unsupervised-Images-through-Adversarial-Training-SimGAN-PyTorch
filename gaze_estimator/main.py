import sys
sys.path.insert(0, 'lib/')


from gaze_estimator.lib.train_estimator import TrainEstimator
from gaze_estimator.lib.test_estimator import TestEstimator

import gaze_estimator.train_config
import gaze_estimator.test_config

if __name__ == '__main__':
	
	obj = TrainEstimator(gaze_estimator.train_config)
	obj.train()
	
	# obj = TestEstimator(test_config)
	# obj.test()

