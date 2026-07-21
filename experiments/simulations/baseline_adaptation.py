"""
baseline_adaptation.py

Baseline adaptive-system simulator.

Purpose:
    Provide a minimal reference implementation of the Adaptive Evolutionary
    Architecture.

This module does NOT attempt to model intelligence.
It provides a simple dynamical system where:

    R  = available resources
    C  = current capability
    Gs = search capability
    Gm = generator-modification capability
    Ω  = evolutionary velocity proxy

The goal is to separate:

    resource-driven growth
        from

    generator-driven acceleration

Framework mapping:

    X_{t+1} = F_X(X_t, E_t, u_t)

    Λ = d/dt log(|P_reach|)

    Ω ≈ ΔG

This is intentionally minimal and acts as a baseline
for future empirical experiments.
"""

from dataclasses import dataclass
from typing import Dict, List
import math


@dataclass
class AdaptiveState:
    """
    System configuration.

    Corresponds to:

        X_t =
        (
            C_t,
            G_s,t,
            G_m,t,
            R_t
        )
    """

    capability: float = 1.0
    search_capacity: float = 1.0
    generator_capacity: float = 0.0
    resources: float = 1.0

    # Observable history
    history: List[Dict] = None

    def __post_init__(self):
        if self.history is None:
            self.history = []


class AdaptiveSystem:
    """
    Minimal adaptive system.

    Three possible growth sources:

    1. Resource expansion
        R ↑ → C ↑

    2. Search improvement
        Gs ↑ → C ↑

    3. Generator improvement
        Gm ↑ → Ω ↑ → future C acceleration
    """

    def __init__(
        self,
        resource_growth=0.05,
        search_learning=0.02,
        generator_learning=0.0,
    ):
        self.state = AdaptiveState()

        self.resource_growth = resource_growth
        self.search_learning = search_learning
        self.generator_learning = generator_learning


    def reachable_space(self):
        """
        Approximation of:

            |P_reach|

        Not a literal possibility-space measurement.

        This proxy assumes reachable transformations increase with:

            resources
            capability
            search
            generator capacity
        """

        s = self.state

        return (
            1
            + s.resources
            * s.capability
            * (1 + s.search_capacity)
            * (1 + s.generator_capacity)
        )


    def lambda_velocity(self, previous_space):
        """
        Raw frontier expansion:

            Λ =
            d/dt log(|P_reach|)
        """

        current = self.reachable_space()

        if previous_space <= 0:
            return 0.0

        return math.log(current) - math.log(previous_space)


    def omega_estimate(self):
        """
        Proxy for evolutionary velocity.

        Framework definition:

            Ω ≈ ΔG

        Here approximated as generator contribution.
        """

        return self.state.generator_capacity


    def step(self):
        """
        Execute one adaptive timestep.

        Simplified dynamics:

            R_{t+1}
            =
            R_t + ΔR


            G_s,t+1
            =
            G_s,t + ΔGs


            G_m,t+1
            =
            G_m,t + ΔGm


            C_{t+1}
            =
            C_t * improvement_factor
        """

        s = self.state

        previous_space = self.reachable_space()


        # Resource expansion
        s.resources *= (
            1 + self.resource_growth
        )


        # Search adaptation
        s.search_capacity += (
            self.search_learning
        )


        # Generator adaptation
        s.generator_capacity += (
            self.generator_learning
        )


        # Capability growth
        improvement = (
            1
            +
            0.1 * s.search_capacity
            +
            0.2 * s.generator_capacity
        )

        s.capability *= improvement


        # Measurements
        record = {
            "capability": s.capability,
            "search_capacity": s.search_capacity,
            "generator_capacity": s.generator_capacity,
            "resources": s.resources,
            "reachable_space": self.reachable_space(),
            "lambda": self.lambda_velocity(
                previous_space
            ),
            "omega": self.omega_estimate(),
        }


        s.history.append(record)

        return record


    def run(self, steps=10):
        """
        Run simulation.
        """

        results = []

        for _ in range(steps):
            results.append(
                self.step()
            )

        return results



if __name__ == "__main__":

    print(
        "=== Baseline Adaptive System ==="
    )

    system = AdaptiveSystem(
        resource_growth=0.05,
        search_learning=0.02,
        generator_learning=0.01,
    )

    history = system.run(20)

    for t, state in enumerate(history):

        print(
            f"""
t={t}

Capability:
    {state['capability']:.3f}

Resources:
    {state['resources']:.3f}

Search:
    {state['search_capacity']:.3f}

Generator:
    {state['generator_capacity']:.3f}

Λ (frontier velocity):
    {state['lambda']:.4f}

Ω (generator velocity proxy):
    {state['omega']:.4f}
"""
        )
