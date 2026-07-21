"""
Phase Boundary Test

Tests the Adaptive Evolutionary Dynamics hypothesis:

    ΔG_m → ΔΩ → ΔC

where:

    G_m      = generator modification capacity
    Ω        = evolutionary velocity proxy
    C        = capability

The experiment compares:

1. Fixed Generator:
   - capability growth
   - constant improvement mechanism

2. Improving Generator:
   - self-modifying improvement mechanism
   - accelerating capability production
"""


import math


def compute_omega(capability_history, gm_history):
    """
    Estimate evolutionary velocity.

    Ω ≈ d/dt(ΔC / ΔG_m)

    Measures whether the return from generator
    improvement is increasing.
    """

    efficiency = []

    for i in range(1, len(capability_history)):

        delta_c = capability_history[i] - capability_history[i-1]

        delta_gm = gm_history[i] - gm_history[i-1]

        if delta_gm == 0:
            efficiency.append(0)
        else:
            efficiency.append(delta_c / delta_gm)

    if len(efficiency) < 2:
        return 0

    omega = efficiency[-1] - efficiency[0]

    return omega



def fixed_generator(steps=10):

    capability = 1.15
    generator = 1.0

    C = []
    G = []

    for t in range(steps):

        C.append(capability)
        G.append(generator)

        # fixed improvement mechanism
        capability *= 1.15

        # generator stays constant
        generator = generator


    omega = compute_omega(C, G)

    return C, G, omega



def improving_generator(steps=10):

    capability = 1.20

    generator = 1.0

    generator_growth = 0.15

    C = []
    G = []

    for t in range(steps):

        C.append(capability)
        G.append(generator)

        # generator improves itself
        generator *= (1 + generator_growth)

        # improvement rate increases
        generator_growth *= 1.15

        # capability benefits from generator improvement
        capability *= generator


    omega = compute_omega(C, G)

    return C, G, omega



def print_results(name, C, G, omega):

    print("\n==============================")
    print(name)
    print("==============================")

    print()

    print("t | Capability | Generator")

    print("----------------------------")

    for i in range(len(C)):

        print(
            f"{i:2d} | "
            f"{C[i]:10.3f} | "
            f"{G[i]:10.3f}"
        )


    print()

    print("Final Capability:")
    print(f"{C[-1]:.3f}")

    print()

    print("Generator Change:")
    print(f"{G[-1]-G[0]:.3f}")

    print()

    print("Ω (evolutionary velocity proxy):")
    print(f"{omega:.5f}")



def main():

    fixed_C, fixed_G, fixed_omega = fixed_generator()

    improving_C, improving_G, improving_omega = improving_generator()


    print_results(
        "Fixed Generator",
        fixed_C,
        fixed_G,
        fixed_omega
    )


    print_results(
        "Improving Generator",
        improving_C,
        improving_G,
        improving_omega
    )


    print("\n\nPHASE BOUNDARY RESULT")
    print("====================")


    if improving_omega > fixed_omega:

        print(
            """
Evidence consistent with:

        ΔG_m → ΔΩ → ΔC

The improving generator produces
higher evolutionary velocity.
"""
        )

    else:

        print(
            """
No evolutionary acceleration detected.
"""
        )



if __name__ == "__main__":
    main()
