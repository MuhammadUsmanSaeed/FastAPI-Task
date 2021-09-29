from app.celery_app import celery
from database.database import get_db
from models import models


@celery.task(bind=True, name='celery_item')
def celery_item(self, id: int):
    print(id)
    with get_db() as db_session:
        db_session.query(models.Item).filter(models.Item.id == id).delete(synchronize_session=False)
        db_session.commit()
        return {'message': 'Item has been deleted'}
