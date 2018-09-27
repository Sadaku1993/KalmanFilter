#coding:utf-8
import numpy as npimport numpy as np
import matplotlib.pyplot as plt

def random_walker(start_position=0, mean=0, deviation=1, n_steps=99, seed=None):

    if seed is not None:
        np.random.seed(seed=seed)

    move = np.random.normal(loc=mean, scale=deviation, size=n_steps)
    position = np.insert(move, 0, start_position)
    position = np.cumsum(position)

    return position



def add_noise(position, mean=0, deviation=10, seed=None):

    if seed is not None:
        np.random.seed(seed=seed)

    n_observation = len(position)
    noise = np.random.normal(loc=mean, scale=deviation, size=n_observation)
    observation = position + noise

    return observation

true_position = random_walker(start_position=0, mean=0, deviation=1, n_steps=99, seed=0)
observed_position = add_noise(true_position, mean=0, deviation=10, seed=0)


class Simple_Kalman:

    def __init__(self, observation, start_position, start_deviation, deviation_true, deviation_noise):
        self.pos = observation
        self.n_obs = len(observation)
        self.start_pos = start_position
        self.start_dev = start_deviation
        self.dev_q = deviation_true
        self.dev_r = deviation_noise

    def _forward(self):
        self.x_prev_ = [self.start_pos]
        self.P_prev_ = [self.start_dev]
        
