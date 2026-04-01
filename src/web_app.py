from flask import Flask, render_template, request, jsonify

from src.task_manager import TaskManager
from src.api_service import get_study_advice

app = Flask(__name__, template_folder="../templates", static_folder="../static")

manager = TaskManager()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(manager.list_tasks())


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Título da tarefa é obrigatório."}), 400

    task = manager.add_task(title)
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    result = manager.complete_task(task_id)

    if not result:
        return jsonify({"error": "Tarefa não encontrada."}), 404

    return jsonify(result)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    result = manager.remove_task(task_id)

    if not result:
        return jsonify({"error": "Tarefa não encontrada."}), 404

    return jsonify({"message": "Tarefa removida com sucesso."})


@app.route("/study-tip", methods=["GET"])
def study_tip():
    return jsonify(get_study_advice())


if __name__ == "__main__":
    app.run(debug=True)