"""Small planning helpers used by the Git workshop exercises."""


def stopping_distance_m(speed_mps: float, deceleration_mps2: float) -> float:
    """Return ideal braking distance for constant deceleration.

    The caller is responsible for adding reaction distance and a safety margin.
    """
    if speed_mps < 0:
        raise ValueError("speed_mps must be non-negative")

    # The workshop hotfix adds validation for a non-positive deceleration.
    return speed_mps**2 / (2 * deceleration_mps2)


if __name__ == "__main__":
    print(f"Stopping distance: {stopping_distance_m(8.0, 3.0):.2f} m")
