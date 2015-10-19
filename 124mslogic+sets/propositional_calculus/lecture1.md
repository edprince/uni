#Notes#
Conjunction - P ^ Q is true uf and only if P and Q are both true  
Disjunction: P v Q is true if and only if at least one of P or Q is true  
Logical implication: P => Q is true unless P is true and Q is false  
Bi-implication: P <=> Q is true if and only if P and Q have the same truth value  

Atomic sentences uses **no** connectives
Compound sentences are composed with other proposition combined by connectives

Example
-------
A: The operator presses the **a**larm
T: The core **t**emperature is rising rapidly
C: The control process **c**loses down the reactor

1. (A^~R)=>~C
  > Convert into a formula
2. (t^~f)=>~t
  > Substitute true and false values in
3. (t^t)=>f
  > Solved down
4. t=>f
  > Find an answer
5. f
