import matplotlib.pyplot as plt
import numpy as np

def plot_phi_decay(phi_norms, title="Decay of ||ϕₖ|| under symbolic iteration"):
    """
    Plots the exponential decay of the norm of the transcendental component ϕₖ.

    Parameters:
    - phi_norms : list or np.ndarray
        Norm values of ϕₖ at each iteration step.
    - title : str
        Title of the plot.
    """
    iterations = np.arange(len(phi_norms))

    plt.figure(figsize=(8, 5))
    plt.plot(iterations, phi_norms, marker='o', color='crimson', linewidth=2)
    plt.yscale("log")
    plt.xlabel("Iteration k")
    plt.ylabel(r"$\|\phi_k\|$")
    plt.title(title)
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_projection_trajectory(points, title="Symbolic Algebraization Trajectory", labels=None):
    """
    Plots the trajectory of ωₖ in reduced symbolic coordinate space (e.g., Lefschetz coefficients).

    Parameters:
    - points : np.ndarray of shape (k, 2) or (k, 3)
        List of coordinate tuples at each iteration step.
    - title : str
        Title of the plot.
    - labels : list of str or None
        Optional list of labels for each point (e.g., ["ω₀", "ω₁", ..., "ωₖ"])
    """
    points = np.array(points)
    dim = points.shape[1]

    fig = plt.figure(figsize=(7, 6))
    if dim == 2:
        plt.plot(points[:,0], points[:,1], marker='o', linestyle='-', color='navy')
        if labels:
            for i, label in enumerate(labels):
                plt.text(points[i,0], points[i,1], label, fontsize=10)
        plt.xlabel("⟨Λ^k ω, D₁⟩")
        plt.ylabel("⟨Λ^k ω, D₂⟩")
        plt.title(title)
        plt.grid(True, alpha=0.3)
    elif dim == 3:
        from mpl_toolkits.mplot3d import Axes3D
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(points[:,0], points[:,1], points[:,2], marker='o', color='teal')
        if labels:
            for i, label in enumerate(labels):
                ax.text(points[i,0], points[i,1], points[i,2], label, fontsize=10)
        ax.set_xlabel("⟨Λ^k ω, D₁⟩")
        ax.set_ylabel("⟨Λ^k ω, D₂⟩")
        ax.set_zlabel(r"$\|\phi_k\|$")
        ax.set_title(title)
    else:
        raise ValueError("Points must have dimension 2 or 3.")

    plt.tight_layout()
    plt.show()
