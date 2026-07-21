# 05_evolutionary_velocity.md

# Evolutionary Velocity (Ω)

## Overview

Evolutionary Velocity, denoted by:

\[
\boxed{
\Omega
}
\]

is the central dynamical quantity of the Adaptive Evolutionary Architecture.

It measures not the amount of capability a system possesses, but the rate at which the system improves the mechanisms responsible for producing future capability.

The central distinction:

\[
\boxed{
C \neq \Omega
}
\]

where:

\[
C=\text{current capability}
\]

and:

\[
\Omega=\text{capability-generation acceleration}
\]

A system may have high capability but low evolutionary velocity.

A system may have modest capability but rapidly increasing evolutionary velocity.

---

# 1. Motivation

Traditional growth metrics measure:

\[
\frac{dC}{dt}
\]

the rate at which capability changes.

However, this treats capability as the endpoint.

The framework asks a deeper question:

> What determines the rate at which capability itself can improve?

The relevant object is not:

\[
C(t)
\]

but:

\[
\frac{dC}{dt}
\]

and not merely:

\[
\frac{dC}{dt}
\]

but:

\[
\frac{d}{dt}
\left(
\frac{dC}{dt}
\right)
\]

or more generally:

\[
\boxed{
\text{the dynamics of capability production}
}
\]

---

# 2. Reachable Future Space

Define:

\[
\mathcal{P}^{reach}_{evo}(t)
\]

as the set of evolutionary transformations reachable by the system at time \(t\).

Formally:

\[
\boxed{
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
}
\]

This is not the total space of imaginable futures.

It is constrained by:

\[
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
\]

The distinction:

\[
\boxed{
\text{possible futures}
\neq
\text{reachable futures}
}
\]

---

# 3. Raw Reachable Expansion

The total rate of reachable-space expansion is:

\[
\boxed{
\Lambda(t)
=
\frac{d}{dt}
\log
|
\mathcal{P}^{reach}_{evo}(t)
|
}
\]

Expanded:

\[
\boxed{
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
}
\]

This measures:

\[
\boxed{
\text{How quickly the accessible future frontier expands}
}
\]

However:

\[
\Lambda
\]

is not identical to:

\[
\Omega
\]

because expansion may occur from multiple sources.

---

# 4. Expansion Decomposition

The total expansion rate:

\[
\boxed{
\Lambda
=
\Delta_R
+
\Delta_C
+
\Delta_G
}
\]

where:

---

## Resource contribution

Additional substrate:

\[
R
=
\{
compute,
energy,
capital,
labor,
data
\}
\]

Contribution:

\[
\boxed{
\Delta_R
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial R
}
\dot R
}
\]

Examples:

- more computational power
- more funding
- larger workforce
- more available data

---

## Capability contribution

Improvement through existing mechanisms:

\[
\boxed{
\Delta_C
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial C
}
\dot C
}
\]

Examples:

- accumulated knowledge
- better execution
- refinement of existing methods

---

## Generator contribution

Expansion caused by improving the mechanisms that create improvements:

\[
\boxed{
\Delta_G
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial G_m
}
\dot G_m
}
\]

This is the quantity of interest.

---

# 5. Definition of Evolutionary Velocity

The core definition:

\[
\boxed{
\Omega
\equiv
\Delta_G
}
\]

or:

\[
\boxed{
\Omega
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial G_m
}
\dot G_m
}
\]

Therefore:

\[
\boxed{
\Omega
=
\text{reachable future expansion caused by improving future-improvement mechanisms}
}
\]

---

# 6. Interpretation

The difference:

## Normal growth

\[
R
\rightarrow
C
\]

Resources produce capability.

---

## Learning

\[
C
\rightarrow
C'
\]

Existing mechanisms improve.

---

## Evolutionary acceleration

\[
G_m
\rightarrow
\Omega
\rightarrow
C'
\]

The system improves the machinery responsible for producing improvements.

---

# 7. Capability vs Evolutionary Velocity

Capability:

\[
\boxed{
C
=
|\mathcal{P}^{reach}_{current}|
}
\]

