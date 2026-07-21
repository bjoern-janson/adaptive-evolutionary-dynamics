# Definitions

## Overview

This document defines the core terms of the Adaptive Evolutionary Architecture.

The framework studies adaptive systems that do not merely change their state, but modify the mechanisms responsible for producing future change.

The central distinction:

$$
\boxed{
\text{adaptation changes a system}
}
$$

$$
\boxed{
\text{evolutionary acceleration changes the system that changes systems}
}
$$

---

# Adaptive System

## Definition

An adaptive system is a system whose internal configuration changes in response to information from its environment.

Formally:

$$
X_{t+1}=F_X(X_t,E_t,u_t)
$$

where:

- \(X_t\) is internal configuration,
- \(E_t\) is environment,
- \(u_t\) is action.

An adaptive system changes itself based on observed consequences.

---

# Adaptation

## Definition

Adaptation is the process by which feedback modifies system configuration.

General form:

$$
\Delta X \neq 0
$$

The defining question:

$$
\boxed{
\text{What does feedback modify?}
}
$$

The answer determines adaptive depth.

---

# Adaptive Depth

## Definition

$$
D=\operatorname{Target}(Feedback)
$$

Adaptive depth describes the causal target of adaptation.

It does not represent:

- intelligence,
- complexity,
- abstraction,
- size.

It represents:

$$
\boxed{
\text{where the adaptive update terminates}
}
$$

---

# State Adaptation (D0)

## Definition

Feedback modifies the current configuration.

$$
Z_{t+1}=f(Z_t,O_t)
$$

Examples:

- learning a fact,
- correcting an error,
- changing physical state.

The system becomes different.

---

# Search Adaptation (D1)

## Definition

Feedback modifies the process used to explore possibilities.

$$
G_{s,t+1}=f(G_{s,t},O_t)
$$

Examples:

- improving strategy selection,
- changing research methods,
- refining optimization procedures.

The system changes how it finds solutions.

---

# Generator Adaptation (D2)

## Definition

Feedback modifies the mechanism that produces search or solution-generating processes.

$$
G_{m,t+1}
=
f(G_{m,t},G_s,M_t,O_t)
$$

Examples:

- scientific institutions,
- programming languages,
- automated discovery systems.

The system changes how it creates methods.

---

# Generator-Dynamics Adaptation (D3)

## Definition

Feedback modifies the rate at which generators improve.

$$
\Omega_{t+1}
=
f(\Omega_t,G_m,G_s,M_t,O_t)
$$

The system changes:

$$
\frac{dG_m}{dt}
$$

This is the transition associated with evolutionary acceleration.

---

# State Space

## Definition

The internal configuration of the system:

$$
X_t=
(Z_t,M_t,\pi_t,V_t,C_t,G_{s,t},G_{m,t},R_t)
$$

It represents what exists at time \(t\).

---

# Scale

## Definition

$$
S_t
$$

The location or organizational level at which adaptation occurs.

Examples:

$$
micro
$$

individual.

$$
meso
$$

organization.

$$
macro
$$

civilization.

Scale and depth are independent.

---

# Representation

## Definition

$$
M_t
$$

The internal model used by the system to interpret observations and select actions.

Observation:

$$
O_t=H(E_t)
$$

Update:

$$
M_{t+1}=U(M_t,O_t)
$$

Representations determine which transformations are visible or reachable.

---

# Policy / Controller

## Definition

$$
\pi_t
$$

The mechanism mapping internal information into action.

$$
u_t=\pi_t(M_t,V_t)
$$

---

# Search Mechanism

## Definition

$$
G_s
$$

The process by which the system explores reachable transformations.

Abstractly:

$$
G_s:
\mathcal{P}^{reach}_{current}
\rightarrow
\mathcal{P}^{explored}
$$

Examples:

- reasoning,
- experimentation,
- optimization,
- exploration algorithms.

---

# Generator Modification Mechanism

## Definition

$$
G_m
$$

The mechanism that modifies search or production mechanisms.

Formally:

$$
G_m:
G_s(t)
\rightarrow
G_s(t+1)
$$

A system with \(G_m\) can improve the process by which it finds improvements.

---

# Capability

## Definition

$$
C_t
$$

The currently reachable ability of a system.

