
def Optimise_Cloud_Cost():
    total_cost = 0
    wasted_cost = 0
    idle_instance = []
    with open ("instances.txt","r") as file:
        for line in file:
                parts = line.strip().split(":")
                instance_id = parts[0]
                state = parts[1]
                cost = float(parts[2]) 
                usage = parts[3]
                if state == "running":
                    total_cost = total_cost + cost
        
                if state == "running" and usage == "idle":
                    wasted_cost = wasted_cost + cost
                    idle_instance.append(instance_id)

    return total_cost, wasted_cost, idle_instance

total, waste, idle_servers = Optimise_Cloud_Cost()
print(f"[REPORT] Total Active Cloud Cost: ${total:.2f}")
print(f"[REPORT] Wasted Cost (Idle Servers): ${waste:.2f}")
print(f"[REPORT] Idle Instance IDs to Terminate: {idle_servers}")
    
