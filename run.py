from executor.executor import Executor

# Add list to executor parameters
optional_parameters = ["push up", "deadlift", "swings", "row", "squat", "wear"]
optional = None
executor = Executor("vest", optional)
# executor.execute_all()
executor.execute_converter()