Measures:

\[
\text{what the system can currently do}
\]

---

Evolutionary velocity:

\[
\boxed{
\Omega
=
\Delta_G
}
\]

Measures:

\[
\text{how quickly the system improves what it can eventually do}
\]

---

Examples:

## High C, low Ω

A mature industrial process.

\[
C\uparrow
\]

but:

\[
G_m\approx constant
\]

The system performs extremely well but does not improve its improvement process.

---

## Low C, high Ω

An emerging research field.

Current capability may be limited:

\[
C\approx low
\]

but:

\[
G_m\uparrow
\]

and:

\[
\Omega\uparrow
\]

Future capability may accelerate rapidly.

---

# 8. Relation to Generator Capacity

Generator modification:

\[
\boxed{
G_m:
G_s(t)
\rightarrow
G_s(t+1)
}
\]

defines the mechanism capable of modifying search.

However:

\[
G_m\neq\Omega
\]

because:

\[
G_m
\]

is a mechanism.

\[
\Omega
\]

is the resulting dynamical effect.

The relationship:

\[
\boxed{
G_m
\rightarrow
\dot G_m
\rightarrow
\Omega
}
\]

---

# 9. Temporal Prediction

The framework predicts:

\[
\boxed{
\Delta G_m
\rightarrow
\Delta\Omega
\rightarrow
\Delta C
}
\]

with:

\[
\boxed{
t_{G_m}
<
t_{\Omega}
<
t_C
}
\]

Meaning:

1. The improvement mechanism changes.
2. The rate of capability production changes.
3. Capability growth becomes visible.

---

# 10. Distinguishing Ω From Ordinary Growth

A system with:

\[
R\uparrow
\]

may produce:

\[
C\uparrow
\]

without:

\[
\Omega\uparrow
\]

Example:

Adding more workers increases output.

But unless the organization improves how it creates better organizations:

\[
\Omega
\]

may remain unchanged.

---

The defining test:

\[
\boxed{
\Omega
\neq
\dot C
}
\]

Instead:

\[
\boxed{
\Omega
=
\text{change in the capability-production function}
}
\]

---

# 11. Measurement Approximation

The ideal quantity is difficult to observe.

A practical estimator:

\[
\boxed{
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
}
\]

Meaning:

Measure whether the return on improvement mechanisms increases over time.

---

A system with:

\[
\frac{\Delta C}{\Delta G_m}
=
constant
\]

has:

\[
\Omega\approx0
\]

A system where:

\[
\frac{\Delta C}{\Delta G_m}
\uparrow
\]

has:

\[
\Omega>0
\]

---

# 12. Relation to Dynamic Causal Mass

Static causal influence:

\[
\boxed{
\Phi(I)
=
\frac{\partial Z_{future}}
{\partial I}
}
\]

Dynamic causal influence:

\[
\boxed{
\Phi_D(I)
=
\frac{
\partial
\mathcal{P}^{reach}_{evo}
}{
\partial I
}
}
\]

The difference:

A normal intervention changes future states.

A high dynamic causal intervention changes the future production of future states.

---

# 13. Conceptual Compression

The framework hierarchy:

\[
\boxed{
C
=
\text{what can be produced}
}
\]

\[
\boxed{
G_s
=
\text{how possibilities are searched}
}
\]

\[
\boxed{
G_m
=
\text{how search mechanisms are improved}
}
\]

\[
\boxed{
\Omega
=
\text{how quickly improvement mechanisms improve}
}
\]

---

# Final Definition

\[
\boxed{
\Omega
=
\frac{
\partial
\log|\mathcal{P}^{reach}|
}{
\partial G_m
}
\dot G_m
}
\]

Evolutionary Velocity is:

\[
\boxed{
\textbf{
the rate at which a system improves the machinery responsible for expanding its own reachable future.}
}
\]

The central invariant:

\[
\boxed{
\text{Higher-order adaptive behavior is not another object.}
}
\]

\[
\boxed{
\text{It is the changing dynamics of lower-order adaptive processes.}
}
\]
