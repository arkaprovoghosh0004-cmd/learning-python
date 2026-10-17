tasks = []



while True:
  
  print("\n1. Add")
  print("2. Show")
  print("3. Remove")
  print("4. Quit")

  command = int(input("Choose your command: "))
  if command == 1:
    task = input("Enter task: ")
    tasks.append(task)
  
  elif command == 2:
    if not tasks: 
      print("The list is empty.")
    for index, item in enumerate(tasks):
      print(f"{index + 1}: {item}")
  
  elif command == 3:
    if not tasks: 
      print("Nothing to remove.")
    else:
      number = int(input("Which number to remove? "))
      del tasks[number - 1]
  
  elif command == 4:
    break

  else:
    print("Invalid input.")




