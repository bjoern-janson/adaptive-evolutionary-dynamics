# Adaptive Evolutionary Dynamics

A framework for studying when adaptive systems transition from improving within a fixed space of possibilities to modifying the mechanisms that determine which possibilities are reachable.

> **Central hypothesis:** Major capability transitions are preceded by changes in the processes that generate future capability.

---

# Overview

Most adaptive systems improve by changing their current state:

$$
\Delta C > 0
$$

where $C$ denotes the system's current capability.

Some systems appear to undergo a deeper transition: they begin modifying the mechanisms responsible for producing future improvements.

The key distinction is

$$
\boxed{
\text{Capability growth}
\neq
\text{Evolutionary acceleration}
}
$$

A system can become more capable without becoming better at becoming more capable.

---

# Core Hypothesis

The framework centers on three quantities.

| Symbol | Meaning |
|---------|---------|
| $C$ | Current capability |
| $G_m$ | Generator modification capacity |
| $\Omega$ | Evolutionary velocity |

The central prediction is

$$
\boxed{
\Delta G_m
\rightarrow
\Delta\Omega
\rightarrow
\Delta C
}
$$

Meaning:

1. The capability-generation mechanism changes.
2. The rate of future improvement changes.
3. Observable capability accelerates afterward.

---

# Mathematical Framework

## Adaptive system state

An adaptive system is represented as

$$
\boxed{
\mathcal{A}_t=
(S_t,D_t,X_t,\Theta_t)
}
$$

where

| Variable | Meaning |
|----------|---------|
| $S_t$ | Scale where adaptation occurs |
| $D_t$ | Adaptive depth |
| $X_t$ | System configuration |
| $\Theta_t$ | Trajectory dynamics |

---

## Internal configuration

$$
\boxed{
X_t=
(
Z_t,
M_t,
\pi_t,
V_t,
C_t,
G_{s,t},
G_{m,t},
R_t
)
}
$$

| Variable | Meaning |
|----------|---------|
| $Z_t$ | Current system state |
| $M_t$ | Internal representation/model |
| $\pi_t$ | Policy/controller |
| $V_t$ | Objective or value function |
| $C_t$ | Current capability |
| $G_s$ | Search mechanism |
| $G_m$ | Generator modification mechanism |
| $R_t$ | Available resources |

---

# Adaptive Dynamics

The adaptive loop is

```text
Environment
      ↓
Observation
      ↓
Representation
      ↓
Policy
      ↓
Action
      ↓
Environment
```

or equivalently

$$
E_t
\rightarrow
O_t
\rightarrow
M_t
\rightarrow
\pi_t
\rightarrow
u_t
\rightarrow
E_{t+1}
$$

The component updates are

Observation

$$
O_t=H(E_t)
$$

Representation update

$$
M_{t+1}=U(M_t,O_t)
$$

Action selection

$$
u_t=\pi_t(M_t,V_t)
$$

Environment transition

$$
E_{t+1}=F(E_t,u_t)
$$

Complete system evolution

$$
\boxed{
X_{t+1}=F_X(X_t,E_t,u_t)
}
$$

---

# Adaptive Depth

Adaptive depth is defined by the target of feedback.

$$
\boxed{
D=\operatorname{Target}(Feedback)
}
$$

The key question is:

> **What does the system update when it receives information?**

## D0 — State adaptation

Updates system configuration.

$$
Z_{t+1}=f(Z_t,O_t)
$$

**Example:** learning a fact.

---

## D1 — Search adaptation

Updates the search strategy.

$$
G_{s,t+1}=f(G_{s,t},O_t)
$$

**Example:** improving problem-solving strategy.

---

## D2 — Generator adaptation

Updates the mechanism that produces solutions.

$$
G_{m,t+1}
=
f(G_{m,t},G_{s,t},M_t,O_t)
$$

**Example:** scientific methods, compilers, automated discovery systems.

---

## D3 — Generator-dynamics adaptation

Updates the rate at which generators improve.

$$
\Omega_{t+1}
=
f(\Omega_t,G_m,G_s,M_t,O_t)
$$

The system modifies the dynamics of its own improvement process.

---

# Reachable Future Space

The framework measures **reachable** futures rather than all imaginable futures.

$$
\boxed{
\mathcal{P}^{reach}_{evo}(t)
=
\{
\tau:
E_t\rightarrow E_{t+k}
|
\tau
\text{ reachable under }X_t,R_t
\}
}
$$

This distinguishes

$$
\boxed{
\text{Possible futures}
\neq
\text{Reachable futures}
}
$$

Reachability is constrained by

