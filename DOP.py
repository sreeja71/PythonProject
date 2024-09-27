
from datetime import datetime

class Onboarding:
    def __init__(self, dev_id, roles, modules):
        self.dev_id = dev_id
        self.roles = roles
        self.modules = modules
        self.progress = {module: "not completed" for module in modules}
        self.time_stamp = str(datetime.now())

    def create_progress(self):
        return self.progress

    def update_progress(self, progress_updates):
        self.progress.update(progress_updates)
        self.time_stamp = str(datetime.now())

    def assign_roles(self, roles):
        self.roles = roles

    def assign_modules(self, modules):
        self.modules = modules
        self.progress = {module: "not completed" for module in modules}

    def recommend_next_module(self):
        if all(status == "completed" for status in self.progress.values()):
            return "You have completed all of the onboarding modules."

        for module, status in self.progress.items():
            if status == "not completed":
                return module

    def generate_onboarding_report(self):
        results = [f"{module}: {status}" for module, status in self.progress.items()]
        report_str = (f"Onboarding progress report for {self.dev_id}\n"
                      f"Time updated: {self.time_stamp}\n\n" +
                      "\n".join(results))
        return report_str

if __name__ == "__main__":
    dev_id = input("Enter developer ID: ")
    print("Choose roles: python, java, c/c++")
    roles = input("Enter role: ").strip().lower()
    
    if roles in ["python", "java", "c/c++"]:
        modules = [f"module {i+1}" for i in range(4)]
        print(f"Available modules: {', '.join(modules)}")
    else:
        print("Invalid role")
        exit()

    selected_module = input("Enter the module you want to start with (e.g., 'module 1'): ").strip()
    if selected_module not in modules:
        print("Invalid module")
        exit()
    
    print(f"Welcome to {selected_module}")
    print("Recommended modules:", [mod for mod in modules if mod != selected_module])

    # Creating an Onboarding instance with user input
    onboard = Onboarding(dev_id, roles, modules)

    # Show the next recommended module
    print("Next module to complete:", onboard.recommend_next_module())

    # Generate the initial report
    print("\nInitial Onboarding Report:")
    print(onboard.generate_onboarding_report())

    # Simulate updating progress based on user input
    progress_input = input("\nEnter progress updates (format: module_name:status, comma-separated): ")
    progress_updates = dict(item.split(":") for item in progress_input.split(","))
    
    onboard.update_progress(progress_updates)

    # Show the updated next module recommendation
    print("\nUpdated Next Module Recommendation:")
    print(onboard.recommend_next_module())

    # Show the final report
    print("\nUpdated Onboarding Report:")
    print(onboard.generate_onboarding_report())
