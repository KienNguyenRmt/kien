import gym
import numpy as np
from IPython.display import clear_output
from time import sleep
import random

env = gym.make('Taxi-v3').env

# env.reset()
# env.render()

state = env.encode(1,1,1,1)
env.s = state
# print('State: ',state)
# env.render()

q_table = np.zeros([env.observation_space.n, env.action_space.n])

LEARNING_RATE = 0.1
DISCOUNT_RATE = 0.5
EPSILON = 0.2

def main():
	total_penalties = 0
	total_epochs = 0
	for i in range(1,10000):
	    done = False
	    state = env.reset()
	    while not done:
	        if random.uniform(0,1) < EPSILON:
	            action = env.action_space.sample()
	        else:
	            action = np.argmax(q_table[state])
	        
	        next_state, reward, done, info = env.step(action)

	        q_table[state, action] = (1 - LEARNING_RATE)*q_table[state, action] + LEARNING_RATE*(reward + DISCOUNT_RATE*np.max(q_table[next_state]))
	        state = next_state

	        if reward == -10:
	            total_penalties += 1
	        total_epochs += 1
	        if i % 100 == 0:
	            clear_output(wait=True)
	            env.render()
	            sleep(0.1)

	print('Its done after {} epochs'.format(total_epochs))
	print('Total penalties is: ', total_penalties)
	print('Total epochs is: ', total_epochs)

def test(q_table):
	"""test the model with gven q_table
	:param q_table: 
	"""
	done = False
	state = env.reset()
	while not done:
	    action = np.argmax(q_table[state])
	    next_state, reward, done, info = env.step(action)
	    state = next_state
	    clear_output(wait=True)
	    env.render()
	    sleep(0.1)

if __name__ == "__main__":
	main()