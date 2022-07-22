import ftd
import ftd_django

from . import views

@ftd_django.processor("hello_world")
def hello_world(doc_id, section, interpreter):
    return ftd.string_to_value("This is coming from processor")

@ftd_django.processor
def todo_data(doc_id, section, interpreter):
    newlist = views.data
    return ftd.object_to_value(newlist, section, interpreter)

@ftd_django.processor
def reset_todo(doc_id, section, interpreter):
    local_data = [
        {
            "task_name": "Task Name",
            "status": "Status",
            "tid": 1
        },
        {
            "task_name": "ftd application processor for toc data",
            "status": "Done",
            "tid": 2
        },
        {
            "task_name": "call an api to update todo list",
            "status": "In Progress",
            "tid": 3
        },
        {
            "task_name": "documentation for all",
            "status": "Pending",
            "tid": 4
        }
    ]

    return ftd.object_to_value(local_data, section, interpreter)


