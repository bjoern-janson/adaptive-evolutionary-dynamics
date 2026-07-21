import math


# ============================================
# Long Horizon Phase Boundary Experiment
# ============================================
#
# Tests:
#
# ΔGm → ΔΩ → ΔC
#
# Compare:
#
# 1. Resource Scaling
#    Capability grows from increasing resources.
#
# 2. Evolutionary Generator
#    Capability grows from improving the improvement mechanism.
#
# Prediction:
#
# Resource system wins early.
# Generator system eventually crosses over.
#
# ============================================


TIMESTEPS = 100


# -----------------------------
# Model parameters
# -----------------------------

initial_capability = 1.0
initial_resources = 1.0
initial_generator = 1.0


# Resource growth
resource_growth = 1.15

# Resource saturation
resource_decay = 0.015


# Generator improvement
generator_growth = 1.15


# Capability sensitivity
alpha = 0.05



# ============================================
# Resource Scaling System
# ============================================

def run_resource_system():

    capability = initial_capability
    resources = initial_resources
    generator = initial_generator

    history = []

    for t in range(TIMESTEPS):

        history.append({
            "t": t,
            "capability": capability,
            "resources": resources,
            "generator": generator,
            "omega": 0
        })

        # capability improves from resources
        capability *= (1 + alpha * resources)

        # resources grow but saturate
        resources *= resource_growth
        resources *= math.exp(-resource_decay * resources)


    return history



# ============================================
# Evolutionary Generator System
# ============================================

def run_generator_system():

    capability = initial_capability
    resources = initial_resources
    generator = initial_generator

    history = []

    previous_generator = generator


    for t in range(TIMESTEPS):

        omega = generator - previous_generator

        history.append({
            "t": t,
            "capability": capability,
            "resources": resources,
            "generator": generator,
            "omega": omega
        })


        # capability grows through improved generator
        capability *= (1 + alpha * generator)


        # generator improves itself
        previous_generator = generator
        generator *= generator_growth


    return history



# ============================================
# Analysis
# ============================================

resource_history = run_resource_system()
generator_history = run_generator_system()


print("=" * 60)
print("LONG HORIZON PHASE BOUNDARY TEST")
print("=" * 60)



print("\nEarly Comparison")
print("-" * 60)

for t in [0,5,10,20]:

    r = resource_history[t]
    g = generator_history[t]

    print(
        f"t={t:3d} | "
        f"Resource C={r['capability']:12.3f} | "
        f"Generator C={g['capability']:12.3f}"
    )



# Find crossover point

cross = None

for r,g in zip(resource_history,generator_history):

    if g["capability"] > r["capability"]:

        cross = g["t"]
        break



print("\n" + "=" * 60)
print("FINAL RESULTS")
print("=" * 60)


print()

print(
    "Resource Scaling Final Capability:",
    round(resource_history[-1]["capability"],3)
)

print(
    "Generator System Final Capability:",
    round(generator_history[-1]["capability"],3)
)


print()

print(
    "Generator Change ΔGm:",
    round(
        generator_history[-1]["generator"]
        -
        generator_history[0]["generator"],
        3
    )
)


print(
    "Final Ω Proxy:",
    round(generator_history[-1]["omega"],3)
)


print()

if cross:

    print(
        "Capability crossover detected at:",
        f"t={cross}"
    )

else:

    print(
        "No crossover detected"
    )



print("\n" + "=" * 60)
print("PHASE BOUNDARY INTERPRETATION")
print("=" * 60)


if cross:

    print("""
Evidence consistent with:

        ΔGm → ΔΩ → ΔC


The generator system initially may not dominate,
but eventually surpasses resource scaling because
the improvement mechanism compounds.
""")

else:

    print("""
No phase boundary detected.

Possible explanations:

- generator growth too weak
- horizon too short
- resource advantage too strong
- model assumptions incorrect
""")
