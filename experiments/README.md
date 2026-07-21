# Experiments

This directory contains empirical designs, datasets, benchmarks, and analyses for testing the Adaptive Evolutionary Dynamics Framework.

The purpose of experiments is not to demonstrate that the framework is correct, but to determine whether its central variables can be operationalized and whether its predictions survive comparison against alternative explanations.

The primary empirical question:

$$
\boxed{
\text{Does improvement of capability-generation machinery precede measurable capability acceleration?}
}
$$

---

# Experimental Objective

The framework predicts that major adaptive transitions should follow the ordering:

$$
\boxed{
\Delta G_m
\rightarrow
\Delta \Omega
\rightarrow
\Delta C
}
$$

where:

- \(G_m\) = generator modification capacity
- \(\Omega\) = evolutionary velocity
- \(C\) = capability

The experimental goal is to test whether this ordering appears historically and experimentally.

---

# Core Experimental Pipeline

Each experiment follows:

$$
\boxed{
\text{System}
\rightarrow
\text{Intervention}
\rightarrow
\Delta G_m
\rightarrow
\Delta \Omega
\rightarrow
\Delta C
}
$$

## Step 1: Identify the adaptive system

Examples:

- scientific communities
- engineering organizations
- software ecosystems
- AI research systems
- biological systems
- economic institutions

---

## Step 2: Identify the intervention

The intervention should represent a change to the capability-generation process.

Examples:

- introduction of the scientific method
- creation of programming languages
- invention of compilers
- automatic differentiation
- automated experimentation systems

---

## Step 3: Estimate generator modification

Measure whether the system gained mechanisms that improve future improvement.

Possible proxies:

$$
G_m
\rightarrow
\{
\Delta L,
\Delta A,
\Delta I,
\Delta T
\}
$$

where:

- \(\Delta L\): reduction in description length of procedures
- \(\Delta A\): increase in accessible approaches
- \(\Delta I\): reusable infrastructure creation
- \(\Delta T\): reduced iteration cost

---

## Step 4: Estimate evolutionary velocity

Measure whether the capability-generation process itself accelerated.

Target:

$$
\Omega
=
\frac{
\partial \log|\mathcal{P}^{reach}|
}
{\partial G_m}
\dot G_m
$$

Operational approximation:

$$
\hat{\Omega}
=
\frac{
\Delta(\Delta C/\Delta G_m)
}
{\Delta t}
$$

---

## Step 5: Compare against capability growth

The key distinction:

Capability increase:

$$
\Delta C>0
$$

is insufficient.

The question:

$$
\boxed{
\Delta\Omega>0
\Rightarrow
\Delta C_{future}\gg0?
}
$$

---

# Experiment Classes

## 1. Historical Phase Transition Studies

Purpose:

Test whether major technological or scientific transitions show the predicted ordering.

Candidate cases:

- Scientific Revolution
- Industrial Revolution
- Programming languages
- Compilers
- Internet protocols
- Machine learning frameworks
- Automatic differentiation

Example:

Manual computation:

$$
\text{human procedure}
$$

↓

Compiler:

$$
\text{language}
\rightarrow
\text{automated transformation}
$$

Prediction:

$$
G_m\uparrow
$$

before:

$$
C\uparrow\uparrow
$$

---

# 2. Controlled Organizational Experiments

Compare systems with similar resources but different improvement machinery.

Setup:

System A:

$$
R_A\approx R_B
$$

System B:

$$
G_{m,B}>G_{m,A}
$$

Prediction:

$$
\Omega_B>\Omega_A
$$

followed by:

$$
C_B>C_A
$$

---

# 3. AI System Experiments

Potential applications:

- automated machine learning
- AI research assistants
- automated theorem proving
- self-improving software systems

Questions:

Does a system merely solve tasks?

or:

Does it improve the process producing solutions?

---

# 4. Benchmark Construction

Possible benchmark dimensions:

## Generator Improvement Score

Measures:

$$
G_m
$$

Questions:

- Does the system create reusable methods?
- Does it reduce future search cost?
- Does it improve its own workflow?

---

## Reachability Expansion Score

Measures:

$$
|\mathcal{P}^{reach}|
$$

Questions:

- How many new solution trajectories become accessible?
- How many constraints are removed?
- How much search space becomes practical?

---

## Evolutionary Velocity Score

Measures:

$$
\Omega
$$

Questions:

- Does improvement accelerate?
- Does each generation of improvements create faster improvement?

---

# Required Controls

Experiments must separate:

## Resource effects

$$
\Delta_R
$$

Examples:

- more compute
- more funding
- more workers

---

## Capability effects

$$
\Delta_C
$$

Examples:

- accumulated expertise
- optimization
- refinement

---

## Generator effects

$$
\Delta_G
$$

Examples:

- improved methods
- improved search
- improved transformation mechanisms

---

The framework is only supported if:

$$
\boxed{
\Delta_G
\not\approx
\Delta_R+\Delta_C
}
$$

---

# Falsification Criteria

The framework is weakened if:

## 1. Capability transitions occur without prior generator changes

$$
\Delta C
\not\Rightarrow
\Delta G_m
$$

---

## 2. Generator changes do not predict future acceleration

$$
\Delta G_m
\not\Rightarrow
\Delta\Omega
$$

---

## 3. Apparent evolutionary velocity is fully explained by resources

$$
\Omega
\approx
\Delta_R
$$

---

## 4. No measurable proxy distinguishes high-\(G_m\) systems from ordinary improving systems.

---

# Experiment Template

Each experiment should contain:
