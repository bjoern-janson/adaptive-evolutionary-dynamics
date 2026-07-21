# Adaptive Depth

## Overview

Adaptive Depth describes **where a system's adaptation process terminates**.

The central claim is:

\[
\boxed{
D=\text{target of adaptation}
}
\]

Depth is not a measure of:

- intelligence
- complexity
- scale
- abstraction
- organizational size

Instead, it identifies the **causal object modified by feedback**.

A system becomes deeper not when it becomes larger, but when feedback penetrates further into the machinery responsible for producing future states.

---

# Core Principle

Every adaptive system contains:

1. A state
2. A mechanism for changing the state
3. A mechanism for changing the mechanism

The key question is:

> What does feedback modify?

The answer determines adaptive depth.

---

# Adaptive Depth Hierarchy

The framework defines four primary depths:

\[
\boxed{
D_0,D_1,D_2,D_3
}
\]

Each represents a deeper target of modification.

---

# D₀ — State Adaptation

## Definition

Feedback modifies the current configuration.

\[
\boxed{
Z_{t+1}=f(Z_t,O_t)
}
\]

The system changes itself without changing how it changes.

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

A thermostat:

\[
\text{temperature error}
\rightarrow
\text{heater adjustment}
\]

---

## Characteristics

The transformation rule remains fixed.

\[
f_t=f_{t+1}
\]

The system improves within a predefined space.

---

# D₁ — Search Adaptation

## Definition

Feedback modifies exploration strategy.

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

A researcher changes experimental strategy.

A chess player improves opening selection.

A machine-learning system changes its exploration policy.

---

## Characteristics

The system no longer only changes answers.

It changes the process used to find answers.

---

# D₂ — Generator Adaptation

## Definition

Feedback modifies the mechanisms that produce search processes.

\[
\boxed{
G_{m,t+1}
=
f(G_{m,t},G_{s,t},M_t,O_t)
}
\]

The system improves the machinery that generates methods.

---

## Examples

Scientific methodology:

\[
\text{observation}
\rightarrow
\text{experiment}
\rightarrow
\text{improved experimental method}
\]

Programming languages:

\[
\text{manual computation}
\rightarrow
\text{compiler}
\rightarrow
\text{better programming tools}
\]

Organizations:

\[
\text{workflow}
\rightarrow
\text{process optimization}
\]

---

## Characteristics

The system can modify the mechanisms responsible for producing improvements.

This is the transition from:

\[
\text{adaptation}
\]

to:

\[
\text{adaptive adaptation}
\]

---

# D₃ — Generator Dynamics Adaptation

## Definition

Feedback modifies the rate at which generators improve.

\[
\boxed{
\Omega_{t+1}
=
f(\Omega_t,G_m,G_s,M,O)
}
\]

The system changes its own improvement dynamics.

---

## The Key Transition

D₂:

\[
G_m\uparrow
\]

The system improves its generators.

D₃:

\[
\frac{dG_m}{dt}\uparrow
\]

The system improves the rate at which it improves generators.

---

# Meta Without Infinite Regression

A major constraint of the framework:

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

The adaptive depth model instead uses:

\[
X
\rightarrow
\dot X
\rightarrow
\ddot X
\]

Higher-order behavior is a property of trajectories.

---

# Depth Is Not Scale

The framework separates:

\[
S=\text{scale}
\]

from:

\[
D=\text{adaptive depth}
\]

A single person can operate at high depth:

\[
(S,D)=
(\text{micro},D_2)
\]

by developing systems for self-improvement.

A large institution can operate at low depth:

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
\mathcal A_t
=
(S_t,D_t,X_t,\Theta_t)
}
\]

where:

\[
D_t=
\operatorname{Target}(Feedback_t)
\]

The depth variable identifies the destination of adaptive modification.

---

# Relationship to Evolutionary Velocity

Adaptive depth determines whether evolutionary velocity is possible.

The causal progression:

\[
D_0
\rightarrow
D_1
\rightarrow
D_2
\rightarrow
D_3
\]

corresponds to increasing penetration of feedback into the system's transformation machinery.

The critical transition:

\[
\boxed{
D_2\rightarrow D_3
}
\]

because the system begins modifying the dynamics of capability generation itself.

---

# Empirical Prediction

Systems exhibiting higher adaptive depth should show:

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

Generator modification precedes measurable acceleration, which precedes visible capability growth.

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
\text{how complex the system appears}
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
A system becomes more adaptive when feedback modifies deeper parts of the process that produces future change.
}
}
