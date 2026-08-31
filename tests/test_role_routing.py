from showcase.agents.role_example import AgentRole, AgentTask, route_task


def test_routes_build_task_to_coder():
    task = AgentTask(
        task_id="task-1",
        description="Build the API endpoint",
    )

    assert route_task(task) is AgentRole.CODER


def test_routes_test_task_to_tester():
    task = AgentTask(
        task_id="task-2",
        description="Add pytest coverage",
    )

    assert route_task(task) is AgentRole.TESTER
