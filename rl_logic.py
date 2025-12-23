import torch
import torch.nn as nn
import torch.optim as optim

class Policy(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 32),
            nn.ReLU(),
            nn.Linear(32, 3),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.net(x)

class ReinforceAgent:
    def __init__(self, lr=0.005):
        self.policy = Policy()
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
        self.log_probs = []
        self.rewards = []

    def select_action(self, state):
        probs = self.policy(state)
        action = torch.multinomial(probs, 1).item()
        self.log_probs.append(torch.log(probs[0, action]))
        return action

    def store_reward(self, reward):
        self.rewards.append(reward)

    def update(self):
        loss = []
        for log_prob, reward in zip(self.log_probs, self.rewards):
            loss.append(-log_prob * reward)

        loss = torch.stack(loss).sum()

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        self.log_probs.clear()
        self.rewards.clear()

