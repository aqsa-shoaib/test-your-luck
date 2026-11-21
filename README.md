# Test Your Luck

A Python probability simulation based on coin flips, dice rolls, and a three-outcome spinner.

**Author:** Aqsa Shoaib  
**Original classroom project:** January 12, 2025

## How it works

1. A coin is flipped. On **Heads**, one six-sided die is rolled. On **Tails**, two dice are rolled and the higher result is kept.
2. A spinner chooses one of three equally likely outcomes:
   - **LOCKED:** Keep the current result.
   - **ROLL:** Roll the die again and replace the result.
   - **NOTHING:** Set the result to 1.
3. A final number of **4, 5, or 6** is a win; **1, 2, or 3** is a loss.
4. The program repeats for the requested number of rounds and shows the observed win rate.

## Run

Requires Python 3. No external packages are needed.

```bash
python test_your_luck.py
```

## Skills demonstrated

- Functions, conditional logic, and loops
- Pseudorandom simulation
- Counting outcomes and calculating percentages
- Input validation

## Project history

This version preserves the rules of Aqsa's original classroom probability game while organizing the code and handling invalid round counts. The displayed percentage is the **observed win rate** from a simulation, not the exact theoretical probability.
