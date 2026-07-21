"""
causal_analysis.py

Adaptive Evolutionary Architecture

Causal Identification Layer.

Purpose:

Estimate whether observed capability acceleration is caused by
changes in generator dynamics (G_m) rather than:

    ΔR  = resource scaling
    ΔC  = ordinary capability improvement

Core causal question:

    Did the system become better at improving itself?

Framework:

    ΔG_m → ΔΩ → ΔC

The goal is not correlation.

The goal is attribution.

"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math


# ============================================================
# Intervention Model
# ============================================================


@dataclass
class Intervention:
    """
    Historical transformation event.

    Example:

        compiler
        scientific method
        automatic differentiation

    """

    name: str

    timestamp: float

    system: str

    description: str



# ============================================================
# Causal Variables
# ============================================================


@dataclass
class CausalObservation:
    """
    Measurement snapshot.

    """

    time: float

    capability: float

    resources: float

    generator_capacity: float

    reachable_space: float



# ============================================================
# Difference Estimation
# ============================================================


def delta(
    before: float,
    after: float
) -> float:
    """
    Simple change estimator.

    """

    return after - before



# ============================================================
# Growth Decomposition
# ============================================================


@dataclass
class GrowthDecomposition:
    """

    Λ = ΔR + ΔC + ΔG

    """

    total_growth: float

    resource_component: float

    capability_component: float

    generator_component: float



    def residual(self) -> float:

        return (
            self.total_growth
            -
            self.resource_component
            -
            self.capability_component
        )



# ============================================================
# Reachability Growth
# ============================================================


def reachable_growth(
    previous_size: float,
    current_size: float,
    dt: float
) -> float:
    """

    Λ(t)

    =

    d/dt log |P^reach|

    """

    if (
        previous_size <= 0
        or current_size <= 0
        or dt <= 0
    ):
        return 0.0


    return (
        math.log(current_size)
        -
        math.log(previous_size)
    ) / dt



# ============================================================
# Generator Effect Estimation
# ============================================================


def generator_effect(
    capability_before: float,
    capability_after: float,
    gm_before: float,
    gm_after: float
) -> float:
    """

    Estimate:

        ∂C / ∂G_m

    Approximation:

        ΔC / ΔG_m

    """

    delta_gm = gm_after - gm_before

    if delta_gm == 0:
        return 0.0


    return (
        capability_after
        -
        capability_before
    ) / delta_gm



# ============================================================
# Omega Identification
# ============================================================


def estimate_omega(
    efficiency_before: float,
    efficiency_after: float,
    dt: float
) -> float:
    """

    Evolutionary velocity:

        Ω

        =
        Δ(
            ΔC / ΔG_m
        )
        /
        Δt


    """

    if dt <= 0:
        return 0.0


    return (
        efficiency_after
        -
        efficiency_before
    ) / dt



# ============================================================
# Confound Control
# ============================================================


@dataclass
class ConfoundAssessment:
    """
    Separates:

        generator effects

    from:

        resources
        ordinary optimization

    """

    resource_growth: float

    capability_growth: float

    generator_growth: float



    def generator_dominant(
        self,
        threshold: float = 0.5
    ) -> bool:

        total = (
            abs(self.resource_growth)
            +
            abs(self.capability_growth)
            +
            abs(self.generator_growth)
        )

        if total == 0:
            return False


        return (
            abs(self.generator_growth)
            /
            total
        ) > threshold



# ============================================================
# Temporal Ordering Test
# ============================================================


@dataclass
class PhaseOrdering:
    """

    Required:

        t_Gm < t_Omega < t_C

    """

    t_generator: float

    t_omega: float

    t_capability: float



    def supported(self) -> bool:

        return (
            self.t_generator
            <
            self.t_omega
            <
            self.t_capability
        )



# ============================================================
# Comparative Causal Test
# ============================================================


@dataclass
class SystemComparison:
    """

    Controls:

        similar resources
        similar capability

    Compare:

        Ω

    """

    name_a: str

    name_b: str

    resources_a: float

    resources_b: float

    capability_a: float

    capability_b: float

    omega_a: float

    omega_b: float



def causal_prediction(
    comparison: SystemComparison
) -> Dict[str, bool]:
    """

    Prediction:

        Ω_A > Ω_B

    implies:

        C_A_future > C_B_future

    """

    return {

        "resource_control":
            abs(
                comparison.resources_a
                -
                comparison.resources_b
            )
            <
            0.1,

        "capability_control":
            abs(
                comparison.capability_a
                -
                comparison.capability_b
            )
            <
            0.1,

        "omega_difference":
            comparison.omega_a
            >
            comparison.omega_b

    }



# ============================================================
# Falsification Engine
# ============================================================


@dataclass
class FalsificationResult:

    generator_change: bool

    omega_change: bool

    capability_change: bool

    resource_explanation: bool



    def framework_supported(self) -> bool:

        return (
            self.generator_change
            and
            self.omega_change
            and
            self.capability_change
            and
            not self.resource_explanation
        )



def evaluate_case(
    delta_gm: float,
    delta_omega: float,
    delta_c: float,
    delta_r: float
) -> FalsificationResult:
    """

    Evaluate historical event.

    """

    return FalsificationResult(

        generator_change =
            delta_gm > 0,

        omega_change =
            delta_omega > 0,

        capability_change =
            delta_c > 0,

        resource_explanation =
            (
                delta_r
                >
                delta_gm
            )
    )



# ============================================================
# Example
# ============================================================


if __name__ == "__main__":


    ordering = PhaseOrdering(
        t_generator=10,
        t_omega=20,
        t_capability=50
    )


    print(
        "Temporal prediction:",
        ordering.supported()
    )


    result = evaluate_case(
        delta_gm=1.5,
        delta_omega=0.8,
        delta_c=10,
        delta_r=2
    )


    print(
        "Framework supported:",
        result.framework_supported()
    )
