# Notation

## Overview

This document defines the mathematical notation used throughout the Adaptive Evolutionary Architecture.

The framework separates:

1. **System state** — what exists at time \(t\)
2. **Dynamics** — how the system changes
3. **Reachability** — what futures are accessible
4. **Adaptive depth** — what feedback modifies
5. **Evolutionary velocity** — how quickly capability-generation dynamics improve

The notation is designed to prevent category errors between:

- states and processes,
- capabilities and improvement mechanisms,
- possibility and reachability,
- growth and acceleration.

---

# 1. Time

$$
t
$$

represents system time.

Discrete-time form:

$$
X_{t+1}=F(X_t,E_t,u_t)
$$

Continuous-time form:

$$
\dot X(t)=F(X(t),E(t),u(t))
$$

---

# 2. Adaptive System

The complete adaptive system:

$$
\mathcal{A}_t=(S_t,D_t,X_t,\Theta_t)
$$

where:

| Symbol | Meaning |
|---|---|
| \(S_t\) | scale |
| \(D_t\) | adaptive depth |
| \(X_t\) | internal configuration |
| \(\Theta_t\) | trajectory dynamics |

---

# 3. Scale

$$
S_t
$$

describes where adaptation occurs.

Example values:

$$
S_t\in\{micro,meso,macro\}
$$

Examples:

$$
micro=\text{individual}
$$

$$
meso=\text{organization}
$$

$$
macro=\text{civilization}
$$

Scale is independent of adaptive depth.

---

# 4. Internal Configuration

The internal state:

$$
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
$$

---

## 4.1 State

$$
Z_t
$$

Current system configuration.

Examples:

- physical state
- knowledge state
- organizational state
- computational state

---

## 4.2 Representation

$$
M_t
$$

The internal model or representation of the environment.

Observation transformation:

$$
O_t=H(E_t)
$$

Representation update:

$$
M_{t+1}=U(M_t,O_t)
$$

---

## 4.3 Policy / Controller

$$
\pi_t
$$

Maps internal representation to action.

$$
u_t=\pi_t(M_t,V_t)
$$

---

## 4.4 Value / Objective Function

$$
V_t
$$

Defines what outcomes are optimized.

Examples:

- reward functions
- goals
- selection criteria
- constraints

---

## 4.5 Capability

$$
C_t
$$

Current reachable ability.

Defined as:

$$
C_t=
|\mathcal{P}^{reach}_{current}(t)|
$$

Capability is a state property.

It does not measure improvement rate.

---

## 4.6 Search Mechanism

$$
G_{s,t}
$$

The mechanism that explores possible transformations.

Abstractly:

$$
G_s:
\mathcal{P}^{reach}_{current}
\rightarrow
\mathcal{P}^{explored}
$$

Examples:

- reasoning strategies
- experimental methods
- optimization algorithms
- search procedures

---

## 4.7 Generator Modification Mechanism

$$
G_{m,t}
$$

The mechanism that modifies search or production mechanisms.

$$
G_m:
G_s(t)\rightarrow G_s(t+1)
$$

Examples:

- scientific methodology
- compiler construction
- automated optimization systems
- self-improvement procedures

---

## 4.8 Resources

$$
R_t
$$

Available external substrate.

Examples:

- energy
- compute
- capital
- labor
- data
- infrastructure

Resources enable expansion but do not necessarily create evolutionary acceleration.

---

# 5. Environment

$$
E_t
$$

The external state interacting with the adaptive system.

Observation:

$$
O_t=H(E_t)
$$

Transition:

$$
E_{t+1}=F(E_t,u_t)
$$

---

# 6. Action

$$
u_t
$$

The selected intervention or output.

$$
u_t=\pi_t(M_t,V_t)
$$

---

# 7. Dynamics

The complete adaptive transition:

$$
X_{t+1}=F_X(X_t,E_t,u_t)
$$

The system evolves by transforming its own internal configuration.

---

# 8. Reachable Transformation Space

The central geometric object:

