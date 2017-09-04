
from matplotlib import pyplot as plt
import time
import numpy as np

from environments.continous_maze_discrete_fixed import CTS_Maze
from tasks.CTS_TASK import CTS_MazeTask
from pybrain.rl.experiments import EpisodicExperiment
from learners.sparse_learner import GP_SARSA_SPARSE
from agents.sparse_agent import GPSARSA_Agent

plt.ion()

i=1000
performance=[]  #reward accumulation, dump variable for any evaluation metric
sum=[]


track_time=[]
dict_size=[]

for repeat in range(1):
    env = CTS_Maze([0.40, 0.40])  # goal

    task = CTS_MazeTask(env)
    learner = GP_SARSA_SPARSE(gamma=0.95)
    learner.sigma = 1
    learner.batchMode = False  # extra , not in use , set to True for batch learning
    agent = GPSARSA_Agent(learner)
    agent.logging = True

    exp = EpisodicExperiment(task, agent)
    agent.reset()
    sum=[]
    performance=[]
    track_time=[]
    agent.init_exploration=1.0
    starttime = time.time()
    dict_size=[]
    epsilon=[]

    b=[]
    c=[]
    for num_exp in range(10):
        performance=exp.doEpisodes(1)
        sum = np.append(sum, np.sum(performance))

        agent.init_exploration=(10/(10+num_exp))
        epsilon.append(agent.init_exploration)
        agent.learn()
        dict_size=np.append(dict_size,learner.state_dict.shape[0])
        track_time=np.append(track_time,[time.time()-starttime])
        print('dataset',agent.history)
        agent.reset()
        print(sum)




