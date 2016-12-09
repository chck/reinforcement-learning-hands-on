import argparse
import gym
import time


def main(episode):
    env = gym.make("Pong-v0")
    action_number = env.action_space.n
    # コマンドなので決まった数字を設定
    action_up = 2
    action_down = 3
    action_stop = 0
    """ write your code
    """
    ###
    ###

    for i in range(episode):
        # observation...3フレーム分の縦x横のRGBのListが取れる
        observation = env.reset()
        done = False
        agent.init()
        name = agent.__class__.__name__

        while not done:
            env.render()
            action = agent.act(observation)
            next_observation, reward, done, info = env.step(action)
            print("{} takes action: {}...reward: {}".format(name, action, reward))

            observation = next_observation  # ゲームの状態を更新
            agent.reward += reward

            if done:
                print("Episode {} is end by {}!! reward: {}".format(i, name, agent.reward))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is my pong by Open AI Gym")
    parser.add_argument("-e", "--episode", type=int, help="episode count of game", default=2)

    main(parser.parse_args().episode)
