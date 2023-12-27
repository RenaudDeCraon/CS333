import sys
def box_fits_inside(outer,inner):
    return all(outer_dim > inner_dim for outer_dim, inner_dim in zip(outer, inner))
    
    
def findNestedBox(boxDimensions):
    max_nested_count =0
    max_nested_indices = []
    n = len(boxDimensions)
    dp = [1] * n
    for i in range(0, n):
        for j in range(i):
            if box_fits_inside(boxDimensions[i], boxDimensions[j]) and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

        if dp[i] > max_nested_count:
            max_nested_count = dp[i]
            max_nested_indices.append(i)
        elif dp[i] == max_nested_count:
            max_nested_indices.append(i)

    return max_nested_count, max_nested_indices


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        content = file.readlines()
        boxNum = int(content[0].strip())
boxDim = {}
for i in range(boxNum):
    boxDim[i] = [float(x) for x in content[i+1].strip().split(" ")]

def volume(box):
    return boxDim[box][0] * boxDim[box][1] * boxDim[box][2]
sorted_boxDim = sorted(boxDim, key=volume, reverse=False)

finalDict={}
for i, box_index in enumerate(sorted_boxDim):
    finalDict[i]=boxDim[box_index]

max_nested_count, max_nested_indices = findNestedBox(list(finalDict.values()))
print("(MAX NUM OF NESTED BOXES:", max_nested_count)
print("BOXES:")
for i in max_nested_indices:
        print(finalDict[i])
        
print("TIME COMPLEXITY : O(n^2)")