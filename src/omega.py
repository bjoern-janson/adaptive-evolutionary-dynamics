"""
omega.py

Adaptive Evolutionary Architecture

Evolutionary Velocity Measurement Layer.

Core concept:

    Ω

is not capability growth.

It is the internally generated acceleration
of capability-generation dynamics.

The framework distinguishes:

    Λ(t)
        Total reachable-space expansion

    ΔR
        Resource-driven expansion

    ΔC
        Capability-driven expansion

    ΔG
        Generator-driven expansion

    Ω
        Measured evolutionary contribution

Formally:

    Λ = ΔR + ΔC + ΔG

    Ω ≈ ΔG

Operational estimator:

    Ω_hat =
        Δ(ΔC / ΔG_m) / Δt

Meaning:

    Is the system becoming better
    at converting improvement mechanisms
    into future capability?

"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
import math


# ============================================================
# Reachable Space Expansion
# ============================================================


@dataclass
class ReachableState:
    """
    Approximation of reachable future space.

    True:

        P^reach(t)

    cannot be enumerated.

    This is an empirical proxy.

    """

    timestamp: float

    reachable_size: float

    capability: float

    generator_score: float

    resources: float



# ============================================================
# Lambda: Total Frontier Expansion
# ============================================================


def log_growth_rate(
    previous_space: float,
    current_space: float,
    delta_time: float
) -> float:
    """
    Compute:

        Λ(t)
        =
        d/dt log |P^reach|

    """

    if (
        previous_space <= 0
        or delta_time <= 0
    ):
        return 0.0


    return (
        math.log(current_space)
        -
        math.log(previous_space)
    ) / delta_time



# ============================================================
# Resource / Capability / Generator Decomposition
# ============================================================


@dataclass
class ExpansionComponents:
    """
    Decomposition:

        Λ =
        ΔR + ΔC + ΔG

    """

    resource_component: float

    capability_component: float

    generator_component: float



def decompose_expansion(
    resource_effect: float,
    capability_effect: float,
    generator_effect: float
) -> ExpansionComponents:
    """
    Store causal attribution estimates.

    In practice these values would come
    from experimental identification.

    """

    return ExpansionComponents(
        resource_effect,
        capability_effect,
        generator_effect
    )



# ============================================================
# Omega Estimator
# ============================================================


@dataclass
class OmegaMeasurement:
    """
    Single Ω estimate.

    """

    delta_capability: float

    delta_generator: float

    delta_time: float



    def estimate(self) -> float:
        """
        Approximation:

            Ω_hat =
            Δ(ΔC / ΔG_m)
            /
            Δt

        """

        if (
            self.delta_generator == 0
            or self.delta_time == 0
        ):
            return 0.0


        return (
            (
                self.delta_capability
                /
                self.delta_generator
            )
            /
            self.delta_time
        )



# ============================================================
# Evolutionary Velocity Tracker
# ============================================================


@dataclass
class OmegaTracker:
    """
    Tracks changes in:

        capability-generation efficiency

    """

    history: List[OmegaMeasurement] = field(
        default_factory=list
    )


    def add(
        self,
        measurement: OmegaMeasurement
    ):

        self.history.append(
            measurement
        )


    def current(self) -> float:

        if not self.history:
            return 0.0

        return self.history[-1].estimate()



    def trend(self) -> float:
        """
        Positive:

            Ω increasing

        Negative:

            Ω decreasing

        """

        if len(self.history) < 2:
            return 0.0


        return (
            self.history[-1].estimate()
            -
            self.history[-2].estimate()
        )



# ============================================================
# Phase Boundary Detection
# ============================================================


@dataclass
class PhaseBoundarySignal:
    """
    Tests:

        ΔG_m
          ↓
        ΔΩ
          ↓
        ΔC

    """

    generator_change: float

    omega_change: float

    capability_change: float



    def detected(
        self,
        threshold: float = 0.0
    ) -> bool:
        """

        A positive transition requires:

            ΔG_m > 0
            ΔΩ > 0
            ΔC > 0

        """

        return (
            self.generator_change > threshold
            and
            self.omega_change > threshold
            and
            self.capability_change > threshold
        )



# ============================================================
# Causal Identification
# ============================================================


def omega_residual(
    total_growth: float,
    resource_growth: float,
    capability_growth: float
) -> float:
    """
    Residual estimate:

        Ω ≈ Λ - ΔR - ΔC

    Used when direct generator attribution
    is unavailable.

    """

    return (
        total_growth
        -
        resource_growth
        -
        capability_growth
    )



# ============================================================
# Comparative Test
# ============================================================


def compare_systems(
    omega_a: float,
    omega_b: float,
    capability_a_future: float,
    capability_b_future: float
) -> Dict[str, bool]:
    """
    Main empirical prediction:

        Ω_A > Ω_B

        implies:

        C_A(t+τ) > C_B(t+τ)

    """

    return {

        "higher_omega":
            omega_a > omega_b,

        "higher_future_capability":
            capability_a_future
            >
            capability_b_future,

        "prediction_supported":
            (
                omega_a > omega_b
                and
                capability_a_future
                >
                capability_b_future
            )
    }



# ============================================================
# Example
# ============================================================


if __name__ == "__main__":


    measurement = OmegaMeasurement(
        delta_capability=100,
        delta_generator=10,
        delta_time=5
    )


    omega = measurement.estimate()


    print(
        "Ω estimate:",
        omega
    )


    signal = PhaseBoundarySignal(
        generator_change=0.8,
        omega_change=0.5,
        capability_change=1.2
    )


    print(
        "Phase boundary detected:",
        signal.detected()
    )
