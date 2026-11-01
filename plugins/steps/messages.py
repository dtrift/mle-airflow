from airflow.providers.telegram.hooks.telegram import TelegramHook


def send_telegram_success_message(context):
    # token и chat_id получите у @BotFather и @username_to_id_bot и встройте сюда.
    # В репозитории держим плейсхолдеры: реальный токен коммитить нельзя.
    hook = TelegramHook(token='{token_id}', chat_id='{chat_id}')
    dag = context['dag'].dag_id
    run_id = context['run_id']
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!'
    hook.send_message({'chat_id': '{chat_id}', 'text': message})


def send_telegram_failure_message(context):
    hook = TelegramHook(token='{token_id}', chat_id='{chat_id}')
    dag = context['dag']
    # при неудаче dag в контексте может прийти как объект без dag_id — страхуемся
    dag_id = dag.dag_id if hasattr(dag, 'dag_id') else dag
    run_id = context['run_id']
    task = context['task_instance_key_str']
    message = f'Исполнение DAG {dag_id} с id={run_id} завершилось с ошибкой в задаче {task}!'
    hook.send_message({'chat_id': '{chat_id}', 'text': message})
