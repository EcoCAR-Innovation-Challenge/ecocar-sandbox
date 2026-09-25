# Autonomous Vehicle Git Workshop Sandbox

This repository is intentionally small and intentionally contentious. It models a few artifacts an autonomous-vehicle team might maintain while students practice collaborative Git workflows.

## Files

- `vehicle_config.yaml`: vehicle operating parameters
- `src/planner.py`: simple stopping-distance calculation
- `config/lidar_calibration.csv`: text calibration table
- `config/lidar_calibration.xlsx`: equivalent binary spreadsheet
- `CONTRIBUTORS.md`: workshop participant list

## Ground rules

1. Do not push directly to `main`.
2. Use `exercise/<github-username>/<task>` branch names.
3. Make focused commits.
4. Open a Pull Request for integration.
5. Do not modify or push to `workshop/*` prepared branches.
6. Run `git status` whenever you are uncertain.

The facilitator provides the exercise sequence.

## Future exercise idea

Add a visualization of stopping distance at several speeds.
