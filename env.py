import random

class CarFollowingEnv:
    def __init__(self):
        self.dt = 0.1
        self.safe_distance = 60.0
        self.max_steps = 300   # 👈 ADD THIS
        self.reset()

    def reset(self):
        self.ego_speed = random.uniform(2, 4)
        self.front_speed = random.uniform(2.5, 4)
        self.ego_x = 100
        self.front_x = self.ego_x + random.uniform(80, 120)
        self.steps = 0         # 👈 ADD THIS
        self.done = False
        return self._get_state()

    def _get_state(self):
        distance = self.front_x - self.ego_x
        rel_speed = self.ego_speed - self.front_speed
        return [self.ego_speed, distance, rel_speed]

    def step(self, action):
        reward = 0.0
        self.steps += 1   # 👈 ADD THIS

        # Actions
        if action == 0:      # accelerate
            self.ego_speed += 0.2
            reward -= 0.1
        elif action == 2:    # brake
            self.ego_speed = max(0, self.ego_speed - 0.4)
            reward -= 0.2
        else:                # maintain
            reward += 0.1

        # Update positions
        self.ego_x += self.ego_speed
        self.front_x += self.front_speed

        distance = self.front_x - self.ego_x

        # Safety
        if distance < self.safe_distance:
            reward -= 10
            self.done = True

        if self.safe_distance < distance < 120:
            reward += 1.0

        # End episode if max steps reached
        if self.steps >= self.max_steps:
            self.done = True

        return self._get_state(), reward, self.done
