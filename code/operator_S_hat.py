import numpy as np
from primitive_projectors import project_primitive
from algebraic_filters import apply_algebraic_filter
from lefschetz_tools import lefschetz_inverse

def S_hat(omega_k, polarization_matrix=None, filter_order=1):
    """
    Applies the symbolic operator Ŝ to a cohomology class ω_k.

    Ŝ := Λ ∘ Π_prim ∘ P_k

    Parameters:
    - omega_k : np.ndarray
        The current cohomology class vector (numeric or symbolic).
    - polarization_matrix : np.ndarray or None
        The polarization (Kähler) matrix used for Lefschetz and primitivity.
    - filter_order : int
        Order of the symbolic algebraizing filter P_k to apply.

    Returns:
    - omega_k_plus_1 : np.ndarray
        The new cohomology class after applying one iteration of Ŝ.
    """

    # Step 1: Project onto primitive cohomology
    omega_prim = project_primitive(omega_k, polarization_matrix)

    # Step 2: Apply symbolic algebraizing filter
    omega_filtered = apply_algebraic_filter(omega_prim, order=filter_order)

    # Step 3: Apply Lefschetz inverse operator
    omega_k_plus_1 = lefschetz_inverse(omega_filtered, polarization_matrix)

    return omega_k_plus_1
