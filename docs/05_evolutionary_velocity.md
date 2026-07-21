# Evolutionary Velocity (Ω)

## Overview

Evolutionary Velocity, denoted by:

$$
\Omega
$$

is the central dynamical quantity of the Adaptive Evolutionary Architecture.

It measures not the amount of capability a system possesses, but the rate at which the system improves the mechanisms responsible for producing future capability.

The central distinction:

$$
C \neq \Omega
$$

where:

$$
C=\text{current capability}
$$

and:

$$
\Omega=\text{capability-generation acceleration}
$$

A system may have high capability but low evolutionary velocity.

A system may have modest capability but rapidly increasing evolutionary velocity.

---

# 1. Motivation

Traditional growth metrics measure:

$$
\frac{dC}{dt}
$$

the rate at which capability changes.

However, this treats capability as the endpoint.

The framework asks:

> What determines the rate at which capability itself can improve?

The relevant object is not only:

$$
C(t)
$$

but:

$$
\frac{dC}{dt}
$$

and more generally:

$$
\frac{d}{dt}
\left(
\frac{dC}{dt}
\right)
$$

The target quantity is:

$$
\text{the dynamics of capability production}
$$

---

# 2. Reachable Future Space

Define:

$$
\mathcal{P}^{reach}_{evo}(t)
$$

as the set of evolutionary transformations reachable by the system at time $t$.

Formally:

$$
\mathcal{P}^{reach}_{evo}(t)
=
\{
\tau:
E_t\rightarrow E_{t+k}
\mid
\tau
\text{ reachable under }
X_t,R_t
\}
$$

This is not the total space of imaginable futures.

It is constrained by:

$$
X_t
=
(
Z_t,
M_t,
\pi_t,
V_t,
C_t,
G_s,
G_m,
R_t
)
$$

The distinction:

$$
\text{possible futures}
\neq
\text{reachable futures}
$$

---

# 3. Raw Reachable Expansion

The total rate of reachable-space expansion is:

$$
\Lambda(t)
=
\frac{d}{dt}
\log
|
\mathcal{P}^{reach}_{evo}(t)
|
$$

Equivalent form:

$$
\Lambda(t)
=
\frac{
1
}{
|\mathcal{P}^{reach}_{evo}(t)|
}
\frac{
d
|\mathcal{P}^{reach}_{evo}(t)|
}{
dt
}
$$

This measures:

$$
\text{how quickly the accessible future frontier expands}
$$

However:

$$
\Lambda
$$

is not identical to:

$$
\Omega
$$

because expansion can occur from multiple sources.

---

# 4. Expansion Decomposition

The total expansion rate:

$$
\Lambda
=
\Delta_R
+
\Delta_C
+
\Delta_G
$$

where:

---

## Resource Contribution

Additional substrate:

$$
R=
\{
\text{compute},
\text{energy},
\text{capital},
\text{labor},
\text{data}
\}
$$

Contribution:

$$
\Delta_R
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial R
}
\dot R
$$

Examples:

- more computational power
- more funding
- larger workforce
- more available data

---

## Capability Contribution

Improvement through existing mechanisms:

$$
\Delta_C
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial C
}
\dot C
$$

Examples:

- accumulated knowledge
- better execution
- refinement of existing methods

---

## Generator Contribution

Expansion caused by improving the mechanisms that create improvements:

$$
\Delta_G
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial G_m
}
\dot G_m
$$

This is the quantity of interest.

---

# 5. Definition of Evolutionary Velocity

The core definition:

$$
\Omega
\equiv
\Delta_G
$$

or:

$$
\Omega
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial G_m
}
\dot G_m
$$

Therefore:

$$
\Omega
=
\text{reachable future expansion caused by improving future-improvement mechanisms}
$$

---

# 6. Interpretation

## Normal Growth

$$
R
\rightarrow
C
$$

Resources produce capability.

---

## Learning

$$
C
\rightarrow
C'
$$

Existing mechanisms improve.

---

## Evolutionary Acceleration

