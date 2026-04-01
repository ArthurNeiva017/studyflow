async function loadTasks() {
  const response = await fetch("/tasks");
  const tasks = await response.json();

  const taskList = document.getElementById("taskList");
  taskList.innerHTML = "";

  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.innerHTML = `
      ${task.title} ${task.completed ? "✅" : ""}
      <button onclick="completeTask(${task.id})">Concluir</button>
      <button onclick="deleteTask(${task.id})">Remover</button>
    `;
    taskList.appendChild(li);
  });
}

async function addTask() {
  const input = document.getElementById("taskInput");
  const title = input.value.trim();

  if (!title) return;

  await fetch("/tasks", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ title })
  });

  input.value = "";
  loadTasks();
}

async function completeTask(taskId) {
  await fetch(`/tasks/${taskId}/complete`, {
    method: "PATCH"
  });
  loadTasks();
}

async function deleteTask(taskId) {
  await fetch(`/tasks/${taskId}`, {
    method: "DELETE"
  });
  loadTasks();
}

async function loadStudyTip() {
  const response = await fetch("/study-tip");
  const data = await response.json();

  document.getElementById("studyTip").innerText =
    `Dica: ${data.study_tip}`;
}

loadTasks();