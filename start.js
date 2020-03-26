function remove_duplicates(nums){
	hash_table = {}
	for(i=0; i < nums.length; i++){
		for(let key in hash_table){
			if(hash_table[key] == nums[i]){
				hash_table[key] += 1
			}
		}
		
	}
}

remove_duplicates([1,2,3,4])