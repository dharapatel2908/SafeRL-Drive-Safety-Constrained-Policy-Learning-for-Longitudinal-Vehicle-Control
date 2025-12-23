import torch
from env import CarFollowingEnv
from rl_logic import ReinforceAgent
from visualizer import CarVisualizer
import matplotlib.pyplot as plt

env = CarFollowingEnv()
agent = ReinforceAgent()
viz = CarVisualizer()
episode_rewards = []

EPISODES = 100

for ep in range(EPISODES):
    state = torch.tensor([env.reset()], dtype=torch.float32)
    total_reward = 0

    while True:
        action = agent.select_action(state)
        next_state, reward, done = env.step(action)

        agent.store_reward(reward)
        total_reward += reward

        state = torch.tensor([next_state], dtype=torch.float32)

        viz.draw(env.ego_x, env.front_x)

        if done:
            agent.update()
            break
    episode_rewards.append(total_reward)
    print(f"Episode {ep} | Reward: {total_reward:.2f}")

def moving_average(data, window=10):
    return [
        sum(data[max(0, i - window):i + 1]) / (i - max(0, i - window) + 1)
        for i in range(len(data))
    ]
avg_rewards = moving_average(episode_rewards, window=10)

plt.figure(figsize=(10, 5))
plt.plot(episode_rewards, alpha=0.3, label="Raw Reward")
plt.plot(avg_rewards, linewidth=2, label="Moving Avg (10)")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Training Reward with Moving Average")
plt.legend()
plt.grid(True)
plt.show()
viz.close()
