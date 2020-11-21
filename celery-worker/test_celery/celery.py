import celery


app = celery.Celery("test_celery",
                    include=["test_celery.tasks"])
app.config_from_object("celeryconfig")

if __name__ == "__main__":
    app.start()
