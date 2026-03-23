from pathlib import Path

import pytest

from src.task_manager import TaskManager


@pytest.fixture
def manager(tmp_path: Path) -> TaskManager:
    return TaskManager(tmp_path / 'tasks.json')


def test_add_task_successfully(manager: TaskManager) -> None:
    task = manager.add_task('Revisar lógica de programação')

    assert task['id'] == 1
    assert task['title'] == 'Revisar lógica de programação'
    assert task['done'] is False
    assert len(manager.list_tasks()) == 1


def test_add_task_with_empty_title_raises_error(manager: TaskManager) -> None:
    with pytest.raises(ValueError, match='A tarefa não pode estar vazia.'):
        manager.add_task('   ')


def test_remove_nonexistent_task_raises_error(manager: TaskManager) -> None:
    with pytest.raises(ValueError, match='Tarefa não encontrada.'):
        manager.remove_task(99)


def test_complete_task_changes_status(manager: TaskManager) -> None:
    task = manager.add_task('Estudar testes automatizados')
    completed = manager.complete_task(task['id'])

    assert completed['done'] is True
    assert manager.list_tasks()[0]['done'] is True


def test_list_tasks_returns_created_items(manager: TaskManager) -> None:
    manager.add_task('Estudar Python')
    manager.add_task('Revisar Git e GitHub')

    tasks = manager.list_tasks()

    assert len(tasks) == 2
    assert tasks[0]['title'] == 'Estudar Python'
    assert tasks[1]['title'] == 'Revisar Git e GitHub'


def test_remove_existing_task_updates_list(manager: TaskManager) -> None:
    first = manager.add_task('Ler documentação do pytest')
    manager.add_task('Treinar exercícios de lógica')

    removed = manager.remove_task(first['id'])
    remaining_tasks = manager.list_tasks()

    assert removed['title'] == 'Ler documentação do pytest'
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0]['title'] == 'Treinar exercícios de lógica'
