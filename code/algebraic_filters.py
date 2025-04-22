import numpy as np

def apply_algebraic_filter(omega, order=1, decay_rate=0.4):
    """
    Applies a symbolic algebraizing filter P_k of a given order.

    Parameters:
    - omega : np.ndarray
        The current cohomology class vector.
    - order : int
        The order of the filter (number of iterations).
    - decay_rate : float
        Decay factor applied to non-algebraic coefficients (ϕ component).

    Returns:
    - omega_filtered : np.ndarray
        The filtered class with reduced transcendental component.
    """
    omega_filtered = np.copy(omega)

    # Simulate reduction of high-frequency / non-algebraic part
    for k in range(order):
        omega_filtered = decay_rate * omega_filtered + (1 - decay_rate) * omega_filtered.mean()

    return omega_filtered
