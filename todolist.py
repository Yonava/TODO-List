class Todo:
    def __init__(self, ranking, title, due):
        self.ranking = ranking
        self.title = title
        self.due = due
    def display(self):
        print(f"Priority: {self.ranking},\n{self.title}, \nGet This Done By: {self.due}")

def todoRank(sortThis):
    sortThis.sort(key=lambda x: x.ranking)
    return sortThis

def todoDel(masterList):
    remover = input("Thing you want to get rid of: ")
    for e in masterList:
        if e.title.lower() == remover.lower():
            masterList.remove(e)

def display(masterList):
    masterList = todoRank(masterList)
    for e in masterList:
        e.display()
        

def todoInput(todo):
    todo.append(Todo(

    int(input("Rank (1-5): ")),
    input("Title: "),
    input("Due Date: ")
    
    ))
        
    

def main():
    masterList = []
    while True:
        runningInput = input("TODO List - New Item/Del Item/Display: ")
        if runningInput == "new": todoInput(masterList)
        elif runningInput == "del": todoDel(masterList)
        elif runningInput == "display": display(masterList)
        elif runningInput == "exit": return
        else: print("No!")
    

main()




