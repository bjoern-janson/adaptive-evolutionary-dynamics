# Adaptive Evolutionary Dynamics

A framework for studying when adaptive systems transition from improving within a fixed space of possibilities to modifying the mechanisms that determine which possibilities are reachable.

The central hypothesis is:

> Major capability transitions are preceded by changes in the processes that generate future capability.

---

# Overview

Most adaptive systems improve by changing their current state:

$$
\Delta C > 0
$$

where

$$
C = \text{current capability}
$$

However, some systems appear to undergo a deeper transition: they begin modifying the mechanisms responsible for producing future improvements.

This framework studies that transition.

The key distinction:

$$
\boxed{
\text{Capability growth}
\neq
\text{Evolutionary acceleration}
}
$$

A system can become more capable without becoming better at becoming more capable.

---

# Core hypothesis

The framework proposes that adaptive systems can be analyzed through three related quantities.

### Current capability

$$
C
$$

### Generator modification capacity

$$
G_m
$$

The ability of a system to improve the mechanisms that produce solutions.

### Evolutionary velocity

$$
\Omega
$$

The rate at which the system improves its own capability-generation dynamics.

The central prediction:

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

# Mathematical framework

## Adaptive system state

A system is represented as

$$
\boxed{
\mathcal{A}_t=
(S_t,D_t,X_t,\Theta_t)
}
$$

where

$$
S_t=\text{scale}
$$

Where adaptation occurs.

$$
D_t=\text{adaptive depth}
$$

What the adaptive process modifies.

$$
X_t=\text{system configuration}
$$

$$
\Theta_t=\text{trajectory dynamics}
$$

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

where

| Variable | Meaning |
| --- | --- |
| $Z_t$ | Current system state |
| $M_t$ | Internal representation/model |
| $\pi_t$ | Policy/controller |
| $V_t$ | Objective/value function |
| $C_t$ | Current capability |
| $G_s$ | Search mechanism |
| $G_m$ | Generator modification mechanism |
| $R_t$ | Available resources |

---

# Adaptive dynamics

The basic adaptive loop:

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

Observation:

$$
O_t=H(E_t)
$$

Representation update:

$$
M_{t+1}=U(M_t,O_t)
$$

Action selection:

$$
u_t=\pi_t(M_t,V_t)
$$

Environment transition:

$$
E_{t+1}=F(E_t,u_t)
$$

Full system evolution:

$$
\boxed{
X_{t+1}=F_X(X_t,E_t,u_t)
}
$$

---

# Adaptive depth

Depth is defined by the target of feedback:

$$
\boxed{
D=\operatorname{Target}(Feedback)
}
$$

The question:

> What does the system update when it receives information?

## D0 — State adaptation

Feedback changes the configuration.

$$
Z_{t+1}=f(Z_t,O_t)
$$

Example:

Learning a fact.

---

## D1 — Search adaptation

Feedback changes exploration strategy.

$$
G_{s,t+1}=f(G_{s,t},O_t)
$$

Example:

Improving problem-solving strategy.

---

## D2 — Generator adaptation

Feedback changes the mechanism producing solutions.

$$
G_{m,t+1}
=
f(G_{m,t},G_{s,t},M_t,O_t)
$$

Example:

Scientific methods, compilers, automated discovery systems.

---

## D3 — Generator-dynamics adaptation

Feedback changes the rate at which generators improve.

$$
\Omega_{t+1}
=
f(\Omega_t,G_m,G_s,M_t,O_t)
$$

The system modifies the dynamics of its own improvement process.

---

# Reachable future space

The framework does not measure all imaginable futures.

It measures reachable futures:

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

The distinction:

$$
\boxed{
\text{Possible futures}
\neq
\text{Reachable futures}
}
$$

A system's future is constrained by

- representations
- tools
- resources
- search mechanisms
- generator mechanisms

---

# Capability

Current capability:

$$
\boxed{
C_t=
|\mathcal{P}^{reach}_{current}(t)|
}
$$

Capability describes the current reachable frontier.

---

# Search and generator mechanisms

Search:

$$
\boxed{
G_s:
\mathcal{P}^{reach}_{current}
\rightarrow
\mathcal{P}^{explored}
}
$$

