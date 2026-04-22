# Handoff Document — Rubik's Cube Old Pochmann Solver (Python)

## Project Overview
The student is a **2nd year Computer Science student** building a Python project that:
- Takes a **3x3 Rubik's cube state** as input
- Returns a **string of move letters** that solves the cube using the **Old Pochmann (OP) method**

Estimated time to complete: **25–43 hours** (~2–5 weeks at a casual pace)

---

## Old Pochmann Method — Summary
Old Pochmann is a blindsolve method that solves the cube in two phases:
1. **Edges** — solved first
2. **Corners** — solved second

Each phase works by cycling pieces through a **buffer position** using set algorithms (e.g. T-perm, Y-perm).

---

## Phase 1: Edge Memorisation Logic (Student's Understanding)
The student has a solid understanding of this. Here is their description:

- The **buffer piece is at UL**
- Look at the buffer edge piece (UL). If it is not in its correct slot, find where it **should** go
- Memorise the **letter associated with that destination slot**
- Then look at the piece **currently sitting in that destination slot** and repeat the process
- Continue until all edge pieces have been visited
- If at any point the current piece **is the buffer piece**, start a **new cycle** by picking any unsolved edge piece
- This is because the buffer must remain free to perform swaps — it is only resolved at the very end

---

## Cube State Representation (Agreed Approach)

### Data Structure
A **dictionary of lists**, where each key is a face and each value is a list of 9 stickers:

```python
cube = {
    "U": [0,1,2,3,4,5,6,7,8],
    "D": [0,1,2,3,4,5,6,7,8],
    "F": [0,1,2,3,4,5,6,7,8],
    "B": [0,1,2,3,4,5,6,7,8],
    "L": [0,1,2,3,4,5,6,7,8],
    "R": [0,1,2,3,4,5,6,7,8],
}
```

### Index Layout
Each face uses this index layout:
```
0 1 2
3 4 5
6 7 8
```

---

## Applying Moves — Key Insight
When a face rotates, two things must happen:
1. The **rotating face's array** must be rotated (e.g. index 0→2, 1→5, 2→8 for clockwise)
2. The **adjacent faces' affected indices** must be cycled

The affected indices depend entirely on **which face is rotating and which edge is touching it.**

### Worked Examples

**U move (clockwise):**
```
L[0,1,2] → F[0,1,2] → R[0,1,2] → B[0,1,2] → L[0,1,2]
```

**F move (clockwise) — student derived this themselves:**
```
U[6,7,8] → R[0,3,6] → D[0,1,2] → L[2,5,8] → U[6,7,8]
```

---

## Current Stopping Point
The student is about to implement the **`cycle()` function**, which is the core building block for applying any move.

### Function Signature Being Worked On
```python
def cycle(face1, indices1, face2, indices2, face3, indices3, face4, indices4):
    ...
```

### What It Needs To Do
- Take 4 faces and their respective affected indices
- Cycle the values at those indices in order: face1 → face2 → face3 → face4 → face1
- Use a **temporary variable** to avoid overwriting values before they are saved

### The Hint Given
Think about the **temporary variable problem** — if you want to shift 4 groups of values in a circle, you need to save one group first before you start overwriting.

---

## Pedagogy Notes (for the AI continuing this conversation)
- The student is being taught **Socratically** — through leading questions rather than giving answers directly
- They have shown strong intuition and should be encouraged to reason things out before being corrected
- When they get something right, confirm it clearly and move forward
- When they are close but not quite right, ask a follow-up question rather than correcting directly
- **Do not write large blocks of code for them** — guide them to write it themselves
- The next step is for the student to attempt writing the body of the `cycle()` function themselves

---

## Suggested Next Question to Ask the Student
> "Have a go at writing the body of the cycle function. Remember — think about the temporary variable problem. If you start moving values around, what do you need to save first to avoid losing data?"
