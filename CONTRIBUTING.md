# Contributing to Adaptive Evolutionary Dynamics

Thank you for your interest in contributing.

Adaptive Evolutionary Dynamics is an open research framework exploring how adaptive systems transition from improving within existing constraints to modifying the mechanisms that generate future improvements.

Contributions are welcome across:

- mathematical formalization
- theoretical analysis
- empirical validation
- historical case studies
- measurement methodology
- simulations
- documentation
- critical review

The goal is not only to extend the framework, but to improve its ability to make precise, testable claims.

---

# Core Contribution Principle

The framework follows a strict anti-recursion constraint.

> **Prefer trajectory variables over new ontological categories.**

Before introducing a new entity, ask:

1. Is this a genuinely new causal mechanism?
2. Does it produce measurable predictions?
3. Or is it better represented as a derivative or transformation of existing variables?

Avoid adding unnecessary abstraction layers.

---

# Research Philosophy

The framework is built around several core distinctions.

## State vs. Dynamics

A **state** describes what currently exists.

$$
X_t
$$

A **dynamic** describes how the system changes.

$$
X_{t+1}=F(X_t,E_t,u_t)
$$

Contributions should clearly distinguish between:

- new state variables
- new transition rules
- new measurement methods

---

## Capability vs. Evolutionary Velocity

| Quantity | Meaning |
|----------|---------|
| $C$ | What a system can currently do |
| $\Omega$ | How quickly the system improves its capability-generation process |

Do **not** use capability growth alone as evidence of evolutionary acceleration.

---

## Possibility vs. Reachability

The framework studies reachable future spaces,

$$
\mathcal{P}^{reach}
$$

rather than abstract possibility spaces.

When proposing new work, consider:

- available resources
- representations
- search mechanisms
- generator mechanisms
- environmental constraints

A possibility that cannot be reached by the system is not part of its operational future space.

---

# Types of Contributions

## Mathematical Formalization

Examples include:

- improving definitions
- proving relationships
- identifying assumptions
- reducing ambiguity
- developing formal models

Strong mathematical contributions should clarify:

- variables
- operators
- observables
- causal relationships

---

## Empirical Studies

The framework ultimately requires measurable evidence.

Useful studies include:

- historical analyses
- comparative case studies
- simulation experiments
- quantitative proxies for adaptive depth
- tests of the predicted ordering

$$
\Delta G_m
\rightarrow
\Delta\Omega
\rightarrow
\Delta C
$$

---

## Measurement Research

One of the largest open problems is operationalization.

Especially valuable contributions include measurements or proxies for:

- generator modification capacity
- reachable future spaces
- evolutionary velocity
- adaptive depth

---

## Critical Analysis

Strong criticism is encouraged.

Useful critiques include:

- identifying hidden assumptions
- proposing falsification tests
- demonstrating where existing theories explain the phenomenon better
- identifying cases where predictions fail

A framework becomes stronger by surviving attempts to break it.

---

# Repository Structure

Suggested organization:

```text
/
├── README.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
│
├── theory/
│   ├── definitions.md
│   ├── equations.md
│   └── assumptions.md
│
├── empirical/
│   ├── case-studies/
│   └── datasets/
│
├── simulations/
├── docs/
└── discussions/
```

---

# Pull Request Guidelines

Before submitting a pull request:

1. Explain the motivation.
2. Identify which part of the framework is affected.
3. State whether the contribution modifies:
   - ontology
   - dynamics
   - measurement
   - empirical evidence
4. Include reasoning and references where appropriate.

A good pull request answers the question:

> **What does this change allow us to measure, predict, or explain that we could not before?**

---

# Naming and Definitions

Please avoid introducing terms that duplicate existing concepts.

Before adding a new concept, ask:

- Is this a new object?
- Is this a new process?
- Is this a new measurement?
- Is this simply a derivative of an existing variable?

Prefer describing changes in dynamics, for example,

$$
\dot{X}
$$

rather than introducing additional ontological layers such as

$$
X_{meta}
$$

unless a genuinely new causal entity is required.

---

# Discussion Guidelines

When proposing changes, make the following explicit.

## Claim

What is being proposed?

## Mechanism

What causal process produces it?

## Observable

How could it be measured?

## Falsification

What evidence would show it is wrong?

---

# Code Contributions

For simulations or computational experiments, please include:

- clear assumptions
- reproducible parameters
- explanation of metrics
- limitations
- expected behavior

Code should support the theory, not replace explanation.

---

# Versioning

The project uses Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

- `0.1.0` — Initial public research framework
- `0.2.0` — New theoretical or empirical capabilities
- `1.0.0` — Stable validated framework

---

# Final Principle

The purpose of this project is not to create another hierarchy of concepts.

It is to understand the dynamics by which systems change the mechanisms that produce future change.

The guiding question is

$$
\boxed{
\text{What determines the evolution of the function that generates evolution?}
}
$$

Contributions should help answer that question with increasing precision.
