"""
Failed Phase Boundary Experiment

Tests whether generator improvement alone is sufficient.

Hypothesis:

A true phase boundary requires:

    ΔGm → ΔΩ → ΔC

Generator improvement is necessary,
but not sufficient.

Three systems:

1. Successful Transition

    Generator improves
          ↓
    Adoption succeeds
          ↓
    Frontier expands
          ↓
    Capability accelerates


2. Failed Transition

    Generator improves
          ↓
    Adoption fails
          ↓
    Frontier unchanged
          ↓
    No acceleration


3. Resource Scaling

    Resources increase
          ↓
    Capability improves
          ↓
    Generator unchanged


Measures:

Gm:
    generator potential

A:
    adoption

P:
    reachable frontier

C:
    capability

Omega:
    acceleration proxy

"""


TIMESTEPS = 100



# ==========================================
# Parameters
# ==========================================

initial_C = 1.0
initial_P = 10.0

initial_G = 1.0
initial_A = 1.0


alpha = 0.15


# generator growth

gamma = 0.15
G_capacity = 20.0


# adoption

rho_success = 0.08
rho_failure = 0.005


# frontier

beta = 0.04
P_capacity = 10000.0



# ==========================================
# Generic simulation
# ==========================================

def run_system(mode):

    C = initial_C
    P = initial_P

    G = initial_G
    A = initial_A


    history = []

    previous_lambda = 0


    for t in range(TIMESTEPS):

        old_C = C


        # capability follows frontier

        C += alpha*(P-C)



        # generator improves

        G += gamma*G*(1-G/G_capacity)



        # adoption

        if mode == "success":

            A += rho_success*(G-A)


        elif mode == "failure":

            A += rho_failure*(G-A)


        elif mode == "resource":

            A = 1



        # frontier response

        if mode != "resource":

            P += (
                beta
                * A
                * P
                * (1-P/P_capacity)
            )

        else:

            # external resource growth

            P += 0.08 * (1-P/P_capacity)



        Lambda = C-old_C

        Omega = Lambda-previous_lambda


        history.append({

            "t":t,
            "C":C,
            "P":P,
            "G":G,
            "A":A,
            "Lambda":Lambda,
            "Omega":Omega

        })


        previous_lambda = Lambda



    return history



# ==========================================
# Run
# ==========================================

successful = run_system("success")
failed = run_system("failure")
resource = run_system("resource")



# ==========================================
# Output
# ==========================================

print("="*80)
print("FAILED PHASE BOUNDARY TEST")
print("="*80)


print("""
t | Success C | Failed C | Resource C | Success Ω | Failed Ω
-------------------------------------------------------------
""")


for t in [0,10,20,30,50,75,99]:

    s = successful[t]
    f = failed[t]
    r = resource[t]


    print(
        f"{t:2d} | "
        f"{s['C']:10.3f} | "
        f"{f['C']:10.3f} | "
        f"{r['C']:10.3f} | "
        f"{s['Omega']:9.4f} | "
        f"{f['Omega']:9.4f}"
    )



# ==========================================
# Results
# ==========================================

print("\n")
print("="*80)
print("FINAL RESULTS")
print("="*80)


print()

print(
"Successful Transition Capability:",
round(successful[-1]["C"],3)
)

print(
"Failed Transition Capability:",
round(failed[-1]["C"],3)
)

print(
"Resource Capability:",
round(resource[-1]["C"],3)
)


print()

print(
"Successful Generator:",
round(successful[-1]["G"],3)
)

print(
"Failed Generator:",
round(failed[-1]["G"],3)
)


print()

print(
"Successful Adoption:",
round(successful[-1]["A"],3)
)

print(
"Failed Adoption:",
round(failed[-1]["A"],3)
)



print("\n")
print("="*80)
print("FRAMEWORK TEST")
print("="*80)


print(
"""
Prediction:

Generator improvement alone:

    ΔGm > 0

should NOT guarantee:

    ΔΩ > 0

or:

    ΔC > 0


A real phase boundary requires:

    Generator
        ↓
    Adoption / alignment
        ↓
    Reachable frontier expansion
        ↓
    Capability acceleration


Expected:

SUCCESS:
    ΔGm > 0
    Ω > 0
    C acceleration


FAILURE:
    ΔGm > 0
    Ω ≈ 0
    no phase transition


RESOURCE:
    ΔR > 0
    ΔGm ≈ 0
"""
)
