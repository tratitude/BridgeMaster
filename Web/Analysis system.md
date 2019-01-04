## PBN format (Portable Bridge Notation format)
- [stadard](https://www.tistis.nl/pbn/)
- [bridgetoernooi dataset](http://bridgetoernooi.com/index.php/home)
- [create PBN tools](http://www.himbuv.com/nieuw/english/diagram_en1)
## auction best case
- Goal: 內建某個bidding system, 輸入一副牌， 輸出雙方最好的bidding
- [What is the best bidding system in Bridge? Why?](https://www.quora.com/What-is-the-best-bidding-system-in-Bridge-Why)
- [Simple bridge bidding](http://www.cs.cmu.edu/~hde/bidding.htm)
- [A guide to Standard American bidding methods in contract bridge](https://sites.math.washington.edu/~jfrichey/misc_pdfs/Natural_Bridge_Bidding.pdf)
- [Understanding bidding systems](https://southcoastsun.co.za/130643/understanding-bidding-systems/)
## playing best case
- [bridgecaptain](http://www.bridgecaptain.com/downloadDD.html)
- [Learning a Double Dummy Bridge Solver](http://cs229.stanford.edu/proj2016/report/Mernagh-LearningADoubleDummyBridgeSolver-report.pdf)
- [dds-bridge c++](https://github.com/dds-bridge/dds)

---

## Design and Implementation of an Automated Bridge Playing Agent
### 4 SOLVING THE DOUBLE-DUMMY PROBLEM
- **Definition 2. The double-dummy problem:**
> The problem of finding the optimal moves of a player and/or the corresponding
> minimax score in the game of double-dummy bridge. The game may be in the initial
> state (no cards have yet been played) or a later state. In the case of a later state, the
> score might be, either the total tricks expected to be won, or the remaining tricks
> expected to be won.
- The double-dummy problem is computationally demanding, and cannot be solved in
a tractable time without some major optimizations. The optimizations we used include:
  - α-β pruning
  - transposition table
  - iterative deepening zero window search
  - partition search
  - move ordering
  - forward pruning through the use of admissible heuristics
### 4.2 The basic solver
- implemented a simple minimax solver
- α-β pruning optimization does not affect the outcome
of the minimax algorithm, only its efficiency
### 4.3 Implementing and optimizing the transposition table
- store the upper and the lower bound of the score achievable at the remaining
tricks, not the total tricks
#### 4.3.1 The naive implementation
- **Definition 3. Two positions are equal when:**
> 1. Each hand has the same card in both positions. In the corresponding double-
> dummy problem this is true if and only if the same card have been played.
> 2. If we are examining two positions at the beginning of the trick, the leading
> hand of the trick should be the same.
> 3. If we are not examining two positions at the beginning of the trick, the suit
> lead and the winning card should be the same.
- It should be noted, that if the first condition holds true, both positions have the
same number of cards played at this trick.
- implement a hash table that has equal keys for equal positions
> If we stored the total score at the transposition table, we would have an extra
> condition for equal positions. 
> The positions should have the same score so far in order to
> be equal. 
> That would make hits at the hash table more uncommon, negatively affecting
> the performance.
#### 4.3.2 Implementation of the partition search
- it is not necessary for two positions of the same scores to be equal
- The term ”equivalent position” is useful in this case
- **Definition 4. Two positions are equivalent when they have equal minimax score for
the remaining tricks.**
