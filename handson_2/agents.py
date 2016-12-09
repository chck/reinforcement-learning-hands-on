import numpy as np
import random


class Agent():
    def __init__(self):
        self.reward = 0

    def act(self, observation):
        raise Exception("Agent have to implements act function")

    def reset(self):
        self.reward = 0


class RandomAgent(Agent):
    """Agent that behaves ramdomly
    """

    def __init__(self, action_n):
        super().__init__()
        self.actions = list(range(action_n))
        self.reward = 0

    def act(self, observation):
        return random.choise(self.actions)


class FunFunAgent(Agent):
    """Agent that behaves up side down
    """

    def __init__(self, action_up, action_down, action_stop, interval=30):
        super().__init__()
        self.action_up = action_up
        self.action_down = action_down
        self.action_stop = action_stop
        self._interval = interval
        self._plan = []

    def act(self, observation):
        # _plan is empty
        if not self._plan:
            # 初期centerから上下にふんふん守る
            self._plan += [self.action_up] * self._interval  # up
            self._plan += [self.action_down] * self._interval  # back to center
            self._plan += [self.action_down] * self._interval  # down
            self._plan += [self.action_up] * self._interval  # back to center

        return self._plan.pop(0)


class TrackAgent(Agent):
    """Agent that keeps track ball movements
    """

    def __init__(self, action_up, action_down, action_stop):
        super().__init__()
        self.action_up = action_up
        self.action_down = action_down
        self.action_stop = action_stop
        self._past_action = self.action_stop

    def act(self, observation):
        player, enemy, ball = self.observation_to_state(observation)
        action = self._past_action
        # playerとballの座標が検出できていて
        if len(player) == len(ball) == 2:
            # playerよりもballの方が位置的に下だったら
            if player[0] < ball[0]:
                action = self.action_down  # playerも下に動く
            else:  # playerよりもballの方が位置的に上だったら
                action = self.action_up  # playerも上に動く
            self._past_action = action  # playerのactionの履歴を更新

        return action

    def observation_to_state(self, observation):
        """player/enemy/ballの座標(y, x)を返す
        """
        player_color = [92, 186, 92]
        enemy_color = [213, 130, 74]
        ball_color = [236, 236, 236]

        # search_positionの妨げになるため画面上下の余計なピクセルを削除（点数のところとか）
        area = observation[35:194]

        player = self.search_position(area, player_color)
        enemy = self.search_position(area, enemy_color)
        ball = self.search_position(area, ball_color)

        return player, enemy, ball

    def search_position(self, area, color):
        """RGBの行列から指定色の座標を返す
        """
        position = []
        index = np.where(area == color)
        if len(index[0]) > 0:
            position = [index[0][0], index[1][0]]
        return position
