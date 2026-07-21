# Adaptive Depth

## Overview

Adaptive Depth describes **where a system's adaptation process terminates**.

The central definition:

\[
\boxed{
D=\text{target of adaptation}
}
\]

Depth does not measure:

- intelligence
- complexity
- scale
- abstraction
- organizational size

Instead, it identifies the **causal object modified by feedback**.

A system becomes deeper not when it becomes larger, but when feedback reaches further into the machinery responsible for producing future states.

---

# Core Principle

Every adaptive system contains:

1. A state
2. A mechanism that changes the state
3. A mechanism that changes the mechanism

The defining question is:

> What does feedback modify?

The answer determines adaptive depth.

---

# Adaptive Depth Hierarchy

The framework defines four primary adaptive targets:

\[
\boxed{
D_0,D_1,D_2,D_3
}
\]

Each level represents feedback reaching a deeper causal layer.

---

# D₀ — State Adaptation

## Definition

Feedback modifies the current configuration.

\[
\boxed{
Z_{t+1}=f(Z_t,O_t)
}
\]

The system changes itself without changing the mechanism responsible for change.

---

## Examples

Learning a fact:

\[
\text{information}
\rightarrow
\text{memory update}
\]

Physical adaptation:

\[
\text{environment}
\rightarrow
\text{state adjustment}
\]

Thermostat:

\[
\text{temperature error}
\rightarrow
\text{heater adjustment}
\]

---

## Characteristics

The transformation rule remains fixed:

\[
f_t=f_{t+1}
\]

The system adapts within a predefined space.

---

# D₁ — Search Adaptation

## Definition

Feedback modifies the exploration strategy.

\[
\boxed{
G_{s,t+1}
=
f(G_{s,t},O_t)
}
\]

The system changes how it searches for solutions.

---

## Examples

Human:

- changing study strategies
- improving experimental design
- adopting better reasoning methods

AI:

- updating exploration policies
- improving optimization strategies

Science:

- changing research methodology

---

## Characteristics

The system no longer only changes answers.

It changes the process used to find answers.

The adaptive target becomes:

\[
\boxed{
\text{search process}
}
\]

---

# D₂ — Generator Adaptation

## Definition

Feedback modifies the mechanisms that produce search and solution-generation processes.

\[
\boxed{
G_{m,t+1}
=
f(G_{m,t},G_{s,t},M_t,O_t)
}
\]

The system improves the machinery responsible for producing better methods.

---

## Examples

Scientific methodology:

Before:

\[
\text{observation}
\rightarrow
\text{knowledge}
\]

After:

\[
\text{experimental method}
\rightarrow
\text{reliable knowledge production}
\]

---

Programming:

Before:

\[
\text{manual computation}
\]

After:

\[
\text{compiler}
\rightarrow
\text{automatic program generation}
\]

---

Organizations:

Before:

\[
\text{fixed workflow}
\]

After:

\[
\text{process optimization}
\rightarrow
\text{improved workflows}
\]

---

## Characteristics

The system modifies the mechanisms responsible for producing improvements.

The transition:

\[
\boxed{
\text{adaptation}
\rightarrow
\text{adaptive adaptation}
}
\]

---

# D₃ — Generator Dynamics Adaptation

## Definition

Feedback modifies the dynamics governing generator improvement.

\[
\boxed{
\Omega_{t+1}
=
f(\Omega_t,G_m,G_s,M,O)
}
\]

The system changes the rate at which its own improvement mechanisms evolve.

---

## Key Transition

D₂:

\[
\boxed{
G_m\uparrow
}
\]

The system improves its generators.

---

D₃:

\[
\boxed{
\frac{dG_m}{dt}\uparrow
}
\]

The system improves the rate at which it improves generators.

---

## Interpretation

D₂ creates better improvement mechanisms.

D₃ creates mechanisms that improve improvement mechanisms faster.

---

# Meta Without Infinite Regression

A major constraint:

\[
\boxed{
\text{Higher-order behavior should be represented by dynamics, not new entities.}
}
\]

A naive hierarchy:

\[
X
\rightarrow
X_{meta}
\rightarrow
X_{meta^2}
\rightarrow
...
\]

creates infinite regress.

The framework instead uses:

\[
X
\rightarrow
\dot X
\rightarrow
\ddot X
\]

Higher-order adaptation is represented as changing trajectories.

---

# Depth Is Not Scale

The framework separates:

\[
\boxed{
S=\text{scale}
}
\]

from:

\[
\boxed{
D=\text{adaptive depth}
}
\]

A single person may operate at high depth:

\[
(S,D)=
(\text{micro},D_2)
\]

by developing systems for improving their own learning.

A large institution may operate at low depth:

\[
(S,D)=
(\text{macro},D_0)
\]

if it only maintains inherited processes.

---

# Formal Representation

The adaptive system:

\[
\boxed{
\mathcal{A}_t
=
(S_t,D_t,X_t,\Theta_t)
}
\]

where:

\[
\boxed{
D_t=
\operatorname{Target}(Feedback_t)
}
\]

The depth variable identifies the causal target modified by adaptation.

---

# Relationship to Evolutionary Velocity

Adaptive depth determines whether evolutionary velocity can emerge.

The progression:

\[
\boxed{
D_0
\rightarrow
D_1
\rightarrow
D_2
\rightarrow
D_3
}
\]

represents increasing penetration of feedback into the machinery of transformation.

The critical transition:

\[
\boxed{
D_2\rightarrow D_3
}
\]

because the system begins modifying the dynamics of capability generation itself.

---

# Empirical Prediction

Higher adaptive depth should produce:

\[
\boxed{
D_2
\rightarrow
\Omega\uparrow
\rightarrow
C\uparrow\uparrow
}
\]

The expected ordering:

\[
\boxed{
t_{G_m}<t_{\Omega}<t_C
}
\]

Meaning:

1. Generator mechanisms change.
2. Evolutionary velocity increases.
3. Capability growth becomes visible.

---

# Summary

Adaptive Depth measures:

\[
\boxed{
\text{where feedback lands}
}
\]

not:

\[
\text{how impressive the system appears}
\]

The hierarchy:

\[
\boxed{
D_0:
\text{change state}
}
\]

\[
\boxed{
D_1:
\text{change search}
}
\]

\[
\boxed{
D_2:
\text{change generators}
}
\]

\[
\boxed{
D_3:
\text{change generator dynamics}
}
\]

The central invariant:

\[
\boxed{
\textbf{
A system becomes more deeply adaptive when feedback modifies deeper causal mechanisms responsible for producing future change.
}
}
\]
