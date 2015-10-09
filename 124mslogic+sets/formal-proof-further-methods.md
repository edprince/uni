1) V - (modus ponens)   
2) V - Simplification  
3) I  
4) V - (modus ponens)  
5) I  
6) V - Simplification   

If you cannot directly use a rule of inference, always prove by drawing up an assertion/justification table,
label the hypotheses and prove how it works.

Show that the following argument is valid:

h1: x => y  
h2: w => z  
h3: ~z ^ ~y  
- - - - -
~x ^ ~w  

| Assertion | Justification |
| --------- | ------------- |
| 1. ~z ^ ~y | h3 |
| 2. ~z | 1, simplification |
| 3. w => z | h2 |
| 4. ~w | 2, 3, modus tollens |
| 5. ~y | 1, simplification |
| 6. x => y | h1 |
| 7. ~x | 5, 6, modus tollens |
| 8. ~x ^ ~y | 5, 7, conjunction |


> R: I read a lot  
W: I am well-educated  
B: I am boring  
F: I have friends  
U: I am rude

h1: R => W v B
h2: B v U => ~F
h3: R ^ F
- - - - 
W

| Assertion | Justification |
| --- | --- |
| 1. R ^ F | h3 |
| 2. R | 1, simplification |
| 3. R => W v B | h1 |
| 4. W v B | 2, 3, modus ponens |
| 5. F | 1, simplification |
| 6. B v U => ~F | h2 |
| 7. ~(B v U) | 5, 6, modus tollens |
FINISH