- representations
- tools
- resources
- search mechanisms
- generator mechanisms

---

# Capability

Current capability is defined as

$$
\boxed{
C_t=
|\mathcal{P}^{reach}_{current}(t)|
}
$$

Capability describes the current reachable frontier.

---

# Search and Generator Mechanisms

Search maps reachable possibilities into explored possibilities.

$$
\boxed{
G_s:
\mathcal{P}^{reach}_{current}
\rightarrow
\mathcal{P}^{explored}
}
$$

Generator modification improves search itself.

$$
\boxed{
G_m:
G_s(t)
\rightarrow
G_s(t+1)
}
$$

---

# Evolutionary Velocity

The raw expansion rate of reachable space is

$$
\Lambda(t)
=
\frac{d}{dt}
\log
|\mathcal{P}^{reach}(t)|
$$

This expansion contains multiple causes.

$$
\boxed{
\Lambda
=
\Delta_R+\Delta_C+\Delta_G
}
$$

where

Resource contribution

$$
\Delta_R
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial R}
\dot R
$$

Capability contribution

$$
\Delta_C
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial C}
\dot C
$$

Generator contribution

$$
\Delta_G
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial G_m}
\dot G_m
$$

The quantity of interest is

$$
\boxed{
\Omega\equiv\Delta_G
}
$$

---

# Interpretation

| Quantity | Interpretation |
|----------|----------------|
| $C$ | What the system can do |
| $G_s$ | How the system finds new capabilities |
| $G_m$ | How the system improves its search mechanism |
| $\Omega$ | How quickly the system improves its own improvement machinery |

---

# Dynamic Causal Mass

Traditional causal influence

$$
\boxed{
\Phi(I)
=
\frac{\partial Z_{future}}{\partial I}
}
$$

Dynamic causal influence

$$
\boxed{
\Phi_D(I)
=
\frac{\partial G_{future}}{\partial I}
}
$$

A normal intervention changes outcomes.

An evolutionary intervention changes the mechanism producing future outcomes.

---

# Evolutionary Primitives

An artifact stores a result.

$$
A=x
$$

A primitive stores a transformation.

$$
P:x\rightarrow y
$$

An evolutionary primitive stores a transformation that modifies future transformations.

$$
P_e:f\rightarrow f'
$$

Examples

| System | Primitive |
|----------|-----------|
| Hammer | Force → impact |
| Factory | Inputs → products |
| Programming language | Problems → programs |
| Scientific method | Questions → experiments → knowledge |
| Self-improving discovery system | Discovery → better discovery |

---

# Anti-Recursion Principle

The framework rejects unnecessary ontological layers.

**Rule**

$$
\boxed{
\textbf{
Do not add a new entity when a trajectory variable explains the phenomenon.
}
}
$$

Higher-order behavior is represented through dynamics

$$
X
\rightarrow
\dot X
\rightarrow
\ddot X
$$

rather than

$$
X
\rightarrow
X_{meta}
\rightarrow
X_{meta^2}
$$

Therefore,

$$
\boxed{
\text{Meta is not a location.}
}
$$

and

$$
\boxed{
\text{Meta is a property of transformation dynamics.}
}
$$

---

# Empirical Program

The framework is not complete until its latent variables become measurable.

## Measuring $G_m$

Can we identify when a system begins modifying its own improvement mechanisms?

Possible proxies

- reduced iteration cost
- reusable improvement infrastructure
- abstraction creation
- automated method generation
- increased search efficiency

---

## Measuring Reachable Space

Possible proxies

- number of reachable solution classes
- search efficiency
- representation compression
- tool leverage
- exploration breadth

---

## Testing $\Omega$

The central prediction is

$$
\boxed{
\Omega_t\uparrow
\Rightarrow
C_{t+\tau}\uparrow\uparrow
}
$$

while controlling for

- resources
- current capability
- data
- labor
- compute

---

# Historical Case Studies

Potential test cases

- Scientific method
- Printing press
- Programming languages
- Compilers
- Automatic differentiation
- Machine learning
- Automated scientific discovery

For each case ask

1. Did $G_m$ change?
2. Did $\Omega$ increase?
3. Did capability acceleration follow?

---

# Status

Early research framework.

Current goals

- formalize definitions
- develop measurable proxies
- build simulations
- analyze historical transitions
- attempt falsification

---

# Core Invariant

$$
\boxed{
\textbf{
Higher-order adaptive behavior is not a higher object.
It is the dynamics of lower-order adaptive processes.
}
}
$$

The framework studies the point where systems stop merely adapting to the world and begin adapting the mechanisms by which they adapt.
