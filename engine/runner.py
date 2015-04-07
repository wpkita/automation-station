from engine.config import *
import subprocess


class Runner:
    def __init__(self):
        self.local_config = LocalConfig()
        self.cloud_config = CloudConfig(self.local_config.get_task_directory())

    def get_tasks(self, ):
        return [task for task in self.cloud_config.get_value('tasks')]

    def get_task(self, task_name):
        task = next((task for task in self.cloud_config.get_value('tasks') if task['name'] == task_name), None)

        return task

    def add_task(self, task_name):
        tasks = self.cloud_config.get_value('tasks')

        # Make sure the task doesn't already exist
        task = self.get_task(task_name)
        if task is None:
            new_task = {
                'name': task_name,
                'path': task_name
            }

            # Update config with new task
            tasks.append(new_task)
            self.cloud_config.set_value('tasks', tasks)

            return new_task, True

        return task, False

    def run_task(self, task_name):
        task = self.get_task(task_name)

        if task:
            subprocess.call('{0}/{1}'.format(self.local_config.get_task_directory(), task['path']))

            return True

        return False
