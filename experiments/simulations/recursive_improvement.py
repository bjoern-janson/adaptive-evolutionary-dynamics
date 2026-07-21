"""
generator_adaptation.py

Generator Adaptation Simulator

Purpose:
    Model the transition from systems that improve outputs
    to systems that improve the mechanisms producing outputs.

Framework mapping:

    D0:
        Z -> Z'

        State adaptation

    D1:
        Gs -> Gs'

        Search adaptation

    D2:
        Gm -> Gm'

        Generator adaptation

    D3:
        Ω -> Ω'

        Generator-dynamics adaptation


Core distinction:

    Capability growth:

        C(t+1) = F(C_t)

    Generator adaptation:

        Gm(t+1) = F(Gm_t)

    Evolutionary acceleration:

        Ω ≈ ΔGm


This simulation isolates the effect of improving
the improvement mechanism itself.
"""

from dataclasses import dataclass
from typing import List, Dict
import math


@dataclass
class GeneratorState:
    """
    Adaptive generator state.

    Corresponds to:

        X_t =
        (
            C_t,
            G_s,t,
            G_m,t,
            Ω_t
        )
    """

    capability: float = 1.0

    # Search efficiency
    search_capacity: float = 1.0

    # Ability to improve search
    generator_capacity: float = 0.1

    # Rate at which generator improves itself
    generator_dynamics: float = 0.0

    history: List[Dict] = None


    def __post_init__(self):

        if self.history is None:
            self.history = []



class GeneratorAdaptiveSystem:
    """
    System where the adaptive target can move.

    The central experiment:

        Does improving Gm produce
        accelerating capability growth?

    Expected ordering:

        ΔGm
          ↓
        ΔΩ
          ↓
        ΔC
    """


    def __init__(
        self,
        generator_learning_rate=0.05,
        meta_learning_rate=0.0,
    ):

        self.state = GeneratorState()

        self.generator_learning_rate = (
            generator_learning_rate
        )

        self.meta_learning_rate = (
            meta_learning_rate
        )


    def reachable_space(self):
        """
        Proxy:

            |P_reach|

        Reachability increases with:

            C
            Gs
            Gm
        """

        s = self.state

        return (
            1
            +
            s.capability
            *
            s.search_capacity
            *
            (1 + s.generator_capacity)
        )


    def omega(self):
        """
        Evolutionary velocity proxy.

        In the framework:

            Ω = ΔG

        Here:

            Ω ≈ d(Gm)/dt
        """

        return (
            self.state.generator_dynamics
        )


    def update_state(self):

        s = self.state


        # D2:
        # Generator adaptation

        old_generator = (
            s.generator_capacity
        )


        s.generator_capacity += (
            self.generator_learning_rate
            *
            (1 + s.search_capacity)
        )


        delta_generator = (
            s.generator_capacity
            -
            old_generator
        )


        # D3:
        # Generator dynamics adaptation

        old_dynamics = (
            s.generator_dynamics
        )


        s.generator_dynamics += (
            self.meta_learning_rate
            *
            delta_generator
        )


        delta_omega = (
            s.generator_dynamics
            -
            old_dynamics
        )


        # Capability response

        capability_gain = (
            1
            +
            0.1 * s.search_capacity
            +
            0.5 * s.generator_capacity
        )


        s.capability *= (
            capability_gain
        )


        # Search improvement from generator

        s.search_capacity += (
            0.01
            *
            s.generator_capacity
        )


        return {
            "capability":
                s.capability,

            "search_capacity":
                s.search_capacity,

            "generator_capacity":
                s.generator_capacity,

            "delta_generator":
                delta_generator,

            "omega":
                self.omega(),

            "delta_omega":
                delta_omega,

            "reachable_space":
                self.reachable_space(),
        }



    def run(self, steps=20):

        results = []

        for _ in range(steps):

            result = self.update_state()

            self.state.history.append(
                result
            )

            results.append(
                result
            )

        return results



def compare_systems():

    """
    Compare:

        System A:
            improves solutions

        System B:
            improves solution generators
    """

    baseline = GeneratorAdaptiveSystem(
        generator_learning_rate=0.0,
        meta_learning_rate=0.0,
    )


    generator_system = GeneratorAdaptiveSystem(
        generator_learning_rate=0.05,
        meta_learning_rate=0.01,
    )


    print(
        "\n=== Fixed Generator ==="
    )

    for i, result in enumerate(
        baseline.run(10)
    ):
        print(
            i,
            result["capability"]
        )


    print(
        "\n=== Improving Generator ==="
    )

    for i, result in enumerate(
        generator_system.run(10)
    ):
        print(
            i,
            result["capability"]
        )



if __name__ == "__main__":

    compare_systems()
