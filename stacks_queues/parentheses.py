from stack import Stack



def isBalanced(str):
    open_paran = ["(", "{", "["]
    close_paran = [")", "}", "]"]
    stk = Stack()
    for i in str:
        if i in open_paran:
            stk.push(i)



        elif i in close_paran:
            if stk.size>0:
                last_open = stk.pop()
                if close_paran.index(i) != open_paran.index(last_open):
                    return False
    if stk.size == 0:
        return True
    else:
        return False


if __name__=="__main__":

    str = "{[] {()}}"
    print(isBalanced(str))

    str = "((()"
    print(isBalanced(str))