Approximation:

$$
C_t=
|\mathcal{P}^{reach}_{current}(t)|
$$

Capability describes what can currently be achieved.

It does not describe how quickly capability changes.

---

# Reachable Transformation Space

## Definition

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

It is the set of transformations accessible to the system.

Important distinction:

$$
\boxed{
\text{possible}\neq\text{reachable}
}
$$

---

# Evolutionary Space

## Definition

$$
\mathcal{P}^{reach}_{evo}
$$

The subset of reachable transformations that modify future adaptive capacity.

It includes transformations that affect:

- search,
- generators,
- representations,
- improvement mechanisms.

---

# Reachable-Space Expansion

## Definition

The total rate at which accessible futures expand:

$$
\Lambda
=
\frac{d}{dt}
\log|\mathcal{P}^{reach}(t)|
$$

This measures expansion, not its cause.

---

# Evolutionary Velocity

## Definition

$$
\Omega=\Delta_G
$$

where:

$$
\Delta_G
=
\frac{\partial\log|\mathcal{P}^{reach}|}
{\partial G_m}
\dot G_m
$$

Meaning:

$$
\Omega
=
\text{rate at which the capability-generation process improves}
$$

---

# Growth

## Definition

Growth is an increase in current capability:

$$
\Delta C>0
$$

Growth can occur without evolutionary acceleration.

Example:

$$
R\uparrow
\rightarrow
C\uparrow
$$

without:

$$
\Omega\uparrow
$$

---

# Evolutionary Acceleration

## Definition

Evolutionary acceleration occurs when the system improves the mechanisms responsible for generating future improvements.

Formal signature:

$$
\Delta G_m
\rightarrow
\Delta\Omega
$$

It is a property of dynamics, not state.

---

# Resource Expansion

## Definition

Expansion caused by additional external substrate.

$$
\Delta_R
$$

Examples:

- more compute,
- more energy,
- more capital,
- more labor,
- more data.

Resource growth increases opportunity but does not imply adaptive depth.

---

# Causal Mass

## Definition

A measure of intervention influence.

Static causal mass:

$$
\Phi(I)
=
\frac{\partial Z_{future}}
{\partial I}
$$

Measures downstream state change.

---

# Dynamic Causal Mass

## Definition

$$
\Phi_D(I)
=
\frac{\partial\mathcal{P}^{reach}_{evo}}
{\partial I}
$$

Measures how an intervention changes future transformation capacity.

Difference:

$$
\Phi_D(I)\neq\Phi(I)
$$

---

# Artifact

## Definition

A stored result.

$$
A=x
$$

Examples:

- a tool,
- a document,
- a solution.

An artifact preserves an output.

---

# Primitive

## Definition

A stored transformation.

$$
P:x\rightarrow y
$$

A primitive preserves a process.

Examples:

- algorithms,
- methods,
- procedures.

---

# Evolutionary Primitive

## Definition

A stored transformation capable of modifying future transformations.

$$
P_e:f\rightarrow f'
$$

Examples:

- scientific method,
- programming languages,
- automated optimization systems.

---

# Phase Transition

## Definition

A phase transition occurs when the adaptive target changes.

Formal condition:

$$
D_{t+1}>D_t
$$

The system begins modifying deeper causal structures.

---

# Meta

## Definition

Meta is not an object.

It is a property of dynamics.

$$
\text{Meta}
=
\frac{d}{dt}
(\text{adaptive transformation})
$$

Higher-order behavior emerges from derivatives of existing dynamics.

---

# Anti-Recursion Principle

## Definition

The governing model-selection constraint:

$$
\boxed{
\text{Do not introduce a new entity when a trajectory variable explains the phenomenon.}
}
$$

Higher-order behavior should first be modeled as:

$$
X
\rightarrow
\dot X
\rightarrow
\ddot X
$$

before adding new state variables.

---

# Core Framework Compression

$$
C=\text{what the system can do}
$$

$$
G_s=\text{how the system finds things it can do}
$$

$$
G_m=\text{how the system improves how it finds things it can do}
$$

$$
\Omega=
\text{how quickly the system improves the machinery that produces future capability}
$$

The central object of study:

$$
\boxed{
\text{the dynamics of capability-generation dynamics}
}
$$
