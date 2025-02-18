# # import requests
# # import json

# # # Your Frappe site URL (replace if needed)
# # url = "http://task.localhost/api/resource/Task"

# # # Use your API Key and API Secret
# # headers = {
# #     "Authorization": "40a7c0423e65757:f6b09bf77cfec2b"
# #     "Content-Type": "application/json"
# # }

# # # Send GET request to fetch tasks
# # response = requests.get(url, headers=headers)
# # print("GET Request - Status Code:", response.status_code)
# # print("GET Response JSON:", response.json())

# # # POST Request to Create a New Task
# # data = {
# #     "data": {
# #         "task_title": "New api Task",   # Task title or subject
# #         "task_desc": "New api Task dec",
# #         "task_assign": "ravi",
# #         "task_dd": "2025/03/15",
# #         "task_status": "New",                # Status of the task (e.g., Open, In Progress, etc.)
# #         "task_priority": "Low",            # Task priority (e.g., Low, Medium, High)
# #         "project": "Auction System"         # Optional: Link to the project this task belongs to
# #     }
# # }

# # # Send POST request to create a new task
# # response = requests.post(url, headers=headers, data=json.dumps(data))

# # # Check if the request was successful (status code 200)
# # print("POST Request - Status Code:", response.status_code)

# # # Print the response JSON (contains the created task details)
# # print("POST Response JSON:", response.json())

# import requests
# import json

# # Frappe site URL
# url = "http://task.localhost/api/resource/Task"

# # Data for the new Task (make sure field names match with the Task DocType)
# data = {
#         "task_title": "New api Task",   # Task title or subject
#         "task_desc": "New api Task dec",
#         "task_status": "New",                # Status of the task (e.g., Open, In Progress, etc.)
#         "task_priority": "Low", 
#         "task_assign": "ravi",
#         "task_dd": "2025/03/15",           # Task priority (e.g., Low, Medium, High)
#         "project": "Auction System"         # Optional: Link to the project this task belongs to
#     }


# # Headers for the request (including Authorization for security)
# headers = {
#     "Authorization": "40a7c0423e65757:f6b09bf77cfec2b",  # Replace with your token
#     "Content-Type": "application/json"
# }

# # Send the POST request to create the task
# response = requests.post(url, data=json.dumps(data), headers=headers)

# # Check and print response status and data
# if response.status_code == 200:
#     print("Task Created Successfully!")
#     print("Response Data:", response.json())
# else:
#     print("Failed to create task")
#     print("Status Code:", response.status_code)
#     print("Response Text:", response.text)

import requests
import json

task_id = "kusekti0qs"  # Replace with a real Task ID from your GET request
url = f"http://task.localhost/api/resource/Task/{task_id}"

# # Update only the decs
# data = {
#     "task_desc": "changed by api"
# }

headers = {
    "Authorization": "40a7c0423e65757:f6b09bf77cfec2b"
}

response = requests.get(url, data=json.dumps(data), headers=headers)

