import gym
from IPython.display import clear_output
import numpy as np
import random
from time import sleep

#Initiate the environment
env = gym.make('MountainCar-v0').env

# print('Observation Space: ', env.observation_space)
# print('Action Space: ', env.action_space.n)

LEARNING_RATE = 0.1
DISCOUNT = 0.2
EPSILON = 0.1

discrete_os_size = [24] * len(env.observation_space.high)
discrete_win_size = (env.observation_space.high - env.observation_space.low) / discrete_os_size

#inititate the q_table
q_table = np.zeros(discrete_os_size + [env.action_space.n])

def get_discrete_state(state):
	"""
	Find the discrete state of the car
	:param state: the current state
	"""
	discrete_state = (state - env.observation_space.low) / discrete_win_size
	return tuple(discrete_state.astype(np.int))


def main():
	done = False

	for i in range(0,20000):
	    state = env.reset()
	    epochs = 0
	    while not done:
	        discrete_state = get_discrete_state(state)
	        action = np.argmax(q_table[discrete_state])
	        new_state, reward, done, info = env.step(action)
	        new_discrete_state = get_discrete_state(new_state)
	        q_table[discrete_state + (action,)] = (1 - LEARNING_RATE) * q_table[discrete_state + (action,)] + \
	                                            LEARNING_RATE * (reward + DISCOUNT * np.max(q_table[new_discrete_state]))
	        state = new_state
	        epochs += 1
	        env.render()

	env.close()

if __name__ == "__main__":
	main()