$$
G_m
\rightarrow
\Omega
\rightarrow
C'
$$

The system improves the machinery responsible for producing improvements.

---

# 7. Capability vs Evolutionary Velocity

Capability:

$$
C
=
|\mathcal{P}^{reach}_{current}|
$$

Measures:

$$
\text{what the system can currently do}
$$

---

Evolutionary velocity:

$$
\Omega
=
\Delta_G
$$

Measures:

$$
\text{how quickly the system improves what it can eventually do}
$$

---

## High Capability, Low Ω

A mature industrial process.

$$
C\uparrow
$$

but:

$$
G_m\approx constant
$$

The system performs well but does not improve its improvement process.

---

## Low Capability, High Ω

An emerging research field.

Current capability may be limited:

$$
C\approx low
$$

but:

$$
G_m\uparrow
$$

and:

$$
\Omega\uparrow
$$

Future capability may accelerate rapidly.

---

# 8. Relation to Generator Capacity

Generator modification:

$$
G_m:
G_s(t)
\rightarrow
G_s(t+1)
$$

defines the mechanism capable of modifying search.

However:

$$
G_m\neq\Omega
$$

because:

$$
G_m
$$

is a mechanism.

$$
\Omega
$$

is the resulting dynamical effect.

The relationship:

$$
G_m
\rightarrow
\dot G_m
\rightarrow
\Omega
$$

---

# 9. Temporal Prediction

The framework predicts:

$$
\Delta G_m
\rightarrow
\Delta\Omega
\rightarrow
\Delta C
$$

with:

$$
t_{G_m}
<
t_{\Omega}
<
t_C
$$

Meaning:

1. The improvement mechanism changes.
2. The rate of capability production changes.
3. Capability growth becomes visible.

---

# 10. Distinguishing Ω From Ordinary Growth

A system with:

$$
R\uparrow
$$

may produce:

$$
C\uparrow
$$

without:

$$
\Omega\uparrow
$$

Example:

Adding more workers increases output.

But unless the organization improves how it creates better organizations:

$$
\Omega
$$

may remain unchanged.

---

The defining distinction:

$$
\Omega
\neq
\dot C
$$

Instead:

$$
\Omega
=
\text{change in the capability-production function}
$$

---

# 11. Measurement Approximation

The ideal quantity is difficult to observe.

A practical estimator:

$$
\hat{\Omega}
=
\frac{
\Delta
(
\Delta C/\Delta G_m
)
}{
\Delta t
}
$$

Meaning:

Measure whether the return on improvement mechanisms increases over time.

A system with:

$$
\frac{\Delta C}{\Delta G_m}
=
constant
$$

has:

$$
\Omega\approx0
$$

A system where:

$$
\frac{\Delta C}{\Delta G_m}
\uparrow
$$

has:

$$
\Omega>0
$$

---

# 12. Relation to Dynamic Causal Mass

Static causal influence:

$$
\Phi(I)
=
\frac{\partial Z_{future}}
{\partial I}
$$

Dynamic causal influence:

$$
\Phi_D(I)
=
\frac{
\partial
\mathcal{P}^{reach}_{evo}
}{
\partial I
}
$$

The difference:

A normal intervention changes future states.

A high dynamic causal intervention changes the future production of future states.

---

# 13. Conceptual Compression

The framework hierarchy:

$$
C
=
\text{what can be produced}
$$

$$
G_s
=
\text{how possibilities are searched}
$$

$$
G_m
=
\text{how search mechanisms are improved}
$$

$$
\Omega
=
\text{how quickly improvement mechanisms improve}
$$

---

# Final Definition

$$
\Omega
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial G_m
}
\dot G_m
$$

Evolutionary Velocity is:

$$
\textbf{
the rate at which a system improves the machinery responsible for expanding its own reachable future.
}
$$

The central invariant:

$$
\text{Higher-order adaptive behavior is not another object.}
$$

$$
\text{It is the changing dynamics of lower-order adaptive processes.}
$$
