import os
broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://");
result_backend = "mongodb://localhost:27017/"
mongodb_backend_settings = {
    "database": "celery-results",
    "user": "admin",
    "password": "password",
    "taskmeta_collection": "my_taskmeta_collection",
}
