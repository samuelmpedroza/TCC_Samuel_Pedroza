import gym
import rsoccer_gym
from neat import nn, population, statistics, parallel
import neat_gym

net, env_name, recording_flag, seed, no_display_flag, csv_file_name = neat_gym.read_file()
# Using VSS Single Agent env
# env = gym.make('VSS-v0')

# env.reset()
# # Run for 1 episode and print reward at the end
# for i in range(1):
#     done = False
#     while not done:
#         # Step using random actions
#         action = env.action_space.sample()
#         next_state, reward, done, _ = env.step(action)
#         env.render()
#     print(reward)