The process of discovering possibilities.

---

Generator modification:

$$
\boxed{
G_m:
G_s(t)
\rightarrow
G_s(t+1)
}
$$

The process that improves search itself.

---

# Evolutionary velocity

The raw expansion rate of reachable space:

$$
\Lambda(t)
=
\frac{d}{dt}
\log
|\mathcal{P}^{reach}(t)|
$$

However, this contains multiple causes:

$$
\boxed{
\Lambda
=
\Delta_R+\Delta_C+\Delta_G
}
$$

Resource contribution:

$$
\Delta_R
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial R}
\dot R
$$

Capability contribution:

$$
\Delta_C
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial C}
\dot C
$$

Generator contribution:

$$
\Delta_G
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial G_m}
\dot G_m
$$

The target quantity:

$$
\boxed{
\Omega\equiv\Delta_G
}
$$

---

# Interpretation

$$
\boxed{
C=\text{what the system can do}
}
$$

$$
\boxed{
G_s=\text{how the system finds things it can do}
}
$$

$$
\boxed{
G_m=\text{how the system improves how it finds things it can do}
}
$$

$$
\boxed{
\Omega=\text{how quickly the system improves its own improvement machinery}
}
$$

---

# Dynamic causal mass

Traditional causal influence:

$$
\boxed{
\Phi(I)
=
\frac{\partial Z_{future}}{\partial I}
}
$$

Dynamic causal influence:

$$
\boxed{
\Phi_D(I)
=
\frac{\partial G_{future}}{\partial I}
}
$$

The difference:

A normal intervention changes outcomes.

An evolutionary intervention changes the mechanism producing future outcomes.

---

# Evolutionary primitives

An artifact stores a result:

$$
\boxed{
A=x
}
$$

A primitive stores a transformation:

$$
\boxed{
P:x\rightarrow y
}
$$

An evolutionary primitive stores a transformation that modifies future transformations:

$$
\boxed{
P_e:f\rightarrow f'
}
$$

Examples:

| System | Primitive |
| --- | --- |
| Hammer | Force → impact |
| Factory | Inputs → products |
| Programming language | Problems → programs |
| Scientific method | Questions → experiments → knowledge |
| Self-improving discovery system | Discovery → better discovery |

---

# Anti-recursion principle

The framework rejects unnecessary ontological layers.

Rule:

$$
\boxed{
\textbf{
Do not add a new entity when a trajectory variable explains the phenomenon.
}
}
$$

Higher-order behavior is represented through dynamics:

$$
X
\rightarrow
\dot X
\rightarrow
\ddot X
$$

not

$$
X
\rightarrow
X_{meta}
\rightarrow
X_{meta^2}
$$

Therefore:

$$
\boxed{
\text{Meta is not a location.}
}
$$

$$
\boxed{
\text{Meta is a property of transformation dynamics.}
}
$$

---

# Empirical program

The framework is not complete until the latent variables become measurable.

## Measuring $G_m$

Can we identify when a system begins modifying its own improvement mechanisms?

Possible proxies:

- reduced iteration cost
- reusable improvement infrastructure
- abstraction creation
- automated method generation
- increased search efficiency

---

## Measuring reachable space

Possible proxies:

- number of reachable solution classes
- search efficiency
- representation compression
- tool leverage
- exploration breadth

---

## Testing $\Omega$

The central prediction:

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

# Historical case studies

Potential test cases:

- Scientific method
- Printing press
- Programming languages
- Compilers
- Automatic differentiation
- Machine learning
- Automated scientific discovery

Each case asks:

1. Did $G_m$ change?
2. Did $\Omega$ increase?
3. Did capability acceleration follow?

---

# Status

Early research framework.

Current goals:

- formalize definitions
- develop measurable proxies
- build simulations
- analyze historical transitions
- attempt falsification

---

# Core invariant

$$
\boxed{
\textbf{
Higher-order adaptive behavior is not a higher object.
It is the dynamics of lower-order adaptive processes.
}
}
$$

The framework studies the point where systems stop merely adapting to the world and begin adapting the mechanisms by which they adapt.
