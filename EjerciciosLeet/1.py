class Solution:
    list=[]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I me sirve para el indice, que me lo da range(lem(nums))
        for i in range(len(nums)):
            #i+1 me serviria para que no compare el mismo numero dos veces
            for j in range(i + 1, len(nums)):
                #Aca lo que hago es encontrar el numero necesario para igualar el target
                if nums[j] == target - nums[i]:
                    return [i, j]
    #Si no hay target que coincida me devolveria esto
        return []