$$
\mathcal{P}^{reach}(t)
=
\{
\tau:
E_t\rightarrow E_{t+k}
\mid
\tau
\text{ reachable under }X_t,R_t
\}
$$

Meaning:

The set of transformations the system can actually produce.

---

## 8.1 Possible vs Reachable

Possible futures:

$$
\mathcal{P}
$$

Reachable futures:

$$
\mathcal{P}^{reach}
$$

The distinction:

$$
\mathcal{P}\neq\mathcal{P}^{reach}
$$

---

# 9. Reachable-Space Expansion

The total frontier growth rate:

$$
\Lambda(t)
=
\frac{d}{dt}
\log
|\mathcal{P}^{reach}(t)|
$$

\(\Lambda\) measures expansion, regardless of cause.

---

# 10. Growth Decomposition

Total expansion:

$$
\Lambda
=
\Delta_R+\Delta_C+\Delta_G
$$

---

## Resource Contribution

$$
\Delta_R
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial R}
\dot R
$$

Expansion caused by additional substrate.

---

## Capability Contribution

$$
\Delta_C
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial C}
\dot C
$$

Expansion from existing competence.

---

## Generator Contribution

$$
\Delta_G
=
\frac{\partial\log|\mathcal{P}^{reach}|}{\partial G_m}
\dot G_m
$$

Expansion caused by changing improvement mechanisms.

---

# 11. Evolutionary Velocity

The central variable:

$$
\Omega=\Delta_G
$$

Expanded:

$$
\Omega
=
\frac{\partial\log|\mathcal{P}^{reach}|}
{\partial G_m}
\dot G_m
$$

Interpretation:

$$
\Omega
=
\text{rate at which capability-generation dynamics improve}
$$

---

# 12. Adaptive Depth

$$
D=\operatorname{Target}(Feedback)
$$

Depth describes what feedback modifies.

---

## D0 — State Adaptation

$$
Z_{t+1}=f(Z_t,O_t)
$$

---

## D1 — Search Adaptation

$$
G_{s,t+1}=f(G_{s,t},O_t)
$$

---

## D2 — Generator Adaptation

$$
G_{m,t+1}
=
f(G_{m,t},G_s,M_t,O_t)
$$

---

## D3 — Generator Dynamics

$$
\Omega_{t+1}
=
f(\Omega_t,G_m,G_s,M_t,O_t)
$$

---

# 13. Causal Mass

## Static causal mass

$$
\Phi(I)
=
\frac{\partial Z_{future}}
{\partial I}
$$

Effect of intervention on future state.

---

## Dynamic causal mass

$$
\Phi_D(I)
=
\frac{\partial\mathcal{P}^{reach}_{evo}}
{\partial I}
$$

Effect of intervention on future transformation capacity.

---

# 14. Primitive Notation

## Artifact

Stored output:

$$
A=x
$$

---

## Primitive

Stored transformation:

$$
P:x\rightarrow y
$$

---

## Evolutionary Primitive

Stored transformation of transformations:

$$
P_e:f\rightarrow f'
$$

---

# 15. Meta Dynamics

No additional meta-objects are introduced.

System:

$$
X_{t+1}=F(X_t)
$$

Velocity:

$$
\dot X_t=\frac{dX}{dt}
$$

Acceleration:

$$
\ddot X_t=\frac{d^2X}{dt^2}
$$

Therefore:

$$
\text{Meta}
=
\frac{d}{dt}
(\text{adaptive transformation})
$$

---

# 16. Core Prediction

The phase transition ordering:

$$
\Delta G_m
\rightarrow
\Delta\Omega
\rightarrow
\Delta C
$$

Temporal form:

$$
t_{G_m}<t_\Omega<t_C
$$

---

# 17. Core Invariant

The framework's governing principle:

$$
\boxed{
\text{Higher-order adaptive behavior is not a higher object.}
}
$$

$$
\boxed{
\text{It is the dynamics of lower-order adaptive processes.}
}
$$

The stopping rule:

$$
\boxed{
\text{Do not add an entity when a trajectory variable explains the phenomenon.}
}
$$
