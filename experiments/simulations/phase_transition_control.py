"""
Phase Transition Control Experiment

Tests the core hypothesis:

    ΔG_m → ΔΩ → ΔC

against alternative explanations.

Three systems:

1. Baseline:
   - Fixed resources
   - Fixed generator

2. Resource Scaling:
   - Increasing resources
   - Fixed generator

3. Evolutionary:
   - Fixed resources
   - Improving generator

The prediction:

If evolutionary acceleration is a distinct phenomenon:

    Ω_evolutionary > Ω_resource_scaling > Ω_baseline

and:

    ΔG_m precedes ΔC

"""

import math


class AdaptiveSystem:
    def __init__(
        self,
        name,
        capability=1.0,
        resources=1.0,
        generator=1.0,
        resource_growth=0.0,
        generator_growth=0.0,
    ):
        self.name = name
        self.capability = capability
        self.resources = resources
        self.generator = generator

        self.resource_growth = resource_growth
        self.generator_growth = generator_growth

        self.history = []

    def step(self, t):
        previous_generator = self.generator
        previous_capability = self.capability

        # Resource update
        self.resources *= (1 + self.resource_growth)

        # Generator update
        self.generator *= (1 + self.generator_growth)

        # Capability production
        productivity = (
            0.05
            * self.resources
            * self.generator
        )

        self.capability *= (
            1 + productivity
        )

        # Measurements
        delta_gm = self.generator - previous_generator

        capability_gain = (
            self.capability - previous_capability
        )

        omega_proxy = (
            capability_gain
            * delta_gm
        )

        self.history.append(
            {
                "t": t,
                "capability": self.capability,
                "resources": self.resources,
                "generator": self.generator,
                "delta_gm": delta_gm,
                "omega": omega_proxy,
            }
        )


def run(system, steps=15):

    for t in range(steps):
        system.step(t)

    return system


def print_results(system):

    print("\n")
    print("=" * 35)
    print(system.name)
    print("=" * 35)

    print(
        "\nt | Capability | Resources | Generator | Ω"
    )
    print("-" * 55)

    for row in system.history:
        print(
            f"{row['t']:2d} | "
            f"{row['capability']:10.3f} | "
            f"{row['resources']:9.3f} | "
            f"{row['generator']:9.3f} | "
            f"{row['omega']:10.5f}"
        )

    final = system.history[-1]

    print("\nFinal Capability:")
    print(
        f"{final['capability']:.3f}"
    )

    print("\nGenerator Change:")
    print(
        f"{final['generator'] - 1:.3f}"
    )

    print("\nΩ:")
    print(
        f"{final['omega']:.5f}"
    )


# -------------------------------------
# Experimental conditions
# -------------------------------------

baseline = AdaptiveSystem(
    name="Baseline Fixed System",
    resource_growth=0.0,
    generator_growth=0.0,
)


resource_scaled = AdaptiveSystem(
    name="Resource Scaling System",
    resource_growth=0.15,
    generator_growth=0.0,
)


evolutionary = AdaptiveSystem(
    name="Evolutionary Generator System",
    resource_growth=0.0,
    generator_growth=0.15,
)


# Run experiments

systems = [
    run(baseline),
    run(resource_scaled),
    run(evolutionary),
]


# Output

for system in systems:
    print_results(system)


# -------------------------------------
# Phase boundary comparison
# -------------------------------------

print("\n")
print("=" * 35)
print("PHASE BOUNDARY ANALYSIS")
print("=" * 35)

for system in systems:

    final = system.history[-1]

    print(
        f"\n{system.name}"
    )

    print(
        f"ΔGm = {final['generator'] - 1:.3f}"
    )

    print(
        f"Ω = {final['omega']:.5f}"
    )

    print(
        f"C = {final['capability']:.3f}"
    )


print("\nPrediction:")
print(
    """
If the framework is correct:

Evolutionary Generator System should show:

    ΔGm > 0
    Ω > resource scaling
    delayed capability acceleration

while resource scaling should show:

    ΔR > 0
    ΔGm ≈ 0
"""
)
