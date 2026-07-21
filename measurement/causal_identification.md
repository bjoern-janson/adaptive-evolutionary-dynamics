# Causal Identification

## Overview

The central empirical challenge of the Adaptive Evolutionary Architecture is identifying whether observed capability growth originates from:

1. increased resources,
2. improved existing capabilities,
3. changes in the mechanisms that generate future improvements.

The framework defines the target quantity:

$$
\Omega
=
\Delta_G
$$

as the component of reachable-space expansion attributable to changes in generator dynamics.

Therefore, causal identification asks:

$$
\boxed{
\text{Did the system become better because it had more resources, or because it became better at improving itself?}
}
$$

---

# 1. The Identification Problem

Observed capability change:

$$
\Delta C
$$

is not sufficient evidence of evolutionary acceleration.

A general decomposition:

$$
\Delta C
=
f(R,C,G_s,G_m,E)
$$

where:

- \(R\) = resources
- \(C\) = current capability
- \(G_s\) = search mechanism
- \(G_m\) = generator-modification mechanism
- \(E\) = environment

The causal question:

$$
\boxed{
\frac{\partial C_{future}}{\partial G_m}
>
\frac{\partial C_{future}}{\partial R}
}
$$

Is improvement machinery itself producing disproportionate future gains?

---

# 2. Counterfactual Definition

The causal effect of generator improvement is:

$$
\Phi_G(I)
=
C_{future}(G_m+\Delta G_m)
-
C_{future}(G_m)
$$

where:

- \(I\) is an intervention affecting generator mechanisms.
- \(C_{future}\) is future reachable capability.

The counterfactual comparison:

$$
Y(1)-Y(0)
$$

where:

$$
Y(1)
=
\text{future capability with generator intervention}
$$

$$
Y(0)
=
\text{future capability without generator intervention}
$$

---

# 3. Required Controls

A valid test must control for:

## Resource changes

$$
\Delta R
$$

Examples:

- compute
- funding
- labor
- energy
- data

---

## Existing capability

$$
C_t
$$

A system already ahead may simply continue ahead.

---

## Environmental changes

$$
\Delta E
$$

Examples:

- market changes
- scientific discoveries
- external shocks

---

The comparison:

$$
R_A\approx R_B
$$

$$
C_A\approx C_B
$$

$$
E_A\approx E_B
$$

while:

$$
G_{m,A}>G_{m,B}
$$

Prediction:

$$
C_A(t+\tau)>C_B(t+\tau)
$$

---

# 4. Difference-in-Differences Formulation

A possible empirical design:

$$
Y_{it}
=
\alpha_i
+
\lambda_t
+
\beta G_{m,it}
+
\epsilon_{it}
$$

where:

- \(Y\) = future capability growth
- \(\alpha_i\) = system fixed effects
- \(\lambda_t\) = time effects
- \(G_m\) = generator intervention

The key coefficient:

$$
\boxed{
\beta>0
}
$$

would support the claim that generator modification predicts accelerated capability growth.

---

# 5. Event Study Design

Many historical transitions occur around identifiable interventions.

Examples:

- manual calculation → programming languages
- handwritten mathematics → symbolic systems
- manual derivatives → automatic differentiation
- individual experiments → scientific method
- isolated invention → industrial R&D systems

Define:

$$
t_0
=
\text{generator transition point}
$$

Measure:

Before:

$$
t<t_0
$$

After:

$$
t>t_0
$$

Prediction:

$$
\Delta G_m(t_0)
\rightarrow
\Delta\Omega(t_0+\tau)
\rightarrow
\Delta C(t_0+\tau+\tau')
$$

---

# 6. Instrumental Variable Strategy

Generator improvement may itself be caused by hidden factors.

A possible identification strategy:

Find an instrument:

$$
Z
$$

such that:

$$
Z\rightarrow G_m
$$

but:

$$
Z\nrightarrow C
$$

except through \(G_m\).

Required conditions:

## Relevance

$$
Cov(Z,G_m)\neq0
$$

## Exclusion

$$
Z\perp C\mid G_m
$$

This is difficult but theoretically possible.

---

# 7. Granger Causality Test

A weaker temporal test:

Does generator change predict future capability?

Compare:

$$
C_{t+1}
=
f(C_t)
$$

against:

$$
C_{t+1}
=
f(C_t,G_{m,t})
$$

If:

$$
G_{m,t}
$$

improves prediction of:

$$
C_{t+1}
$$

then generator dynamics contain predictive information.

Formally:

$$
G_m
\rightarrow
C_{future}
$$

---

# 8. Mediation Model

The framework predicts mediation:

$$
G_m
\rightarrow
\Omega
\rightarrow
C
$$

not:

$$
G_m
\rightarrow
C
$$

directly.

Structural equation:

$$
\Omega_t
=
aG_{m,t}
+
bX_t
+
\epsilon
$$

$$
C_{t+\tau}
=
c\Omega_t
+
dX_t
+
\epsilon
$$

where \(X\) contains controls.

The prediction:

$$
a>0
$$

and:

$$
c>0
$$

---

# 9. Falsification Conditions

The framework is weakened if:

## Capability precedes generator change

Observed:

$$
C\uparrow
$$

before:

$$
G_m\uparrow
$$

---

## Resources explain all variance

Observed:

$$
\Delta C
\approx
\Delta R
$$

with:

$$
\Omega\approx0
$$

---

## Generator changes do not predict acceleration

Observed:

$$
G_m\uparrow
$$

but:

$$
\Omega\nuparrow
$$

---

## No temporal ordering

Observed:

$$
t_C<t_{G_m}
$$

contradicts:

$$
t_{G_m}<t_\Omega<t_C
$$

---

# 10. Practical Identification Pipeline

$$
\text{Historical transition}
$$

↓

$$
\text{Identify generator intervention}
$$

↓

$$
\Delta G_m
$$

↓

$$
\text{Estimate }\Omega
$$

↓

$$
\text{Measure delayed capability growth}
$$

↓

$$
\text{Compare against controls}
$$

---

# 11. Core Identification Principle

The framework does not attempt to prove:

$$
\text{innovation causes progress}
$$

That is already known.

The stronger claim is:

$$
\boxed{
\text{Changes in the mechanisms that produce innovation are measurable causal precursors of capability acceleration.}
}
$$

The identification target is therefore not:

$$
\Delta C
$$

but:

$$
\boxed{
\frac{\partial \Delta C}{\partial G_m}
}
$$

The central empirical question:

$$
\boxed{
\text{Does improving the generator of improvement create a measurable acceleration of future capability production?}
}
$$
