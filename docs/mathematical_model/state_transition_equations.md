# State Transition Equations

> Canonical dynamical system for Adaptive Evolutionary Dynamics.

---

# Overview

The framework models adaptive systems as evolving over a finite state space.

Rather than viewing capability as the primary state variable, capability is treated as the downstream consequence of changes in generator dynamics, execution, and reachable space.

The complete system state is:

$$
\boxed{
S_t=
(G_t,A_t,X_t,P_t,C_t,R_t)
}
$$

where:

- \(G_t\) — Generator quality
- \(A_t\) — Adoption state
- \(X_t\) — Execution / alignment capacity
- \(P_t\) — Reachable frontier
- \(C_t\) — Capability
- \(R_t\) — Resources

---

# State Variables

## Generator

Generator quality represents the system's ability to create future improvements.

$$
G_t\ge0
$$

Examples:

- compiler technology
- scientific methodology
- optimization algorithms
- learning rules

Generator quality determines the potential for future adaptation.

It does not directly produce capability.

---

## Adoption

Adoption measures how much of the generator has been incorporated into the active system.

$$
0\le A_t\le G_t
$$

Examples:

- deployment
- education
- tooling
- infrastructure

A generator may exist without widespread adoption.

---

## Execution Capacity

Execution capacity measures whether the adopted generator can actually be used.

$$
0\le X_t\le1
$$

Examples:

- institutional compatibility
- compute availability
- organizational alignment
- engineering maturity

Execution is distinct from adoption.

A system may possess a generator and adopt it while remaining unable to operationalize it.

---

## Reachable Frontier

The reachable frontier measures the volume of accessible future states.

$$
P_t\ge0
$$

It represents the effective search space available to the adaptive system.

Unlike raw state space, the reachable frontier depends on the current adaptive machinery.

---

## Capability

Capability is the realized performance of the system.

$$
C_t
$$

Examples:

- prediction accuracy
- scientific output
- engineering productivity
- technological performance

Capability follows the reachable frontier rather than directly following the generator.

---

## Resources

Resources include external inputs that support capability growth.

$$
R_t
$$

Examples:

- compute
- labor
- capital
- energy
- data

Resources increase capacity but do not necessarily improve the adaptive process.

---

# State Transitions

The framework proposes the following dependency graph:

$$
\boxed{
G
\rightarrow
A
\rightarrow
X
\rightarrow
P
\rightarrow
C
}
$$

with resources acting as an external modifier:

$$
R
\rightarrow
C
$$

---

# Generator Dynamics

Generator evolution is modeled as:

$$
G_{t+1}=f_G(G_t)
$$

Possible implementations include:

- logistic growth
- innovation processes
- stochastic discovery
- endogenous learning

---

# Adoption Dynamics

Adoption depends on generator quality and current adoption.

$$
A_{t+1}=f_A(G_t,A_t)
$$

Example:

$$
A_{t+1}
=
A_t
+
\rho(G_t-A_t)
$$

where:

$$
\rho
$$

is the adoption rate.

---

# Execution Dynamics

Execution capacity depends on adoption and external constraints.

$$
X_{t+1}
=
f_X(A_t,X_t,\Theta)
$$

where:

$$
\Theta
$$

represents environmental constraints.

Examples:

- institutions
- hardware
- regulations
- coordination costs

---

# Reachable Frontier Dynamics

The reachable frontier expands according to:

$$
P_{t+1}
=
f_P(P_t,A_t,X_t)
$$

One possible implementation:

$$
P_{t+1}
=
P_t
+
\beta
A_t
X_t
P_t
\left(
1-\frac{P_t}{K}
\right)
$$

where:

$$
K
$$

is the maximum reachable frontier.

Execution therefore gates frontier expansion.

If:

$$
X=0
$$

then:

$$
P_{t+1}=P_t
$$

Generator improvement alone is insufficient.

---

# Capability Dynamics

Capability follows the reachable frontier.

$$
C_{t+1}
=
f_C(C_t,P_t,R_t)
$$

A simple implementation:

$$
C_{t+1}
=
C_t
+
\alpha(P_t-C_t)
+
g(R_t)
$$

where:

$$
g(R_t)
$$

captures direct resource effects.

---

# Evolutionary Velocity

Evolutionary velocity measures the rate at which adaptive capacity changes.

$$
\boxed{
\Omega
=
\frac{dG_m}{dt}
}
$$

Operational proxies may instead estimate:

$$
\hat{\Omega}
=
\frac{d\Lambda}{dt}
$$

where:

$$
\Lambda
$$

is frontier velocity.

---

# Phase Boundary

A phase boundary occurs when generator improvement propagates through the full state transition chain.

$$
\boxed{
\Delta G
\rightarrow
\Delta A
\rightarrow
\Delta X
\rightarrow
\Delta P
\rightarrow
\Delta C
}
$$

Missing any intermediate transition weakens or prevents capability acceleration.

---

# Failure Modes

The framework predicts several distinct failure modes.

## Generator Failure

$$
\Delta G\approx0
$$

No adaptive transition occurs.

---

## Adoption Failure

$$
\Delta G>0
$$

but:

$$
\Delta A\approx0
$$

The generator exists but is not deployed.

---

## Execution Failure

$$
\Delta A>0
$$

but:

$$
X\approx0
$$

The system cannot operationalize the adopted generator.

---

## Frontier Failure

Execution succeeds but frontier expansion remains constrained.

$$
\Delta P\approx0
$$

Examples:

- hard physical limits
- saturated search spaces
- insufficient representation quality

---

## Capability Failure

The frontier expands but realized capability does not.

Examples:

- insufficient resources
- delayed exploitation
- measurement limitations

---

# Central Hypothesis

The framework predicts that sustained adaptive acceleration requires successful propagation through every state transition.

$$
\boxed{
G
\rightarrow
A
\rightarrow
X
\rightarrow
P
\rightarrow
C
}
$$

Capability is therefore interpreted as the endpoint of a causal chain rather than the primary object of optimization.
