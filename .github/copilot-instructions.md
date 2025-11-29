<!-- .github/copilot-instructions.md - Project-specific guidance for AI coding agents -->
# Retirement Investment — Copilot Instructions

Purpose: Help AI coding agents be productive quickly when editing or extending this small Python CLI project.

- **Project layout**: core code lives in `src/`.
  - `src/Main.py`: CLI entrypoint that reads user input and calls calculators.
  - `src/MaxWithdrawal.py`: Core algorithm — `MaxWithdrawal` class (binary search + simulation).
  - `src/FixedInvestor.py`: `FixedInvestor.fixed_investor(principal, years, rate)` — simple compound interest.
  - `src/VariableInvestor.py`: `variableInvestor(principal, rateList)` — multiplies successive annual rates.
  - `src/expense.py`: auxiliary utilities (inspect before modifying).

- **Big-picture architecture & data flow**:
  - This is a small, script-style CLI app. `Main.py` collects numeric inputs -> calls one of the calculators -> prints results.
  - Numerical logic and validation live in `src/MaxWithdrawal.py` and the investor modules. Keep numerical semantics and validation intact when refactoring.

- **Key public APIs to preserve** (examples from codebase):
  - `MaxWithdrawal(num_years, balance, rate, tolerance=0.1).maximum_withdrawal()` — returns a float.
  - `FixedInvestor.fixed_investor(principal, years, rate)` — returns final balance.
  - `variableInvestor(principal, rateList)` — returns final balance after applying each rate.

- **Project-specific conventions & gotchas**:
  - Naming is inconsistent between modules and `Main.py` (camelCase vs snake_case). Example: `VariableInvestor.py` defines `variableInvestor`, but `Main.py` sometimes refers to `variable_investor` or `variableInvestor` — be conservative when renaming and run the CLI after changes.
  - `MaxWithdrawal.__init__` expects `num_years` as an `int`; other inputs accept floats. Preserve input validation (ValueError/TypeError) rather than removing it.
  - `MaxWithdrawal` computes an initial `high` bound using an annuity formula and then runs a binary search using `__simulate_retirement`. Changes to these routines must include numerical sanity checks for edge cases (zero rate, extreme rates, tiny denominators).

- **How to run locally (Windows/cmd)**:
  - From repository root run the CLI:
    `python src\\Main.py`
  - Quick REPL checks (run inside `src` folder for simple imports):
    `cd src` then `python` then `from FixedInvestor import FixedInvestor; FixedInvestor.fixed_investor(1000,10,0.05)`

- **Testing / validation approach**:
  - There are no automated tests. Use small deterministic checks when modifying algorithms: known inputs with closed-form answers (e.g., compound interest), and simple simulations with small `num_years` to manually verify behavior.
  - For `MaxWithdrawal`, verify edge cases: `rate=0`, very small `tolerance`, very small `num_years`, and negative rates above -1.

- **When editing**:
  - Avoid broad renames across modules in a single PR; fix one naming inconsistency at a time and run the CLI after each change.
  - Preserve public function signatures and input validation unless you update all call sites and add tests/manual checks.
  - If adding dependencies, update repository README and provide installation instructions; however, current code has no external dependencies.

- **Files to read first when investigating behavior**:
  - `src/MaxWithdrawal.py` (algorithm details)
  - `src/Main.py` (user flows and current naming inconsistencies)
  - `src/VariableInvestor.py` and `src/FixedInvestor.py` (math helpers)

If anything here is unclear or you'd like the instructions to be stricter (for example, enforcing snake_case across the repo), tell me which policy to apply and I will update this file.
