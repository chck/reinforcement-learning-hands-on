#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gym
import time

env = gym.make('cartpole-v0')
env.reset()  # 初期値
for i in range(1000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())  # 適当な動き
    print("observation: {}\treward: {}\tdone: {}".format(observation, reward, done))
    time.sleep(1)

# rewardをたくさんもらいたい！！
