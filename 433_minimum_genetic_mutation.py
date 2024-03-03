# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.


# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2


# Constraints:

# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)

        def get_next_mutation(input_gene_str):
            ans = []
            for i in range(len(input_gene_str)):
                part1 = input_gene_str[:i]
                target = input_gene_str[i]
                part2 = input_gene_str[i + 1 :]

                for char in "ACGT":
                    if char != target:
                        new_tar = char
                        new_gene = part1 + new_tar + part2
                        if new_gene in bank_set:
                            ans.append(new_gene)

            return ans

        q = deque()
        # in q: gene, steps to get there from start
        q.append((startGene, 0))

        seen = set()
        seen.add(startGene)

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            for neighbor in get_next_mutation(gene):
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append((neighbor, steps + 1))

        return -1
