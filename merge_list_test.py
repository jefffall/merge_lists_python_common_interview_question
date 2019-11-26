#Merge list test.
# note how they make it painful by requiring " and lists print out '


input1 = [1,2,3,4]
input2 = ["a","b","c","d","e"]



def merge_lists(input1, input2):
    merged_list = []
    output_string = "["
    index = 0
    for letter in input2:
        merged_list.append(input1[index])
        merged_list.append(letter)
        if (index == len(input1)-1):
            if (index+1 <= len(input2)):
                merged_list.append(input2[index+1])
                break
            else:
                break
        else:
            index=index + 1
            
 
    index = 0  
  
    
    for item in merged_list:
        if (index % 2) == 0: 
            #even
            output_string = output_string + str(item) + ","
        else:
            output_string = output_string + "\"" + item + "\"" + ","
        index = index + 1
  
        if (index == len(merged_list)-1):
            break
        
    last = merged_list[index]
    output_string = output_string + "\"" + last + "\"" 
           
    output_string = output_string + "]"
     
    return output_string

#######################################################################################
   
print (merge_lists(input1, input2))








