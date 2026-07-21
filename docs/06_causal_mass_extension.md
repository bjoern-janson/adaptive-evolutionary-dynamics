# 06 — Causal Mass Extension

# Overview

The Adaptive Evolutionary Architecture describes how systems expand their reachable future transformation space.

The Causal Mass extension asks a complementary question:

> How much does an intervention change the future trajectory of a system?

Traditional causal analysis focuses on immediate downstream effects.

This extension formalizes interventions that alter not only outcomes, but the mechanisms generating future outcomes.

The distinction:

$$
\text{Causal effect}
\neq
\text{Evolutionary causal effect}
$$

An intervention may change the world.

A higher-order intervention changes the process by which the world continues changing.

---

# 1. Static Causal Mass

Define ordinary causal influence:

$$
\Phi(I)
=
\frac{\partial Z_{future}}{\partial I}
$$

where:

- $I$ is an intervention
- $Z_{future}$ is the resulting future system state

This measures:

> How much does intervention $I$ alter future states?

Examples:

A hammer:

$$
I \rightarrow \text{physical outcome}
$$

A policy decision:

$$
I \rightarrow \text{social outcome}
$$

A new technology:

$$
I \rightarrow \text{capability increase}
$$

---

# 2. Dynamic Causal Mass

Some interventions modify the generator of future change.

Define:

$$
\Phi_D(I)
=
\frac{
\partial
\mathcal{P}^{reach}_{evo}(t+\Delta t)
}{
\partial I
}
$$

where:

$$
\mathcal{P}^{reach}_{evo}
$$

is the reachable future transformation space.

Dynamic causal mass measures:

> How much does an intervention alter the future capacity to generate future transformations?

---

# 3. Causal Hierarchy

The framework separates three intervention classes.

## Level 1 — State Intervention

Changes the current state.

$$
I \rightarrow Z
$$

Example:

- repairing a machine

---

## Level 2 — Capability Intervention

Changes what the system can do.

$$
I \rightarrow C
$$

Example:

- adding a new tool

---

## Level 3 — Generative Intervention

Changes the system that produces capabilities.

$$
I \rightarrow G_m
$$

Examples:

- scientific method
- compiler
- automated discovery system

---

The highest-impact interventions are not necessarily those with the largest immediate effects.

They are those that modify the future production function.

---

# 4. Intervention on Transformation Functions

Ordinary intervention:

$$
X_{t+1}=F(X_t,I)
$$

The intervention changes the trajectory.

Dynamic intervention:

$$
F_{t+1}=G(F_t,I)
$$

The intervention changes the transition function itself.

This is the key distinction.

The object being modified moves from:

$$
X
$$

to:

$$
F
$$

---

# 5. Causal Mass and Evolutionary Velocity

The relationship:

$$
\Phi_D
\rightarrow
G_m
\rightarrow
\Omega
$$

A high dynamic causal mass intervention should:

1. Modify generator mechanisms.
2. Increase evolutionary velocity.
3. Expand reachable future transformations.

The predicted sequence:

$$
I
\rightarrow
\Delta G_m
\rightarrow
\Delta\Omega
\rightarrow
\Delta C
$$

---

# 6. Examples

## Printing Press

Static view:

$$
\text{press}
\rightarrow
\text{more books}
$$

Dynamic view:

$$
\text{press}
\rightarrow
\text{knowledge transmission infrastructure}
$$

The intervention changes the reproduction rate of ideas.

---

## Programming Languages

Static view:

$$
\text{program}
\rightarrow
\text{computation}
$$

Dynamic view:

$$
\text{language}
\rightarrow
\text{new class of programs}
$$

The intervention expands the generator of future software.

---

## Scientific Method

Static view:

$$
\text{experiment}
\rightarrow
\text{knowledge}
$$

Dynamic view:

$$
\text{scientific method}
\rightarrow
\text{better discovery process}
$$

The method becomes a generator of improved methods.

---

## Automated Research Systems

Static:

$$
AI
\rightarrow
\text{answers}
$$

Dynamic:

$$
AI
\rightarrow
\text{improved discovery pipeline}
$$

The system changes future research capacity.

---

# 7. Causal Mass and Irreplaceability

The original causal mass intuition:

$$
\Phi(I)
=
D_{KL}
(
P(X|I)
||
P(X|\neg I)
)
$$

measures divergence between futures with and without an intervention.

The dynamic extension:

$$
\Phi_D(I)
=
D_{KL}
(
P(\mathcal{P}^{reach}_{evo}|I)
||
P(\mathcal{P}^{reach}_{evo}|\neg I)
)
$$

The question becomes:

Not:

> How different is the future because of this intervention?

But:

> How different is the future distribution of possible futures because of this intervention?

---

# 8. Swappability Test

An intervention has high causal mass if replacing it produces large changes.

Define:

$$
S(I)
=
D_{KL}
(
P(Future|I)
||
P(Future|I')
)
$$

where $I'$ is a plausible replacement intervention.

Low swappability:

$$
S(I)\gg0
$$

The intervention is causally unique.

High swappability:

$$
S(I)\approx0
$$

The intervention is replaceable.

---

# 9. Relationship to the Adaptive Framework

The complete relationship:

$$
\Phi_D
\rightarrow
G_m
\rightarrow
\Omega
\rightarrow
\mathcal{P}^{reach}_{evo}
\rightarrow
C
$$

Causal mass measures interventions.

Evolutionary velocity measures system dynamics.

Reachable space measures accessible futures.

Capability measures current outcomes.

---

# 10. Summary

Dynamic causal mass extends ordinary causal analysis by measuring interventions that modify future transformation capacity.

The central distinction:

$$
\text{A powerful intervention changes the future.}
$$

$$
\text{A transformative intervention changes how futures are produced.}
$$

The strongest interventions are therefore not necessarily those with the largest immediate effects.

They are those that alter the mechanisms generating future change.

$$
\Phi_D(I)
=
\text{causal influence over future transformation capacity}
$$
