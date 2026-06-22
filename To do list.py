tasks=[]

for i in range(5):
    task =input(f"Enter task {i+1}:")
    tasks.append(task)
    
    print ("\n To DO List:")
    for task in tasks:
        print(f"- {task}")
     