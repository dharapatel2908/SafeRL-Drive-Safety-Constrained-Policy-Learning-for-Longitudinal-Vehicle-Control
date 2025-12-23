# Reinforcement Learning for Safe Longitudinal Control

## Overview
This project implements a reinforcement learning agent using the **REINFORCE policy-gradient algorithm**
to perform safe longitudinal control (accelerate, maintain, brake) in a simulated car-following task.
The agent learns purely from reward feedback without an explicit model and is trained in a lightweight
Python environment for fast iteration.

---

## Environment
- **Scenario:** Ego vehicle follows a lead vehicle in 1D
- **State:**
  - Ego speed
  - Distance to front vehicle
  - Relative speed
- **Actions:**
  - Accelerate
  - Maintain speed
  - Brake
- **Safety Constraint:**
  - Episode terminates if following distance falls below a threshold

---

## Reinforcement Learning Method
- **Algorithm:** REINFORCE (Monte Carlo policy gradient)
- **Policy:** 2-layer neural network (PyTorch)
- **Action Selection:** Stochastic sampling from policy distribution
- **Update Rule:**
  - Gradient ascent on expected return
  - Discounted and normalized returns

---

## Data Flow
The system follows a **closed-loop interaction** between the environment and the reinforcement learning agent.
All components are decoupled and communicate through well-defined interfaces.

### Step-by-Step Data Flow
Environment State (sₜ)

↓

Policy Network πθ(a | sₜ)

↓

Sample Action (aₜ)

↓

Environment Transition

↓

Reward (rₜ), Next State (sₜ₊₁)

↓

Store (log πθ(aₜ | sₜ), rₜ)

↓

Episode Termination

↓

Policy Gradient Update


---

## Learning Pipeline
The learning process is **episodic** and follows the **REINFORCE policy-gradient algorithm**.

### Training Pipeline
Initialize Policy Network

↓

For each Episode:

↓

Reset Environment

↓

For each Step in Episode:

↓

Observe State

↓

Sample Action from Policy

↓

Execute Action in Environment

↓

Receive Reward and Next State

↓

Store Reward and Log-Probability

↓

Check Termination Condition

↓

End Episode

↓

Compute Returns

↓

Update Policy Parameters

---

## Training Results

### Reward Curve
Below is the training reward per episode with a 10-episode moving average.

![Training Reward](Figuare_1.png)

### Observations
- Early training shows high variance due to stochastic policy sampling.
- Over time, the agent increasingly completes full episodes without violating safety constraints.
- High-reward episodes correspond to safe driving for the entire episode duration.

---

## Evaluation
To measure true policy performance, the agent was periodically evaluated using **greedy action selection**
(no exploration).

- Evaluation rewards increased steadily over training.
- The learned policy consistently maintained safe following distances.

---

## Key Takeaways
- REINFORCE is simple but high-variance.
- Discounted normalized returns significantly improve stability.
- Modular design allows future integration with **ROS 2** and **Gazebo**.

---

## Future Work
- Actor–Critic / PPO for lower variance
- Continuous action space control



