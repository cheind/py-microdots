# neural-anoto-dot

Neural decoding of anoto micro dot pattern

## Definitions

-   B(k,n) De Bruijn sequence of order n over alphabet k with length $k^n$.
-   CB(k,n,m) Cut-down (quasi) De Bruijn sequence of ordern n over alphabet of size k with length m (m < $k^n$)

## Encoding

Given:

-   MNS: CB(2,6,63)
-   A range valid delta values [dlow, dhigh] having R values with dlow >= 0 and dhigh < 63. In Anoto [5,58]
-   Prime factors p1,...,pn for R
-   A set of secondary number sequences SNS, one for each prime factor

Given position p to encode and the previos roll value for the MNS

1. Compute remainders r1,...,rn of (p-1) wrt to SNS
2. Lookup the symbol ci at SNS_i[ri] them to get c1,...,cn
3. Use the number basis to reconstruct d from c1,....,cn
4. Apply any affine transformation to d to get final delta value
5. Compute the current roll value as (prev_roll + delta) mod |MNS|

Remarks

-   SNS need to be relatively prime in length, so we need to create CB sequences

```

# Number of combinations of delta values
In [2]: 54**5
Out[2]: 459165024

# If we represent 54 via prime factors [2,3,3,3]
In [6]: (2**5)*(3**5)**3
Out[6]: 459165024

# However, we need lists to be relatively prime for CRT to work,
# So we reduce the SNS lengths to
In [1]: 31*236*233*241
Out[1]: 410815348
```

What's the impact of the reduced list lengths? I beleive that some delta values in [0,54) + 5 will simply never appear.

So given a position, we compute the remainders in these lists. These remainders correspond to indices into that lists. The values at those indices in the corresponding lists will be the coefficients of the delta values. Delta values will be used in encoding to determine the roll of the MNS. The roll for position i, can be computed by roll(i-1)+delta(i-1,i) % |MNS|.

Why need SNS be CB(k,5,...)? It means that _no_ set of 5 consecutive delta values (from 6 positions) will repeat, I think. That makes sense, since each set of 5 delta values should be decodable into a unique positions.

Probably we should not worry about which elements from SNS have been removed, it simply means they will not be used in encoding and hence are also not required in decoding.

## Example

Consider MNS B(2,4), |MNS| = 16 unique positions and hence there are 15 delta (mod 16) values. For symmetry assume that we observer 4x4 patterns. Then we want each set of 4-1=3 delta values to be non-repeating. So 15 has prime factors 3\*5 and we can
have SNS1 = B(3 (alphabet from prime-factor),3 (order - 3 delta)), |SNS1| = 27 and SNS2 = B(5,3), |SNS2| = 125. Since gcd(27,125)=1, SNS1 and 2 are already prime and we will not need any quasi debruijn sequence.

How many elements can we encode? 15\*\*3=3375
